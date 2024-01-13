#!/usr/bin/env bash
set -euo pipefail
shopt -s globstar nullglob

verbose=0


usage() {
    printf "Usage: %s [-h]
    
Options:
    -v:     display SLOC per file
    -h:     show this message and exit

Prints the number of source lines of code (SLOC) in ./src directory (excluding 
empty lines).
" "$(basename "$0")"
}


check_args() {
    while getopts ":hv" opt; do
        case "$opt" in
            v)
                verbose=1
                ;;
            h | *)
                usage
                exit 0
        esac
    done
}


main() {
    sum=0
    for file in ./src/**/*.py; do
        lines=$(sed '/^\s*#.*$/d;/^\s*$/d' < "$file" | wc -l) # skips empty and commented out lines
        if [[ "$verbose" -eq 1 ]]; then
            printf "%s: %d\n" "$file" "$lines"
        fi
        sum=$((sum + lines))
    done
    if [[ "$verbose" -eq 1 ]]; then
        printf "total: %d\n" "$sum"
    else
        printf "%d\n" "$sum"
    fi
}


check_args "$@" && main
