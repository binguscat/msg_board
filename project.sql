/*
Names: Russell Rusnell and Lance Cagle
Assignment: SY306 - Course Project
*/

-- Database Creation
DROP DATABASE IF EXISTS Project;
CREATE DATABASE Project;
USE Project;

-- Table Creation
CREATE TABLE user_table (
   username varchar(25) not null,
   name varchar(50) not null,
   password varchar(50) not null,
   admin varchar(5) DEFAULT 'false',
   CONSTRAINT PK_User PRIMARY KEY (username)
);

CREATE TABLE msg_table (
   msgID int auto_increment,
   msg varchar(75) not null,
   username varchar(25) not null,
   time TIME,
   CONSTRAINT PK_Msg PRIMARY KEY (msgID)
);