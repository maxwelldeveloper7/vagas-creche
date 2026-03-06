# Script SQL completo (DDL) para PostgreSQL**, estruturado com:

* tabelas
* chaves primárias
* chaves estrangeiras
* constraints
* índices
* algumas validações de integridade

## Extensão recomendada

```sql
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
```

---

# 1. Tabela de Unidades Escolares

```sql
CREATE TABLE unidades_escolares (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    endereco TEXT,
    ativa BOOLEAN DEFAULT TRUE,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

# 2. Tabela de Usuários

```sql
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    senha_hash TEXT NOT NULL,

    perfil VARCHAR(20) NOT NULL
    CHECK (perfil IN ('administrador','diretor','secretario')),

    unidade_id INTEGER
    REFERENCES unidades_escolares(id),

    ativo BOOLEAN DEFAULT TRUE,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

# 3. Tabela de Responsáveis

```sql
CREATE TABLE responsaveis (
    id SERIAL PRIMARY KEY,

    nome VARCHAR(150) NOT NULL,
    cpf VARCHAR(14) NOT NULL UNIQUE,
    rg VARCHAR(20),

    telefone VARCHAR(20),
    parentesco VARCHAR(50),

    endereco TEXT,
    ponto_referencia TEXT,

    comprovante_endereco BOOLEAN DEFAULT FALSE,

    renda_percapita NUMERIC(10,2),

    mae_vinculo_empregaticio BOOLEAN DEFAULT FALSE,
    comprovante_endereco_trabalho BOOLEAN DEFAULT FALSE,

    demonstrativo_credito_beneficio BOOLEAN DEFAULT FALSE,
    loas_bpc_seguro_desemprego BOOLEAN DEFAULT FALSE,

    autonomo BOOLEAN DEFAULT FALSE,
    mae_matriculada_rede_publica BOOLEAN DEFAULT FALSE,

    vulnerabilidade_social BOOLEAN DEFAULT FALSE,
    declaracao_mae_adolescente BOOLEAN DEFAULT FALSE,

    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

# 4. Tabela de Crianças

```sql
CREATE TABLE criancas (
    id SERIAL PRIMARY KEY,

    nome VARCHAR(150) NOT NULL,
    data_nascimento DATE NOT NULL,

    cpf VARCHAR(14) NOT NULL UNIQUE,

    nome_pai VARCHAR(150),
    nome_mae VARCHAR(150),

    nis VARCHAR(20),
    cartao_sus VARCHAR(20),

    certidao_sem_pai_mae BOOLEAN DEFAULT FALSE,

    laudo_deficiencia BOOLEAN DEFAULT FALSE,
    laudo_neoplasia BOOLEAN DEFAULT FALSE,
    laudo_intolerancia_alimentar BOOLEAN DEFAULT FALSE,
    laudo_neurodivergente BOOLEAN DEFAULT FALSE,

    irmao_matriculado BOOLEAN DEFAULT FALSE,

    encaminhamento_institucional BOOLEAN DEFAULT FALSE,

    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

# 5. Tabela de Inscrições

```sql
CREATE TABLE inscricoes (
    id SERIAL PRIMARY KEY,

    numero_inscricao VARCHAR(30) UNIQUE NOT NULL,

    crianca_id INTEGER NOT NULL
    REFERENCES criancas(id),

    responsavel_id INTEGER NOT NULL
    REFERENCES responsaveis(id),

    unidade_id INTEGER NOT NULL
    REFERENCES unidades_escolares(id),

    vaga_pleiteada VARCHAR(50),
    situacao VARCHAR(50),

    usuario_registro INTEGER
    REFERENCES usuarios(id),

    data_inscricao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

# Índices para desempenho

```sql
CREATE INDEX idx_crianca_cpf
ON criancas(cpf);

CREATE INDEX idx_responsavel_cpf
ON responsaveis(cpf);

CREATE INDEX idx_inscricao_unidade
ON inscricoes(unidade_id);

CREATE INDEX idx_inscricao_data
ON inscricoes(data_inscricao);

CREATE INDEX idx_inscricao_crianca
ON inscricoes(crianca_id);
```

---

# Constraint importante contra duplicidade

Uma criança **não pode ter duas inscrições simultâneas**.

```sql
ALTER TABLE inscricoes
ADD CONSTRAINT unica_inscricao_por_crianca
UNIQUE (crianca_id);
```

---

# Geração automática do número de inscrição

Podemos usar um **trigger**.

## Função

```sql
CREATE OR REPLACE FUNCTION gerar_numero_inscricao()
RETURNS TRIGGER AS $$
BEGIN
    NEW.numero_inscricao :=
    'INS-' ||
    TO_CHAR(NOW(),'YYYY') ||
    '-' ||
    LPAD(nextval('inscricao_seq')::TEXT,6,'0');

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
```

---

## Sequence

```sql
CREATE SEQUENCE inscricao_seq START 1;
```

---

## Trigger

```sql
CREATE TRIGGER trigger_numero_inscricao
BEFORE INSERT ON inscricoes
FOR EACH ROW
EXECUTE FUNCTION gerar_numero_inscricao();
```

---

# Resultado do número de inscrição

Exemplo:

```
INS-2026-000001
INS-2026-000002
INS-2026-000003
```

---

# Segurança recomendada

Nunca armazenar senha simples.

Utilizar **hash bcrypt** no backend.

---

# Estrutura final do banco

```
unidades_escolares
        │
        ├── usuarios
        │
        └── inscricoes
                │
                ├── criancas
                │
                └── responsaveis
```

---

# Esse banco já suporta

✔ cadastro completo
✔ inscrição de irmãos
✔ bloqueio de duplicidade
✔ consultas por CPF
✔ relatórios administrativos
✔ rastreamento por unidade escolar
