# Modelo de Dados — Sistema de Inscrição em Creche

## Entidades principais

1. **usuarios**
2. **unidades_escolares**
3. **responsaveis**
4. **criancas**
5. **inscricoes**

---

# 1. Tabela: unidades_escolares

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

# 2. Tabela: usuarios

Usuários podem ser:

* administrador
* diretor
* secretário

```sql
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    senha_hash TEXT NOT NULL,
    perfil VARCHAR(20) NOT NULL CHECK (perfil IN ('administrador','diretor','secretario')),
    unidade_id INTEGER REFERENCES unidades_escolares(id),
    ativo BOOLEAN DEFAULT TRUE,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

# 3. Tabela: responsaveis

```sql
CREATE TABLE responsaveis (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    cpf VARCHAR(14) NOT NULL,
    rg VARCHAR(20),
    telefone VARCHAR(20),
    parentesco VARCHAR(50),

    endereco TEXT,
    ponto_referencia TEXT,

    comprovante_endereco BOOLEAN DEFAULT FALSE,

    renda_percapita NUMERIC(10,2),

    mae_vinculo_empregaticio BOOLEAN DEFAULT FALSE,
    comprovante_endereco_trabalho BOOLEAN DEFAULT FALSE,

    beneficio_social BOOLEAN DEFAULT FALSE,
    loas_bpc_seguro_desemprego BOOLEAN DEFAULT FALSE,

    autonomo BOOLEAN DEFAULT FALSE,
    mae_matriculada_rede_publica BOOLEAN DEFAULT FALSE,
    vulnerabilidade_social BOOLEAN DEFAULT FALSE,
    declaracao_mae_adolescente BOOLEAN DEFAULT FALSE,

    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

# 4. Tabela: criancas

```sql
CREATE TABLE criancas (
    id SERIAL PRIMARY KEY,

    nome VARCHAR(150) NOT NULL,
    data_nascimento DATE NOT NULL,
    cpf VARCHAR(14) NOT NULL,

    nome_pai VARCHAR(150),
    nome_mae VARCHAR(150),

    nis VARCHAR(20),
    cartao_sus VARCHAR(20),

    laudo_deficiencia BOOLEAN DEFAULT FALSE,
    laudo_neoplasia BOOLEAN DEFAULT FALSE,
    laudo_intolerancia_alimentar BOOLEAN DEFAULT FALSE,
    laudo_neurodivergente BOOLEAN DEFAULT FALSE,

    certidao_sem_pai_mae BOOLEAN DEFAULT FALSE,
    irmao_matriculado BOOLEAN DEFAULT FALSE,

    encaminhamento_institucional BOOLEAN DEFAULT FALSE,

    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

# 5. Tabela: inscricoes

Relaciona **criança + responsável + unidade escolar**.

```sql
CREATE TABLE inscricoes (
    id SERIAL PRIMARY KEY,

    numero_inscricao VARCHAR(30) UNIQUE NOT NULL,

    crianca_id INTEGER NOT NULL REFERENCES criancas(id),
    responsavel_id INTEGER NOT NULL REFERENCES responsaveis(id),

    unidade_id INTEGER NOT NULL REFERENCES unidades_escolares(id),

    vaga_pleiteada VARCHAR(50),
    situacao VARCHAR(50),

    usuario_registro INTEGER REFERENCES usuarios(id),

    data_inscricao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

# Índices recomendados

Para melhorar desempenho das buscas:

```sql
CREATE INDEX idx_crianca_cpf
ON criancas(cpf);

CREATE INDEX idx_responsavel_cpf
ON responsaveis(cpf);

CREATE INDEX idx_inscricao_unidade
ON inscricoes(unidade_id);

CREATE INDEX idx_inscricao_data
ON inscricoes(data_inscricao);
```

---

# Estrutura de relacionamentos

```
unidades_escolares
        │
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

# Regras de negócio importantes no banco

1. **CPF da criança deve ser único por inscrição ativa**
2. **Número da inscrição deve ser único**
3. **Usuários só visualizam inscrições da própria unidade**
4. **Administrador pode visualizar todas**

---

# Estrutura pronta para PostgreSQL

Este modelo suporta diretamente:

* geração de relatórios
* consultas por CPF
* consultas por unidade
* inscrição de irmãos
* histórico de registros

