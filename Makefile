DC = docker-compose

STORAGES_FILE = docker_compose/storages.yml
EXEC = docker exec -it
DB_CONTAINER = db
LOGS = docker logs
ENV_FILE = --env-file .env
APP_CONTAINER = moneytracker-web-1

.PHONY: up
up:
	${DC} up

.PHONY: build
build:
	${DC} build

.PHONY: up-build
up-build:
	${DC} up --build

.PHONY: makemigrations
makemigrations:
	${EXEC} ${APP_CONTAINER} python manage.py makemigrations

.PHONY: migrate
migrate:
	${EXEC} ${APP_CONTAINER} python manage.py migrate
