CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(255) NOT NULL,
    cpf CHAR(11) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL,
    telefone VARCHAR(14) NOT NULL,
    email VARCHAR(100),
    endereco VARCHAR(100) NOT NULL,
    bairro VARCHAR(100) NOT NULL,
    ponto_referencia VARCHAR(255),
    endereco_trabalho TEXT,
    bairro_trabalho VARCHAR(255)
);