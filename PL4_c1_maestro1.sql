\c telpark
BEGIN;

CREATE EXTENSION IF NOT EXISTS postgres_fdw;

DROP SCHEMA IF EXISTS telpark_foraneo CASCADE;
DROP SERVER IF EXISTS maestro2 CASCADE;

CREATE SERVER IF NOT EXISTS maestro2
    FOREIGN DATA WRAPPER postgres_fdw
    OPTIONS (host 'localhost', port '5433', dbname 'telpark');

CREATE USER MAPPING IF NOT EXISTS FOR postgres
    SERVER maestro2
    OPTIONS (user 'postgres', password 'postgres');

CREATE SCHEMA IF NOT EXISTS telpark_foraneo;

IMPORT FOREIGN SCHEMA public
    FROM SERVER maestro2
    INTO telpark_foraneo;

COMMIT;

