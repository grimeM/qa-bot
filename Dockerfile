FROM python:3.11-slim as builder

RUN apt-get update && \
    apt-get install -y libpq-dev gcc

WORKDIR /usr/src

RUN pip install --user pipenv

ADD Pipfile Pipfile.lock ./

ENV PIPENV_VENV_IN_PROJECT=1

RUN python3 -m pipenv sync

FROM python:3.11-slim AS runtime

RUN apt-get update && \
    apt-get install -y libpq-dev && \
    rm -rf /var/lib/apt/lists/*

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY --from=builder /usr/src/.venv/ ./.venv/

COPY ./src /app

CMD ["./.venv/bin/python3", "main.py"]