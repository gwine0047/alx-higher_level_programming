-- This script creates the table state and the database bhtn_0d_usa on MySQL server.
-- states description:
--          id INT unique, primary key, can't be null,
--          name VARCHAR(256) can't be null.
-- if the database hbtn_0d_usa exists, script will not fail
-- if table force_name exists, script will not fail.

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.state (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, name VARCHAR(256) NOT NULL);