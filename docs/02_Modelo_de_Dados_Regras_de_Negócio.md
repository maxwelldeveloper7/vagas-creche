# 1. Modelo de Dados (Conceitual)

## Entidades Principais

1. **Usuário**
2. **UnidadeEscolar**
3. **Inscrição**
4. **Responsável**
5. **Criança**

---

# Entidade: Usuário

Representa quem acessa o sistema.

| Campo      | Tipo    | Observação               |
| ---------- | ------- | ------------------------ |
| id_usuario | inteiro | chave primária           |
| nome       | texto   |                          |
| login      | texto   | único                    |
| senha_hash | texto   | senha criptografada      |
| perfil     | lista   | administrador / operador |
| id_unidade | inteiro | vínculo com unidade      |

---

# Entidade: UnidadeEscolar

| Campo        | Tipo    | Observação                    |
| ------------ | ------- | ----------------------------- |
| id_unidade   | inteiro | chave primária                |
| nome_unidade | texto   |                               |
| diretor      | texto   | cadastrado pelo administrador |
| secretario   | texto   | cadastrado pelo administrador |

Observação importante:

O administrador **não pode editar registros feitos pelo diretor ou secretário**, conforme decisão anterior.

---

# Entidade: Responsável

| Campo                | Tipo    |
| -------------------- | ------- |
| id_responsavel       | inteiro |
| nome                 | texto   |
| cpf                  | texto   |
| rg                   | texto   |
| telefone             | texto   |
| parentesco           | lista   |
| endereco             | texto   |
| ponto_referencia     | texto   |
| comprovante_endereco | lógico  |

### Situação socioeconômica

| Campo                           | Tipo     |
| ------------------------------- | -------- |
| mae_vinculo_empregaticio        | lógico   |
| comprovante_endereco_trabalho   | lógico   |
| demonstrativo_credito_beneficio | lógico   |
| loas_bpc_seguro_desemprego      | lógico   |
| autonomo                        | lógico   |
| mae_matriculada_rede_publica    | lógico   |
| vulnerabilidade_social          | lógico   |
| declaracao_mae_adolescente      | lógico   |
| renda_percapita                 | numérico |

---

# Entidade: Criança

| Campo           | Tipo    |
| --------------- | ------- |
| id_crianca      | inteiro |
| nome            | texto   |
| data_nascimento | data    |
| cpf             | texto   |
| nome_pai        | texto   |
| nome_mae        | texto   |
| nis             | texto   |
| cartao_sus      | texto   |

### Situação escolar

| Campo           | Tipo  |
| --------------- | ----- |
| unidade_escolar | lista |
| situacao        | lista |
| vaga_pleiteada  | lista |

### Condições sociais / jurídicas

| Campo                        | Tipo   |
| ---------------------------- | ------ |
| certidao_sem_pai_ou_mae      | lógico |
| irmao_matriculado            | lógico |
| encaminhamento_institucional | lógico |

### Condições de saúde

| Campo                        | Tipo   |
| ---------------------------- | ------ |
| laudo_deficiencia_neoplasia  | lógico |
| laudo_intolerancia_alimentar | lógico |
| laudo_neurodivergente        | lógico |

---

# Entidade: Inscrição

| Campo            | Tipo      |
| ---------------- | --------- |
| id_inscricao     | inteiro   |
| numero_inscricao | texto     |
| data_inscricao   | data/hora |
| id_usuario       | inteiro   |
| id_unidade       | inteiro   |
| id_responsavel   | inteiro   |
| id_crianca       | inteiro   |

---

# Relacionamentos

```
UnidadeEscolar
      |
      | 1
      |
      |------ N
       Usuario

Responsavel
      |
      | 1
      |
      |------ N
       Crianca

Crianca
      |
      | 1
      |
      |------ 1
       Inscricao

Usuario
      |
      | 1
      |
      |------ N
       Inscricao
```

---

# 2. Regras de Negócio (Business Rules)

## BR-01 — Autenticação obrigatória

Todo acesso ao sistema deve ocorrer mediante **login e senha válidos**.

---

## BR-02 — Perfis de usuário

O sistema possui dois perfis:

**Administrador**

* cadastrar unidades
* cadastrar diretores
* cadastrar secretários
* consultar todas as inscrições
* gerar relatórios

**Operador**

* realizar inscrições
* consultar inscrições da própria unidade
* reemitir comprovantes

---

## BR-03 — Controle por unidade escolar

Operadores **apenas acessam dados da própria unidade escolar**.

---

## BR-04 — Verificação de duplicidade de inscrição

Ao iniciar inscrição:

1. operador informa **CPF da criança**
2. sistema verifica existência de inscrição

Se existir:

* bloqueia nova inscrição
* informa **local e data da inscrição anterior**

---

## BR-05 — Preenchimento automático do CPF

Se não houver inscrição:

* o CPF informado deve ser **armazenado temporariamente**
* deve ser **preenchido automaticamente no cadastro da criança**

---

## BR-06 — Cadastro sequencial de irmãos

Após cadastrar uma criança:

O sistema pergunta:

> Deseja cadastrar outra criança?

Se **sim**:

* abre novo formulário
* reaproveita dados do responsável

---

## BR-07 — Reutilização de dados parentais

O sistema pergunta:

> É filho do mesmo relacionamento?

Se **sim**:

* preenche automaticamente

  * nome do pai
  * nome da mãe

Campos permanecem **editáveis**.

---

## BR-08 — Conferência obrigatória

Antes de salvar a inscrição:

O sistema deve exibir **resumo completo dos dados**.

Campos lógicos devem aparecer **somente quando verdadeiros**.

---

## BR-09 — Geração de número de inscrição

Cada inscrição deve possuir:

* **número único**
* **data e hora do registro**

---

## BR-10 — Comprovante de inscrição

Após salvar inscrição:

O sistema deve:

* gerar comprovante
* permitir impressão
* gerar **PDF**

---

## BR-11 — Segurança do comprovante

O PDF do comprovante deve:

* ser **criptografado**
* ser aberto apenas mediante **CPF da criança**

---

## BR-12 — Reemissão de comprovante

Operadores podem **reemitir comprovantes** de inscrições registradas na própria unidade.

---

## BR-13 — Relatórios administrativos

O sistema deve permitir geração de relatórios:

* lista geral de inscritos
* inscritos por unidade
* inscritos por faixa etária
* inscritos por critérios sociais

Exportação:

* **CSV**