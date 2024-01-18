DC = docker-compose

STORAGES_FILE = docker_compose/storages.yml
EXEC = docker exec -it
DB_CONTAINER = db
LOGS = docker logs
ENV_FILE = --env-file .env

.PHONY: storages
storages:
	${DC} -f ${STORAGES_FILE} ${ENV_FILE} up -d

.PHONY: storages-logs
storages-logs:
	${LOGS} ${DB_CONTAINER} -f

.PHONY: storages-down
storages-down: 
	${DC} -f ${STORAGES_FILE} down