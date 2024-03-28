-- This script creates a table called first_table in database
-- first_table description:
--      id INT
--      name VARCHAR(256)
-- if table exists, script won't fail
--no use of SELECT or SHOW

CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256));
