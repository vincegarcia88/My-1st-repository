CREATE DATABASE IF NOT EXISTS paises; -- comentário de uma linha
/*
comentario com 
mais de uma linha
*/
-- DROP DATABASE IF EXISTS paises;


SHOW DATABASES;

USE paises;

CREATE TABLE IF NOT EXISTS continents(
continent_id INT auto_increment,
name VARCHAR(255) NOT NULL,
PRIMARY KEY (continent_id)
);

DROP table IF EXISTS continents;

CREATE TABLE IF NOT EXISTS continents(
continent_id INT,
name VARCHAR(255)
);

-- para alterar uma tabela
ALTER TABLE continents ADD PRIMARY KEY(continent_id);
ALTER TABLE continents DROP PRIMARY KEY;
ALTER TABLE continents MODIFY COLUMN continent_id INT AUTO_INCREMENT PRIMARY KEY;
ALTER TABLE continents MODIFY COLUMN name VARCHAR(255) NOT NULL;

CREATE TABLE IF NOT EXISTS languages(
	language_id INT AUTO_INCREMENT,
	language VARCHAR(50) NOT NULL,
	PRIMARY KEY(language_id)
;

CREATE TABLE IF NOT EXISTS regions(
	region_id INT AUTO_INCREMENT,
	name VARCHAR(100) NOT NULL,
    continent_id INT,
    PRIMARY KEY(region_id)
    CONSTRAINT fk_regions_continents FOREIGN KEY(continent_id) REFERENCES continents(continent_id)
    );
