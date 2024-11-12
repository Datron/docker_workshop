FROM postgres:12-alpine

COPY ./db-init.sql /docker-entrypoint-initdb.d/db_init.sql
COPY ./data.csv /tmp/data.csv
CMD ["postgres", "-c", "log_statement=all"]
