-- This scrip creates a MySQL user as user_0d_1
-- user_0d_1 has all privileges on the server
-- user_0d_1 password is set to user_0d_1_pwd
-- if user_0d_1 exists, script will not fail

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';