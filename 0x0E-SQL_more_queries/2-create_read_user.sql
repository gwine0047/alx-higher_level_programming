-- This script creates the hbtn_od_2 database and the user user_0d_2.
-- user_0d_2 has only SELECT privilege in this database.
-- the password is set touser_0d_2_pwd

CREATE DATABASE IF NOT EXISTS hbtn_od_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON 'hbtn_0d_2'.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;