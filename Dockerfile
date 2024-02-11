FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Use apt to install packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends python3-dev \
    gcc \
    musl-dev \
    libpq-dev \
    nmap && \
    rm -rf /var/lib/apt/lists/*

ADD pyproject.toml /app

RUN pip install --upgrade pip
RUN pip install poetry 

RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-interaction --no-ansi

COPY . /app/