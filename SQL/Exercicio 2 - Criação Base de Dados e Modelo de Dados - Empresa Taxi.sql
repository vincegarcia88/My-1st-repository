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
    id INT AUTO_INCREMENT PRIMARY KEY,
    Nome_marca VARCHAR(100) NOT NULL
);

-- 3. Tabela de Táxis
CREATE TABLE IF NOT EXISTS taxi(
	Taxi_Matricula VARCHAR (100) AUTO_INCREMENT PRIMARY KEY,
    Nome_carro VARCHAR (100) NOT NULL,
    Marca_ID INT NOT NULL,
    Número_lugares INT NOT NULL,
    Ano_Fabrico YEAR NOT NULL,
    Cor VARCHAR (100),
    GPS BOOLEAN,
    CONSTRAINT FOREIGN KEY (Marca_ID) REFERENCES marcas(id)
);

-- 4. Condutor
CREATE TABLE IF NOT EXISTS Condutor_Info(
	Num_Carta_Conducao PRIMARY KEY INT NOT NULL,
	Nome_condutor VARCHAR (100) NOT NULL,
	Morada_condutor VARCHAR (100) NOT NULL,
	Data_Nascimento DATE NOT NULL,
    Ativo BOOLEAN NOT NULL,
    CONSTRAINT FOREIGN KEY (nome_condutor) REFERENCES taxi(condutor)
);

-- 5. Informação da Viagem
CREATE TABLE IF NOT EXISTS Viagem_taxi(
	Codigo_viagem INT NOT NULL AUTO_INCREMENT,
    data_viagem DATE NOT NULL,
    hora_viagem_ida DATETIME,
    hora_viagem_volta DATETIME,
    numero_passageiros INT NOT NULL,
    preço_viagem DECIMAL (15,2)
);


	

