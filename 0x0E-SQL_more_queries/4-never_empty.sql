-- This script creates the table id_not_null on my MySQL server
-- it does not fail if id_not_null already exists

CREATE TABLE IF NOT EXISTS id_not_null (
       id INT DEFAULT 1,
       name VARCHAR(256)
);
