#!/bin/bash
set -e
# Скрипт создания пользователя `POSTGRES_USER` в БД
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
	CREATE USER $PG_USER WITH PASSWORD '$PG_USER_PASSWORD';
	GRANT ALL PRIVILEGES ON DATABASE $POSTGRES_DB TO $PG_USER;
EOSQL