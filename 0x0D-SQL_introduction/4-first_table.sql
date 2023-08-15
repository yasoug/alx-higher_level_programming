-- This script creates a table called first_table in the current database
-- should not fail if the table first_table already exists
CREATE TABLE IF NOT EXISTS first_table (
	id INT,
	name VARCHAR(256)
);
