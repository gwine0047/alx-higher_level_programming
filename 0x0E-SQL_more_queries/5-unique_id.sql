-- This script creates the table unique_id on MySQL server.
-- unique_id description:
--          id INT with default value = 1 and UNIQUE,
--          name VARCHAR(256).
-- if table force_name exists, script will not fail

CREATE TABLE IF NOT EXISTS unique_id (id INT UNIQUE DEFAULT 1, name VARCHAR(256));