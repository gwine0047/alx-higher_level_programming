--This scripts creates a table calles force_name on MySQL server.
-- force_name description:
--      id INT,
--      name VARCHAR(256) Noy Null;
-- if table force_name exists, script will not fail

CREATE TABLE IF NOT EXISTS force_name (id INT, name VARCHAR(256) NOT NULL);