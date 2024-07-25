-- Exercício Prático 4 - Modelação Base de Dados - Empresa de Táxis

-- Considere o seguinte problema:

-- Uma empresa de táxis pretende implementar uma base de dados com a seguinte informação:

-- A empresa tem vários táxis. Cada táxi tem, para além da matrícula, um nome, a marca, o número de lugares, o ano de fabrico, a cor e se tem GPS. 
-- Existem várias marcas. Para cada marca é necessário guardar o seu ID e nome. 

-- Na empresa trabalham vários condutores de táxi. Para cada condutor é necessário guardar o seu nome, morada e data de nascimento, além do número
-- da sua carta de condução. 

-- Existem condutores que pela sua idade estão apenas em funções administrativas dentro da empresa, estando impossibilitados
-- de conduzir. Cada táxi faz várias viagens. 

-- Cada viagem deve ter a indicação do código, da data e da hora em que se efetua, do local de partida
-- e do local de destino, bem como do número de pessoas que transportou e o preço.

-- Cada viagem de um dado táxi é feita por um condutor apenas. 

-- 1. Faça o modelo ER para o problema apresentado
-- 2. Faça o diagrama ER do modelo criado na pergunta anterior
-- 3. Converta o modelo ER para o modelo racional
-- 4. Crie o diagrama de Modelo relacional

-- 0. Criação do banco de dados
CREATE DATABASE IF NOT EXISTS Empresa_taxi;
USE Empresa_taxi;

-- 1. Tabela de marcas
CREATE TABLE IF NOT EXISTS marca(
	Marca_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Marca_nome VARCHAR (100) NOT NULL
);

-- 2. Tabela de Taxis
CREATE TABLE IF NOT EXISTS Taxi(
	Taxi_matricula VARCHAR (100) PRIMARY KEY,
    Taxi_marca INT NOT NULL,
    Taxi_nome VARCHAR (100) NOT NULL,
    numero_lugares INT NOT NULL,
    ano_fabrico YEAR NOT NULL,
    Cor_Taxi VARCHAR (100) NOT NULL,
    GPS BOOLEAN NOT NULL,
    CONSTRAINT fk_Taxi_marca FOREIGN KEY (Taxi_marca) REFERENCES marca (Marca_ID)
);

-- 3. Tabela de condutores
CREATE TABLE IF NOT EXISTS Condutores(
	Condutor_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Nome_condutor VARCHAR (50) NOT NULL,
    Condutor_Morada VARCHAR (100) NOT NULL,
    Data_nascimento DATE NOT NULL,
    Ativo BOOLEAN NOT NULL
);

-- 4. Tabela de viagens
CREATE TABLE IF NOT EXISTS Viagens(
	Codigo_viagem INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Taxi_matricula VARCHAR (100) NOT NULL,
    Condutor_ID INT NOT NULL,
    Data_viagem DATE NOT NULL,
    Hora_viagem DATETIME NOT NULL,
    Local_partida VARCHAR (100) NOT NULL,
    Local_chegada VARCHAR (100) NOT NULL,
    Numero_pessoas INT NOT NULL,
    Preco_viagem DECIMAL (10,2) NOT NULL,
    CONSTRAINT fk_Viagens_Taxi FOREIGN KEY Taxi_matricula REFERENCES taxi (Taxi_matricula),
    CONSTRAINT fk_Viagens_Condutores FOREIGN KEY Condutor_ID REFERENCES Condutores (Condutor_ID)
);
