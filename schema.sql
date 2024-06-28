PRAGMA foreign_keys= ON;

CREATE TABLE usuarios (
    cpf CHAR(11) PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    telefone VARCHAR(14) NOT NULL,
    email VARCHAR(100) NOT NULL,
    senha VARCHAR(255) DEFAULT NULL
);

CREATE TABLE responsaveis(
    cpf CHAR(11) PRIMARY KEY,
    rg VARCHAR(11) NOT NULL,
    data_nascimento DATE NOT NULL,
    endereco VARCHAR(100) NOT NULL,
    bairro VARCHAR(100) NOT NULL,
    ponto_referencia VARCHAR(255),
    endereco_trabalho TEXT,
    bairro_trabalho VARCHAR(255),
    FOREIGN KEY (cpf) REFERENCES usuarios(cpf)
);
