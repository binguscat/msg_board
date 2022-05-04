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
   password varchar(256) not null,
   admin varchar(5) DEFAULT 'false',
   CONSTRAINT PK_User PRIMARY KEY (username)
);

CREATE TABLE msg_table (
   msgID int auto_increment,
   msg varchar(75) not null,
   username varchar(25) not null,
   time TIMESTAMP not null DEFAULT CURRENT_TIMESTAMP,
   CONSTRAINT PK_Msg PRIMARY KEY (msgID)
);

-- Test insert
INSERT INTO user_table (username,name,password) VALUES ("admin_user","Admin","129589a884d88f3dc379505bb51509b9728ca8a634e068bbaebf6b58dc894b80");

INSERT INTO user_table (username,name,password) VALUES ("normal_user","Normal","81722d1723083bc06233e4c796d67789446f1757ee773356d876ad0ea59b8b41");

UPDATE user_table SET admin='true' WHERE username='admin_user';

INSERT INTO msg_table (msg,username) VALUES ("This is a test message","normal_user");