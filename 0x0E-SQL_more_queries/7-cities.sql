-- This script creates the table CITIES and the database hbtn_0d_usa on MySQL server.
-- CITIES description:
--          id INT unique, primary key, can't be null,
--          state_id INT, must not be null and a FOREIGN KEY
--          name VARCHAR(256) can't be null.
-- if the database hbtn_0d_usa exists, script will not fail
-- if table force_name exists, script will not fail.

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
state_id INT NOT NULL,
name VARCHAR(256) NOT NULL,
FOREIGN KEY(state_id) REFERENCE hbtn_0d_usa.states(id));