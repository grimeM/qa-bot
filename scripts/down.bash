#!/usr/bin/env bash
set -euo pipefail

header=true

config=
context=

docker_opts=()
compose_opts=()

local_config=compose.yml
dev_config=compose.yml
prod_config=compose.yml


usage() {
    printf "Usage: %s [OPTIONS]

Options:
\t-l\tuse local config\t(%s)\t(default)
\t-d\tuse development config\t(%s)
\t-p\tuse production config\t(%s)
\t-R\tuse context \"remote\"
\t-H\thide header
\t-D\tdry run
\t-h\tdisplay this message

Stop service with Docker Compose.
You can specify no more than one of [ldp] options.
" "$(basename "$0")" "$local_config" "$dev_config" "$prod_config"
}


process_args() {
    while getopts ":ldpRDHh" flag; do
        case "$flag" in
            l) [ -n "$config" ] && usage && exit 1 || config="$local_config" ;;
            d) [ -n "$config" ] && usage && exit 1 || config="$dev_config" ;;
            p) [ -n "$config" ] && usage && exit 1 || config="$prod_config" ;;
            R) context="remote";;
            D) compose_opts+=(--dry-run) ;;
            H) header=false ;;
            h) usage && exit 0 ;;
            *) printf "Error: unrecognized option.\n\n" && usage && exit 1 ;;
        esac
    done

    [ -z "$config" ] && config="$local_config"
    [ -z "$context" ] && context="$(docker context show)"

    docker_opts+=(--context "$context")
    compose_opts+=(--file "$config")
}


main() {
    if "$header"; then
        printf "Docker options:\t\t%s\nCompose options:\t%s\n" \
            "${docker_opts[*]}" "${compose_opts[*]}"
    fi

    docker "${docker_opts[@]}" \
        compose "${compose_opts[@]}" \
        down
}


process_args "$@" && main