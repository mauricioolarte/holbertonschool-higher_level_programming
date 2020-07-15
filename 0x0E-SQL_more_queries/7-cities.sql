-- this script create a table and database.
-- table hbtn_0d_usa states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
       id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
       state_id int,
       FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states(id),
       name VARCHAR(256) NOT NULL);
