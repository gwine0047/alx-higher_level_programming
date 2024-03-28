-- This script creates the table CITIES and the database hbtn_0d_usa on MySQL server.

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
state_id INT NOT NULL,
name VARCHAR(256) NOT NULL,
FOREIGN KEY(state_id) REFERENCE hbtn_0d_usa.states(id));
