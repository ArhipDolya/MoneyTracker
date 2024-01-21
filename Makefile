DC = docker-compose

STORAGES_FILE = docker_compose/storages.yml
EXEC = docker exec -it
DB_CONTAINER = db
LOGS = docker logs
ENV_FILE = --env-file .env
APP_CONTAINER = moneytracker-web-1

.PHONY: up
up:
	@docker-compose up

.PHONY: build
build:
	@docker-compose build

.PHONY: up-build
up-build:
	@docker-compose up --build

.PHONY: makemigrations
makemigrations:
	${EXEC} ${APP_CONTAINER} python manage.py makemigrations

.PHONY: migrate
migrate:
	${EXEC} ${APP_CONTAINER} python manage.py migrate
