-- create table and give perm to user
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY UNIQUE,
    states_id INT NOT NULL FOREIGN KEY,
    name VARCHAR(256) NOT NULL
);