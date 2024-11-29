CREATE DATABASE
IF NOT EXISTS task_list;
SHOW DATABASES;
USE task_list;

CREATE TABLE
IF NOT EXISTS user(
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR
(100) NOT NULL,
    email VARCHAR
(100) NOT NULL UNIQUE,
    password VARCHAR
(100) NOT NULL,
    PRIMARY KEY
(id)
);

CREATE TABLE
IF NOT EXISTS task
(
    title VARCHAR
(100) NOT NULL DEFAULT '',
    user_id INT NOT NULL,
    description TEXT,
    priority_value INT DEFAULT 4,
    priority VARCHAR
(20) DEFAULT 'Low',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY
(title, created_at, user_id),
    FOREIGN KEY
(user_id) REFERENCES user
(id) ON
DELETE CASCADE
);

SHOW TABLES;
