-- This script creates the table id_not_null on MySQL server.
-- id_not_null description:
--          id INT with default value = 1,
--          name VARCHAR(256).
-- if table force_name exists, script will not fail

CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256));