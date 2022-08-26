DROP DATABASE IF EXISTS grocery_budget_db;
CREATE DATABASE grocery_budget_db;

-- CREATE TABLE IF NOT EXISTS grocery(
--     id serial NOT NULL,
--     groc_item_title varchar NOT NULL,
--     groc_item_price decimal NOT NULL,
--     groc_item_cat varchar NOT NULL,
--     CONSTRAINT id PRIMARY KEY (id)
-- );

-- CREATE TABLE IF NOT EXISTS budget(
--     id serial NOT NULL,
--     total_budget decimal NOT NULL,
--     item_budget decimal NOT NULL,
--     CONSTRAINT id PRIMARY KEY (id)
-- );

\c grocery_budget_db

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET default_tablespace = '';
SET default_with_oids = false;

