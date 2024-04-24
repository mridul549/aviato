CREATE DATABASE aviato;

USE aviato;

CREATE TABLE videos (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    videoid VARCHAR(255) NOT NULL UNIQUE,
    title VARCHAR(255) NOT NULL,
    description VARCHAR(255),
    channel VARCHAR(255) NOT NULL,
    publishedTime VARCHAR(255) NOT NULL,
    thumbnail VARCHAR(255)
);

CREATE TABLE apikeys (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    keyValue VARCHAR(255) NOT NULL UNIQUE,
    active BOOLEAN DEFAULT TRUE
);