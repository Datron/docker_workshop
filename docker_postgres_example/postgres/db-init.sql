CREATE TABLE IF NOT EXISTS points (x INT NOT NULL, y INT NOT NULL);

COPY points FROM '/tmp/data.csv' DELIMITER ',' CSV HEADER;
