-- Exercício 1 - Criação de base de Dados e Modelo de Dados - Empresa de Táxis
-- Considere o seguinte problema:

-- Uma empresa de táxis pretende implementar uma base de dados com a seguinte informação:

-- A empresa tem vários táxis. Cada táxi tem, para além da matrícula, um nome, a marca, o número de lugares,
-- o ano de fabrico, a cor e se tem GPS.
-- Existem várias marcas. Para cada marca é necessário guardar o seu id e nome. Na empresa trabalham vários condutores de táxi.
-- Para cada condutor é necessário guardar o seu nome, morada e data de nascimento, além do número da sua carta de condução.
-- Existem condutores que pela sua idade estão apenas em funções administrativas dentro da empresa, estando impossibilitados de conduzir.
-- Cada táxi faz várias viagens. Cada viagem deve ter a indicação do código, da data e hora em que se efetua, do local de partida
-- e do local de destino, bem como do número de pessoas que transportou e o preço.
-- Cada viagem de um dado táxi é feita por um condutor apenas.

-- 1. Criação do banco de dados
CREATE DATABASE IF NOT EXISTS empresa_taxi;

USE empresa_taxi;

-- 2. Tabela de Marcas
CREATE TABLE IF NOT EXISTS marcas (
    id_marca INT AUTO_INCREMENT,
    Nome_marca VARCHAR(100) UNIQUE NOT NULL
);

-- 3. Tabela de Táxis
CREATE TABLE IF NOT EXISTS taxis(
	Taxi_Matricula CHAR (8) NOT NULL UNIQUE CHECK (matricula REGEXP '^[0-9A-Z]{2}-[0-9A-Z]{2}-[0-9A-Z]{2}$'),
    Id_taxi INT auto_increment,
    Nome_carro VARCHAR (50) DEFAULT NULL,
    Marca_ID INT,
    Número_lugares TINYINT (1) NOT NULL,
    Ano_Fabrico YEAR (4) NOT NULL,
    Cor VARCHAR (100) NOT NULL,
    GPS BOOLEAN DEFAULT FALSE,
    PRIMARY KEY (id_taxi),
    CONSTRAINT fk_taxis_marcas FOREIGN KEY (Marca_ID) REFERENCES marcas(id_marca)
);

CREATE TABLE paises(
	id_pais INT auto_increment
	nome_pais VARCHAR (50) UNIQUE NOT NULL,
	PRIMARY KEY (id_pais)
);

CREATE TABLE localidades(
	id_localidade INT auto_increment,
	nome_localidade VARCHAR (100) NOT NULL,
	id_pais INT,
	PRIMARY KEY (id_localidade),
	CONSTRAINT fk_localidades_paises FOREIGN KEY(id_pais) REFERENCES paises (id_pais)
);

CREATE TABLE moradas(
	id_morada INT auto_increment,
	arruamento VARCHAR (10) NOT NULL,
	numero_porta INT NOT NULL,
	fracao VARCHAR (10) DEFAULT NULL,
	cod_postal CHAR (8) NOT NULL CHECK (cod_postal REGEXP '^[0-9](4)-[0-9]{3}$'),
	id_localidade INT,
	PRIMARY KEY (id_morada)
);

CREATE TABLE funcoes(
	id_funcao INT auto_increment,
	nome_funcao VARCHAR (50) NOT NULL UNIQUE,
	PRIMARY KEY (id_funcao)
);

-- 4. Condutor
CREATE TABLE IF NOT EXISTS Condutor_Info(
	Num_Carta_Conducao VARCHAR (10) UNIQUE,
    Id_condutor INT auto_increment,
	Nome_condutor VARCHAR (100) NOT NULL,
	Morada_condutor VARCHAR (100) NOT NULL,
	Data_Nascimento DATE NOT NULL,
    Ativo BOOLEAN NOT NULL,
    idade TINYINT (2) NOT NULL CHECK (idade > 0),
    id_funcao INT,
    CONSTRAINT fk_condutores_moradas FOREIGN KEY (id_morada) REFERENCES moradas (id_morada),
    CONSTRAINT fk_condutores_funcoes FOREIGN KEY (id_funcao) REFERENCES funcoes (id_funcao)
    );

-- 5. Informação da Viagem
CREATE TABLE IF NOT EXISTS Viagem_taxi(
	Codigo_viagem INT AUTO_INCREMENT,
    data_viagem DATE NOT NULL,
    hora_viagem_ida DATETIME NOT NULL DEFAULT NOW(),
    hora_viagem_volta DATETIME NULL,
    numero_passageiros TINYINT (1) CHECK (nr_passageiros >= 0),
    preço_viagem DECIMAL (5,2),
    id_taxi INT,
    id_morada_partida INT,
    id_morada_chegada INT,
    PRIMARY KEY (id_viagem),
    CONSTRAINT fk_viagens_taxis FOREIGN KEY (id_taxi) REFERENCES taxis(id_taxi),
    CONSTRAINT fk_viagens_moradas_p FOREIGN KEY (id_morada_partida) REFERENCES moradas (id_morada),
    CONSTRAINT fk_viagens_moradas_c FOREIGN KEY (id_morada_chegada) REFERENCES moradas(id_morada)
);

CREATE TABLE conduzem(
	id_conducao INT auto_increment,
	data_conducao DATE,
	hora_entrada TIME,
	hora_saida TIME,
	id_condutor INT,
	id_taxi INT,
	PRIMARY KEY (id_conducao),
	CONSTRAINT fk_conduzem_condutores FOREIGN KEY (id_condutor) REFERENCES condutores(id_condutor),
	CONSTRAINT fk_conduzem_taxis FOREIGN KEY(id_taxi) REFERENCES taxis(id_taxi)
);

-- Dados continentes
INSERT INTO continents (name) VALUES ('Africa');
INSERT INTO continents (name) VALUES ('Asia');
INSERT INTO continents (name) VALUES ('Europe');
SELECT * FROM continents;

-- Dados linguas
INSERT INTO languages (language) VALUES ('English');
INSERT INTO languages (language) VALUES ('French');
INSERT INTO languages (language) VALUES ('Spanish');

-- Dados regiões
INSERT INTO regions (name, continent_id) VALUES ('Eastern Africa',1);
INSERT INTO regions (name, continent_id) VALUES ('Western Asia',2);
INSERT INTO regions (name, continent_id) VALUES ('Southern Europe',3);

INSERT INTO countries (name, area, national_date, country_code2, country_code3, region_id)
VALUES ('Kenya',580367.00,'1963-12-12', 'KE', 'KEN',1);

INSERT INTO countries (name, area, national_date, country_code2, country_code3, region_id)
VALUES ('Turkey',783556.00,'1923-10-29', 'TR', 'TUR',2);

INSERT INTO countries (name, area, national_date, country_code2, country_code3, region_id)
VALUES ('Italy',301340.00,'1861-03-17', 'IT', 'ITA',3);

-- Dados da relação entre os países e as línguas
INSERT INTO country_languages (country_id, language_id, official) values (1,2, TRUE);
INSERT INTO country_languages (country_id, language_id, official) values (2,3, TRUE);
INSERT INTO country_languages (country_id, language_id, official) values (3,1, TRUE);
INSERT INTO country_languages (country_id, language_id, official) values (3,2, TRUE);

DELETE FROM continents; -- apaga TODOS os registros da tabela
DELETE FROM continents WHERE continent_id = 4; -- apaga apenas um registro
DELETE FROM continents WHERE name = 'America'; -- Apaga apenas um trgistro
DELETE FROM continents WHERE continent_id IN(5,6);
DELETE FROM continents WHERE name IN('Oceania', 'Coiso');