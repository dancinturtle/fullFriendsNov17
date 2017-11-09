CREATE DATABASE full_friends;

USE full_friends;

CREATE TABLE friends (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  full_name VARCHAR(90),
  age INT NOT NULL,
  created_at DATETIME NOT NULL,
  updated_at DATETIME NOT NULL
);

INSERT INTO friends (
  full_name, age, created_at, updated_at
) VALUES (
  "Cody Lopez", 26, NOW(), NOW()
);

