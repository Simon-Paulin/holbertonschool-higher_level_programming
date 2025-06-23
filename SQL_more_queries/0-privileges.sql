-- create user
CREATE USER 'user_0d_1'@'localhost' INDENTIFIED WITH authentication_plugin BY 'passport';
CREATE USER 'user_0d_2'@'localhost' INDENTIFIED WITH authentication_plugin BY 'passport';
-- list all privileges
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';