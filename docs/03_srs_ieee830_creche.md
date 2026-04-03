# Especificação de Requisitos de Software
## Sistema de Inscrição em Creche da Rede Municipal

**Padrão:** IEEE 830-1998  
**Versão:** 1.0  
**Licença:** GNU General Public License (GPL)  
**Data:** 2026  
**Status:** Em elaboração  

---

## Histórico de Revisões

| Versão | Data | Descrição | Autor |
|--------|------|-----------|-------|
| 1.0 | 2026 | Versão inicial derivada do PRD v2.0 e modelagem de dados v3 | Equipe técnica |

---

## Sumário

1. [Introdução](#1-introdução)
2. [Descrição Geral](#2-descrição-geral)
3. [Requisitos de Interface Externa](#3-requisitos-de-interface-externa)
4. [Requisitos Funcionais](#4-requisitos-funcionais)
5. [Requisitos Não Funcionais](#5-requisitos-não-funcionais)
6. [Restrições de Projeto](#6-restrições-de-projeto)
7. [Atributos do Sistema](#7-atributos-do-sistema)
8. [Apêndices](#8-apêndices)

---

## 1. Introdução

### 1.1 Propósito

Este documento especifica os requisitos de software do **Sistema de Inscrição em Creche da Rede Municipal**, doravante denominado **SICREM**. Destina-se a desenvolvedores, testadores e gestores responsáveis pela implementação, validação e manutenção do sistema.

O documento segue o padrão IEEE 830-1998 e complementa o Documento de Requisitos de Produto (PRD v2.0), incorporando decisões técnicas tomadas durante a modelagem de dados e as revisões de especificação.

### 1.2 Escopo

O SICREM é um sistema web para **registro, controle e gerenciamento de pré-matrículas de crianças em creches da rede municipal de educação**. O sistema:

- centraliza e padroniza o processo de inscrição, anteriormente conduzido de forma presencial via Google Forms na Secretaria Municipal de Educação
- descentraliza o atendimento para as 14 unidades escolares da rede
- garante rastreabilidade, integridade e auditabilidade de todas as operações
- gera comprovantes de inscrição em PDF protegidos por senha
- produz relatórios e exportações CSV para planejamento educacional

**Fora do escopo:**

- critérios de priorização e chamada de vagas
- convocação de responsáveis
- gestão de fila de atendimento presencial
- matrícula definitiva

### 1.3 Definições, Acrônimos e Abreviações

| Termo | Definição |
|-------|-----------|
| SICREM | Sistema de Inscrição em Creche da Rede Municipal |
| PRD | Product Requirements Document — documento de requisitos de produto |
| SRS | Software Requirements Specification — este documento |
| LGPD | Lei Geral de Proteção de Dados Pessoais (Lei 13.709/2018) |
| RBAC | Role-Based Access Control — controle de acesso baseado em perfis |
| CPF | Cadastro de Pessoas Físicas — identificador único de pessoa física no Brasil |
| NIS | Número de Identificação Social |
| CRAS | Centro de Referência de Assistência Social |
| CREAS | Centro de Referência Especializado de Assistência Social |
| BPC | Benefício de Prestação Continuada |
| LOAS | Lei Orgânica da Assistência Social |
| DDL | Data Definition Language — linguagem de definição de estrutura de banco de dados |
| FK | Foreign Key — chave estrangeira |
| PK | Primary Key — chave primária |
| PDF | Portable Document Format |
| CSV | Comma-Separated Values |
| HTTPS | Hypertext Transfer Protocol Secure |
| ORM | Object-Relational Mapping |
| JWT | JSON Web Token |
| TIMESTAMPTZ | Timestamp with time zone — tipo de dado PostgreSQL |

### 1.4 Referências

- PRD — Sistema de Inscrição em Creche da Rede Municipal, v2.0, 2026
- Modelagem de dados DBML v3, 2026
- DDL PostgreSQL v1.0, 2026
- IEEE Std 830-1998 — IEEE Recommended Practice for Software Requirements Specifications
- Lei Geral de Proteção de Dados Pessoais — Lei 13.709/2018
- Lei Federal 15.211/2025 (Lei FELCA)
- GNU General Public License (GPL)

### 1.5 Visão Geral do Documento

A seção 2 descreve o contexto e as características gerais do sistema. A seção 3 especifica as interfaces externas. A seção 4 detalha todos os requisitos funcionais organizados por módulo. A seção 5 especifica os requisitos não funcionais. A seção 6 lista as restrições de projeto. A seção 7 descreve os atributos de qualidade do sistema. A seção 8 contém apêndices de referência.

---

## 2. Descrição Geral

### 2.1 Perspectiva do Produto

O SICREM substitui o processo manual de inscrição conduzido via Google Forms na Secretaria Municipal de Educação. A mudança principal é a **descentralização do atendimento**: de um único ponto centralizado na Secretaria para 14 unidades escolares distribuídas pelo município.

O sistema opera de forma **totalmente online**, sem modo offline. A Secretaria Municipal de Educação mantém visibilidade centralizada de todas as inscrições em tempo real.

```
┌─────────────────────────────────────────────────────┐
│              Rede Municipal de Educação             │
│                                                     │
│  ┌──────────────────┐    ┌──────────────────────┐   │
│  │ Secretaria Mun.  │    │  14 Unidades         │   │
│  │ de Educação      │    │  Escolares           │   │
│  │                  │    │                      │   │
│  │ • Visibilidade   │    │ • Registro de        │   │
│  │   global         │◄───│   inscrições         │   │
│  │ • Relatórios     │    │ • Atendimento        │   │
│  │ • Exportação CSV │    │   presencial         │   │
│  └──────────────────┘    └──────────────────────┘   │
│                   ▲              ▲                  │
│                   └──────────────┘                  │
│                       SICREM                        │
└─────────────────────────────────────────────────────┘
```

### 2.2 Funções do Produto

As funções principais do SICREM são:

1. **Autenticação e controle de acesso** — login seguro com controle por perfil (RBAC)
2. **Gestão da estrutura escolar** — cadastro de unidades, turmas e períodos de inscrição
3. **Registro de inscrições** — cadastro de responsáveis, crianças e pré-matrículas
4. **Geração de comprovantes** — PDF protegido por senha baseada no CPF da criança
5. **Consulta de inscrições** — busca por CPF, nome, número de inscrição e ano letivo
6. **Relatórios administrativos** — consolidação de dados por unidade, turma e critérios sociais
7. **Exportação CSV** — arquivo oficial ao encerramento do período
8. **Auditoria** — registro imutável de todas as operações do sistema

### 2.3 Características dos Usuários

| Perfil | Características técnicas | Responsabilidades no sistema |
|--------|--------------------------|------------------------------|
| Administrador | Perfil técnico — profissional de TI | Configuração, cadastro de Secretários de Educação, definição de períodos |
| Secretário de Educação | Perfil administrativo — gestor público | Cadastro de unidades, diretores e secretários escolares; supervisão global |
| Diretor | Perfil operacional — sem expertise técnica avançada | Registro de inscrições na própria unidade |
| Secretário Escolar | Perfil operacional — sem expertise técnica avançada | Registro de inscrições na própria unidade (mesmas permissões do Diretor) |

### 2.4 Restrições Gerais

- o sistema opera exclusivamente online — não há modo offline
- o atendimento é presencial nas unidades escolares, com senha física gerenciada fora do sistema
- nenhuma inscrição pode ser excluída — apenas consultada e, dentro do período aberto, editada
- o CPF é campo obrigatório para inscrição de crianças
- a data de corte etário é **31 de março** do ano letivo

### 2.5 Suposições e Dependências

- todas as unidades escolares possuem acesso à internet durante o período de inscrição
- os operadores (Diretores e Secretários Escolares) possuem e-mail institucional válido para recuperação de acesso
- o servidor de aplicação e o banco de dados PostgreSQL estão provisionados antes da implantação
- as faixas etárias por tipo de turma seguem a tabela `definicoes_turma` do banco de dados, podendo ser ajustadas pela Secretaria Municipal mediante atualização do seed

---

## 3. Requisitos de Interface Externa

### 3.1 Interfaces de Usuário

O sistema é uma aplicação web responsiva acessível via navegador moderno (Chrome, Firefox, Edge — versões dos últimos 24 meses).

**Princípios de interface:**

- formulários simples e objetivos, adequados a operadores sem perfil técnico avançado
- preenchimento automático sempre que possível (CPF pré-preenchido, turma sugerida, dados do responsável reutilizados para irmãos)
- mensagens de erro claras e orientadas à ação
- campos lógicos (checkboxes) exibidos no resumo da inscrição apenas quando marcados como verdadeiros

**Telas principais por perfil:**

| Perfil | Telas |
|--------|-------|
| Administrador | Login, Painel, Períodos de inscrição, Cadastro de Secretários de Educação |
| Secretário de Educação | Login, Painel, Unidades escolares, Usuários, Consulta global, Relatórios, Exportação CSV |
| Diretor / Secretário Escolar | Login, Painel, Turmas, Nova inscrição, Consulta, Reemissão de comprovante, Relatórios da unidade |

### 3.2 Interfaces de Hardware

Não há requisitos de hardware específicos além de dispositivo com navegador web e acesso à internet. Requisitos mínimos de hardware e navegador serão documentados no Manual de Implantação (artefato externo a este SRS).

### 3.3 Interfaces de Software

| Componente | Tecnologia | Versão mínima |
|------------|------------|---------------|
| Linguagem de backend | Python | 3.11 |
| Framework web | Flask | 3.x |
| ORM | SQLAlchemy | 2.x |
| Banco de dados | PostgreSQL | 14 |
| Geração de PDF | Biblioteca a definir (ex: ReportLab, WeasyPrint) | — |
| Proteção de PDF | PyMuPDF ou pypdf com suporte a criptografia | — |
| Hash de senha | bcrypt ou argon2-cffi | — |
| Autenticação de sessão | Flask-Login + JWT ou sessão server-side | — |

### 3.4 Interfaces de Comunicação

- toda comunicação entre cliente e servidor ocorre via **HTTPS** (TLS 1.2 ou superior)
- não há integrações com sistemas externos na versão 1.0
- o servidor de e-mail (SMTP) deve estar configurado para envio de tokens de recuperação de senha

---

## 4. Requisitos Funcionais

Os requisitos funcionais são organizados por módulo. Cada requisito recebe um identificador único no formato **RF-XXX**.

---

### 4.1 Módulo de Autenticação

#### RF-001 — Login

O sistema deve permitir autenticação de usuários previamente cadastrados mediante CPF ou e-mail institucional e senha.

**Fluxo principal:**
1. usuário informa CPF ou e-mail e senha
2. sistema valida credenciais contra a base de usuários
3. sistema verifica se a conta está ativa
4. sistema redireciona ao painel correspondente ao perfil autenticado
5. sistema registra o evento de login bem-sucedido no `audit_log`

**Fluxos alternativos:**

- **FA-001a — Credenciais inválidas:** sistema exibe mensagem de erro genérica (sem indicar se CPF/e-mail ou senha está incorreto), incrementa `tentativas_login` e registra a tentativa no `audit_log`
- **FA-001b — Conta bloqueada:** sistema exibe mensagem informando que a conta está bloqueada e orienta o usuário a acionar o fluxo de recuperação
- **FA-001c — Conta inativa:** sistema exibe mensagem informando que a conta está inativa e orienta contato com o superior hierárquico

**Regras:**
- o número máximo de tentativas inválidas consecutivas é configurável pelo Administrador
- após atingir o limite, a conta é bloqueada automaticamente
- o contador `tentativas_login` é zerado após login bem-sucedido

---

#### RF-002 — Recuperação de Acesso por E-mail

O sistema deve permitir que usuários bloqueados ou com senha esquecida redefinam suas credenciais de forma autônoma via e-mail institucional.

**Fluxo principal:**
1. usuário acessa a tela de recuperação e informa CPF ou e-mail institucional
2. sistema localiza o cadastro e envia link de redefinição ao e-mail institucional vinculado
3. usuário acessa o link e define nova senha
4. sistema invalida o token e encerra todas as sessões ativas do usuário
5. sistema registra o evento no `audit_log` com IP, dispositivo e timestamp

**Regras:**
- o token de redefinição tem validade de **1 hora**
- após uso ou expiração, o token é invalidado e não pode ser reutilizado
- o e-mail institucional é cadastrado pelo superior hierárquico e não pode ser alterado pelo próprio usuário
- alterações no e-mail institucional são registradas no `audit_log`

**Hierarquia de suporte para casos excepcionais:**

| Usuário com problema | Aciona |
|----------------------|--------|
| Diretor / Secretário Escolar sem acesso ao e-mail | Secretário de Educação |
| Secretário de Educação | Administrador |

---

#### RF-003 — Logout

O sistema deve encerrar a sessão do usuário mediante ação explícita de logout, invalidando o token de sessão.

---

#### RF-004 — Controle de Acesso por Perfil (RBAC)

O sistema deve aplicar controle de acesso baseado em perfil para todas as funcionalidades, conforme a matriz de permissões definida no PRD v2.0, seção 3.5.

**Regras:**
- Diretores e Secretários Escolares acessam exclusivamente dados da unidade à qual estão vinculados
- tentativas de acesso a recursos não autorizados são registradas no `audit_log`
- o perfil do usuário é verificado a cada requisição, não apenas no login

---

### 4.2 Módulo de Gestão da Estrutura Escolar

#### RF-005 — Cadastro de Unidades Escolares

O Secretário de Educação deve ser capaz de cadastrar, editar e ativar/inativar unidades escolares.

**Campos obrigatórios:** nome, endereço, telefone, status  
**Campos opcionais:** nenhum

**Regras:**
- o nome da unidade deve ser único no sistema
- uma unidade inativa não aparece como opção de unidade pretendida no formulário de inscrição
- inativar uma unidade não afeta inscrições já registradas

---

#### RF-006 — Cadastro de Usuários

O Administrador cadastra Secretários de Educação. O Secretário de Educação cadastra Diretores e Secretários Escolares, vinculando-os a uma unidade.

**Campos obrigatórios:** CPF, nome, e-mail institucional, perfil, unidade (para Diretor e Secretário Escolar)

**Regras:**
- CPF e e-mail institucional devem ser únicos no sistema
- Diretores e Secretários Escolares devem obrigatoriamente ter `unidade_id` preenchido — constraint garantida no banco de dados
- a senha inicial é gerada pelo sistema e enviada ao e-mail institucional do novo usuário
- o cadastro de usuário é registrado no `audit_log`

---

#### RF-007 — Configuração do Período de Inscrição

O Administrador deve ser capaz de criar e gerenciar períodos de inscrição.

**Campos obrigatórios:** ano letivo, data de início, data de encerramento, status

**Regras:**
- existe apenas um período por ano letivo — garantido por constraint `UNIQUE` no banco
- `data_encerramento` deve ser posterior a `data_inicio` — garantido por `CHECK` no banco
- apenas o Administrador pode criar, editar e encerrar períodos
- ao encerrar um período (`status = encerrado`), nenhuma inscrição pode ser criada ou editada
- o encerramento do período é registrado no `audit_log`

---

#### RF-008 — Cadastro de Turmas

O Diretor ou Secretário Escolar deve ser capaz de cadastrar turmas para a própria unidade, vinculando-as a um período letivo.

**Campos obrigatórios:** nome, turno, definição de turma (`definicao_id`), unidade, período

**Regras:**
- a turma é associada à combinação `(unidade_id, turma_id, periodo_id)` na tabela `unidade_turma`
- as vagas são definidas por unidade e por período — não são atributo fixo da turma
- o número de vagas deve ser maior que zero — garantido por `CHECK` no banco
- o Diretor só pode cadastrar turmas da própria unidade

---

### 4.3 Módulo de Inscrição

#### RF-009 — Início da Inscrição por CPF da Criança

O Diretor ou Secretário Escolar inicia uma inscrição informando o CPF da criança.

**Fluxo principal:**
1. operador informa o CPF da criança
2. sistema valida o formato e os dígitos verificadores do CPF
3. sistema verifica se já existe inscrição ativa para o CPF no período vigente
4. **se não existir:** sistema pré-preenche o CPF no formulário da criança e prossegue para RF-010
5. **se existir:** sistema bloqueia nova inscrição e exibe data, horário e unidade da inscrição já registrada

**Regras:**
- a verificação de duplicidade é feita pelo índice único `(crianca_id, periodo_id)` no banco
- o período vigente é identificado pelo `status = aberto` em `periodos_inscricao`
- se não houver período aberto, o sistema bloqueia o início de novas inscrições e exibe mensagem explicativa ao operador

---

#### RF-010 — Cadastro do Responsável

Após o início da inscrição, o sistema apresenta o formulário de cadastro do responsável.

**Campos obrigatórios:** nome, CPF, RG, telefone, logradouro, número, bairro, município, UF, CEP

**Campos opcionais:** complemento, ponto de referência, endereço do trabalho (logradouro, bairro, município, UF, CEP)

**Campos da situação socioeconômica (todos opcionais):**
- mãe com vínculo empregatício
- mãe trabalhadora autônoma
- LOAS / BPC
- seguro-desemprego
- mãe matriculada em rede pública de ensino
- situação de vulnerabilidade social
- renda per capita familiar

**Regras:**
- CPF do responsável deve ser válido (dígitos verificadores)
- CEP deve conter exatamente 8 dígitos numéricos — garantido por `CHECK` no banco
- se o CPF do responsável já estiver cadastrado (responsável com múltiplas crianças), o sistema reutiliza os dados existentes e permite edição para o registro atual
- o cadastro do responsável é registrado no `audit_log`

---

#### RF-011 — Cadastro da Criança

Após o cadastro do responsável, o sistema apresenta o formulário de cadastro da criança.

**Campos obrigatórios:** nome, CPF (pré-preenchido), data de nascimento

**Campos opcionais:** nome do pai, nome da mãe

**Campos de solicitação de vaga:**
- unidade escolar pretendida (qualquer unidade ativa da rede — escolha livre do responsável)
- turma pretendida (sugerida automaticamente; seleção incompatível é bloqueada, pois as opções deste campo serão filtradas e haverá uma lista apenas com turmas compatíveis de acordo com o corte etário)

**Campos de situação documental (opcionais):**
- certidão em que não conste pai ou mãe
- irmão matriculado em unidade da rede municipal

**Campos de encaminhamentos institucionais (opcionais):**
- Vara da Família
- Conselho Tutelar
- CRAS / CREAS
- Casa de acolhimento

**Campos de dados sociais e de saúde (opcionais):**
- NIS (`char(13)`)
- número do cartão SUS (`char(15)`)
- laudo de deficiência ou neoplasia
- laudo de intolerância alimentar
- laudo de neurodivergência

**Regras:**
- a idade da criança é calculada com base na data de corte **31 de março** do ano letivo vigente
- o sistema calcula automaticamente a faixa etária elegível e sugere a turma compatível
- seleção de turma incompatível com a idade calculada é impossibilitada, pois o campo só reenderizará lista permitida pelo corte etário. Caso a idade da criança seja imconpativel o sistema emite uma mesagem 'Idade inválida'
- o parentesco entre responsável e criança é registrado em `responsaveis_criancas`

---

#### RF-012 — Cadastro de Irmãos

Após concluir o cadastro de uma criança, o sistema deve perguntar se o responsável deseja inscrever outra criança.

**Fluxo:**
1. sistema exibe: *"Deseja cadastrar outra criança para este responsável?"*
2. se positivo: abre novo formulário de criança com dados do responsável reutilizados
3. sistema pergunta: *"É filho(a) do mesmo relacionamento?"*
4. se sim: preenche automaticamente nome do pai e nome da mãe
5. todos os campos permanecem editáveis

**Regras:**
- o vínculo de irmãos é implícito pelo compartilhamento do `responsavel_id` em `responsaveis_criancas`
- cada criança passa pelo fluxo completo de validação de CPF e faixa etária

---

#### RF-013 — Conferência da Inscrição

Antes de salvar, o sistema deve exibir um resumo completo de todas as informações registradas.

**Informações exibidas:**
- dados do responsável
- dados da criança
- situação socioeconômica informada
- documentos informados
- encaminhamentos institucionais
- dados sociais e de saúde
- unidade pretendida e turma pretendida

**Regras:**
- campos lógicos (booleanos) aparecem no resumo **apenas quando verdadeiros**
- o operador pode retornar a qualquer seção para corrigir informações antes de confirmar
- a confirmação é explícita — o operador deve acionar um botão de confirmação

---

#### RF-014 — Registro da Inscrição

Ao confirmar, o sistema registra a inscrição no banco de dados.

**Regras:**
- `numero_inscricao` é gerado automaticamente no formato `AAAA` + sequência com zeros à esquerda (ex: `202600001`)
- `criado_em` é preenchido pelo banco via `DEFAULT NOW()` — não pela aplicação
- a FK composta `(responsavel_id, crianca_id)` deve existir em `responsaveis_criancas` antes do registro
- a FK composta `(unidade_id, turma_id, periodo_id)` deve existir em `unidade_turma`
- inscrições não podem ser excluídas — apenas editadas dentro do período aberto
- o registro é auditado no `audit_log` com operação `C`

---

#### RF-015 — Edição de Inscrição

O Diretor ou Secretário Escolar pode editar inscrições da própria unidade dentro do período oficial aberto.

**Regras:**
- edição bloqueada automaticamente após `status = encerrado` em `periodos_inscricao`
- cada campo alterado gera entrada no `audit_log` com `operacao = U`, contendo campo, valor anterior e valor novo no `payload_diff`
- o Secretário de Educação e o Administrador não podem editar inscrições

---

### 4.4 Módulo de Comprovante

#### RF-016 — Geração de Comprovante em PDF

Após o registro da inscrição, o sistema gera automaticamente um comprovante em PDF.

**Conteúdo do comprovante:**

*Identificação da inscrição:*
- número da inscrição
- data e hora do registro
- unidade onde foi realizada a inscrição
- ano letivo

*Dados da criança:*
- nome completo, CPF, data de nascimento, nome do pai, nome da mãe

*Dados do responsável:*
- nome completo, CPF, telefone, endereço

*Solicitação:*
- unidade escolar pretendida
- turma pretendida

**Regras:**
- o PDF é gerado com proteção de abertura por senha baseada no CPF da criança (apenas dígitos, sem formatação)
- o comprovante pode ser impresso diretamente ou baixado
- a geração do comprovante é registrada no `audit_log` com operação `R`

---

#### RF-017 — Reemissão de Comprovante

O sistema deve permitir a reemissão do comprovante de inscrição.

**Regras:**
- Diretores e Secretários Escolares podem reemitir comprovantes da própria unidade
- o Secretário de Educação pode reemitir comprovantes de qualquer unidade
- cada reemissão é registrada no `audit_log` com operação `R`

---

### 4.5 Módulo de Consulta

#### RF-018 — Consulta de Inscrições

O sistema deve permitir consulta de inscrições por múltiplos critérios.

**Filtros disponíveis:**
- nome da criança
- CPF da criança
- número da inscrição
- ano letivo (**obrigatório** — padrão: ano letivo vigente)
- unidade escolar (disponível apenas para Secretário de Educação e Administrador)

**Regras:**
- Diretores e Secretários Escolares visualizam apenas inscrições da própria unidade
- o Secretário de Educação visualiza inscrições de todas as unidades
- a consulta é registrada no `audit_log` com operação `R` quando envolve dados sensíveis individuais

---

### 4.6 Módulo de Relatórios

#### RF-019 — Relatórios Administrativos

O sistema deve gerar os seguintes relatórios:

| Relatório | Conteúdo |
|-----------|----------|
| Lista geral de inscritos | Número da inscrição, nome da criança, unidade pretendida, turma pretendida, data da inscrição |
| Inscrições por unidade | Demanda por escola — subsidia planejamento de abertura de turmas |
| Inscrições por turma / faixa etária | Subsidia planejamento da oferta de vagas |
| Critérios sociais | Renda per capita, vulnerabilidade, benefícios, encaminhamentos |

**Regras:**
- todos os relatórios permitem filtragem por ano letivo
- relatórios globais disponíveis apenas para Secretário de Educação e Administrador
- Diretores e Secretários Escolares acessam relatórios apenas da própria unidade

---

#### RF-020 — Exportação CSV

O sistema deve disponibilizar exportação em CSV de todos os registros do período.

**Regras:**
- todos os relatórios podem ser exportados em CSV
- após o encerramento do período, o sistema disponibiliza o **arquivo CSV oficial** com todos os registros do período
- a exportação CSV oficial é disponível apenas para Administrador e Secretário de Educação
- a exportação é registrada no `audit_log` com operação `R`

---

### 4.7 Módulo de Auditoria

#### RF-021 — Registro de Operações

O sistema deve registrar todas as operações em `audit_log` de forma automática e transparente ao operador.

**Operações registradas:**

| Código | Operação |
|--------|----------|
| C | Criação de registros |
| R | Leitura de dados sensíveis |
| U | Atualização de registros |

**Campos obrigatórios por evento:**

| Campo | Descrição |
|-------|-----------|
| `usuario_id` | CPF do usuário autenticado |
| `perfil_usuario` | Perfil do usuário no momento da operação |
| `entidade` | Tabela afetada (ex: `inscricoes`, `usuarios`) |
| `registro_id` | Identificador do registro afetado |
| `operacao` | C, R ou U |
| `payload_diff` | JSONB com campo, valor anterior e valor novo (apenas para U) |
| `ip_origem` | Endereço IP da requisição (IPv4 ou IPv6) |
| `dispositivo` | User agent do navegador |
| `ocorrido_em` | Timestamp com fuso horário (TIMESTAMPTZ) |

**Regras:**
- registros de auditoria são **imutáveis** — `UPDATE` e `DELETE` são bloqueados por `RULE` no banco de dados
- `usuario_id` não possui FK intencional — o log deve sobreviver à desativação do usuário
- `ocorrido_em` é preenchido pelo banco via `DEFAULT NOW()`

---

## 5. Requisitos Não Funcionais

### 5.1 Desempenho

| Requisito | Descrição |
|-----------|-----------|
| RNF-001 | O tempo de resposta para operações de consulta simples (por CPF ou número de inscrição) não deve exceder 2 segundos em condições normais de uso |
| RNF-002 | A geração do comprovante em PDF não deve exceder 5 segundos |
| RNF-003 | O sistema deve suportar os 14 operadores simultâneos (um por unidade) sem degradação de desempenho |

### 5.2 Segurança

| Requisito | Descrição |
|-----------|-----------|
| RNF-004 | Toda comunicação deve ocorrer via HTTPS com TLS 1.2 ou superior |
| RNF-005 | Senhas devem ser armazenadas com hash bcrypt (fator de custo mínimo 12) ou argon2 |
| RNF-006 | Tokens de recuperação de senha têm validade máxima de 1 hora e uso único |
| RNF-007 | O sistema deve bloquear a conta após número configurável de tentativas de login inválidas consecutivas |
| RNF-008 | Comprovantes PDF devem ser protegidos por senha baseada no CPF da criança (apenas dígitos) |
| RNF-009 | Dados pessoais sensíveis (laudos, NIS, situação social) devem ser acessíveis apenas por usuários autorizados conforme RBAC |
| RNF-010 | O `audit_log` deve ser protegido contra `UPDATE` e `DELETE` por `RULE` no PostgreSQL |

### 5.3 Disponibilidade

| Requisito | Descrição |
|-----------|-----------|
| RNF-011 | Em caso de indisponibilidade, o sistema deve exibir mensagem clara ao operador informando a falha |
| RNF-012 | Formulários em andamento não devem ser perdidos em caso de queda de conexão momentânea — o sistema deve alertar o operador antes de qualquer perda de dados |
| RNF-013 | Requisitos de SLA e plano de contingência serão definidos no documento SRS complementar de infraestrutura |

### 5.4 Manutenibilidade

| Requisito | Descrição |
|-----------|-----------|
| RNF-014 | O código-fonte deve seguir PEP 8 para Python |
| RNF-015 | O sistema deve possuir ambiente de homologação separado do ambiente de produção |
| RNF-016 | Toda configuração de ambiente (strings de conexão, chaves secretas, SMTP) deve ser gerenciada via variáveis de ambiente — nunca hardcoded |

### 5.5 Portabilidade

| Requisito | Descrição |
|-----------|-----------|
| RNF-017 | O sistema deve ser executável em qualquer distribuição Linux que suporte Python 3.11+ e PostgreSQL 14+ |
| RNF-018 | O sistema deve funcionar nos navegadores Chrome, Firefox e Edge nas versões dos últimos 24 meses |

### 5.6 Conformidade Legal

| Requisito | Descrição |
|-----------|-----------|
| RNF-019 | O sistema deve estar em conformidade com a LGPD (Lei 13.709/2018) no que se refere a controle de acesso segmentado, registro de operações e armazenamento seguro de dados sensíveis |
| RNF-020 | O código-fonte é distribuído sob GNU General Public License (GPL) |
| RNF-021 | O sistema deve estar em conformidade com a Lei FELCA (Lei 15.211/2025) no que se refere à proteção digital de dados de crianças |

### 5.7 Backup e Recuperação

| Requisito | Descrição |
|-----------|-----------|
| RNF-022 | Rotina de backup automático com periodicidade mínima diária |
| RNF-023 | Procedimento documentado de recuperação em caso de falha — a ser detalhado no documento de infraestrutura |

---

## 6. Restrições de Projeto

| Restrição | Descrição |
|-----------|-----------|
| RC-001 | O sistema opera exclusivamente online — não há suporte a modo offline |
| RC-002 | O CPF é campo obrigatório para inscrição — crianças nascidas no exterior devem regularizar o CPF previamente nos Correios |
| RC-003 | A data de corte etário é 31 de março do ano letivo — não configurável por unidade |
| RC-004 | Nenhuma inscrição pode ser excluída do sistema |
| RC-005 | Critérios de priorização de vagas e convocação estão fora do escopo do sistema |
| RC-006 | A gestão da fila de atendimento presencial é externa ao sistema |
| RC-007 | O stack tecnológico é Flask + PostgreSQL — não há suporte a outros bancos de dados na v1.0 |
| RC-008 | O sistema é restrito à rede municipal — não há suporte a múltiplos municípios na v1.0 |

---

## 7. Atributos do Sistema

### 7.1 Confiabilidade

O sistema utiliza constraints de banco de dados (PKs, FKs, CHECKs, UNIQUEs) para garantir integridade dos dados independentemente da camada de aplicação. As regras críticas de negócio — unicidade de inscrição por CPF por período, compatibilidade de faixa etária, vínculo responsável-criança — são enforçadas no banco.

### 7.2 Rastreabilidade

Toda operação no sistema — criação, leitura de dados sensíveis, atualização — gera um registro imutável em `audit_log`. Alterações em campos específicos registram o valor anterior e o valor novo em JSONB. Isso garante suporte a processos administrativos e jurídicos e conformidade com a LGPD.

### 7.3 Integridade de Dados

| Mecanismo | Garantia |
|-----------|----------|
| `UNIQUE (crianca_id, periodo_id)` | Uma inscrição por CPF por período |
| `UNIQUE (ano_letivo)` em `periodos_inscricao` | Um período por ano letivo |
| FK composta em `inscricoes` → `responsaveis_criancas` | Inscrição só para vínculo responsável-criança existente |
| FK composta em `inscricoes` → `unidade_turma` | Inscrição só em combinação válida unidade+turma+período |
| `CHECK (data_encerramento > data_inicio)` | Período com datas coerentes |
| `CHECK (vagas > 0)` | Turmas com vagas positivas |
| `CHECK (cpf ~ '^\d{11}$')` | CPF com 11 dígitos numéricos |
| `RULE` em `audit_log` | Log imutável |

### 7.4 Neutralidade Jurídica

O sistema coleta dados socioeconômicos e de saúde de forma neutra, sem aplicar critérios de priorização de vagas. A definição de critérios e a condução do processo de oferta de vagas são responsabilidade externa da Secretaria Municipal de Educação. Essa delimitação é intencional e protege o sistema de contestações jurídicas.

---

## 8. Apêndices

### Apêndice A — Matriz de Permissões

| Ação | Administrador | Secretário de Educação | Diretor | Secretário Escolar |
|------|:---:|:---:|:---:|:---:|
| Configurar o sistema | ✓ | — | — | — |
| Cadastrar unidades escolares | — | ✓ | — | — |
| Cadastrar Diretores | — | ✓ | — | — |
| Cadastrar Secretários Escolares | — | ✓ | — | — |
| Definir períodos de inscrição | ✓ | — | — | — |
| Cadastrar e configurar turmas | — | — | ✓ | ✓ |
| Registrar inscrições | — | — | ✓ | ✓ |
| Editar inscrições (período aberto) | — | — | ✓ | ✓ |
| Visualizar inscrições | Todas | Todas | Própria unidade | Própria unidade |
| Reemitir comprovantes | — | Todas | Própria unidade | Própria unidade |
| Gerar relatórios | ✓ | ✓ (todas) | ✓ (própria) | ✓ (própria) |
| Exportar CSV oficial | ✓ | ✓ | — | — |

### Apêndice B — Definições de Turma (Seed)

| ID | Tipo | Faixa Etária | Mín. (meses) | Máx. (meses) |
|----|------|--------------|:------------:|:------------:|
| 1 | Berçário I | 0 a 11 meses | 0 | 11 |
| 2 | Berçário II | 2 anos a 2 anos, 11 meses e 29 dias | 12 | 23 |
| 3 | Berçário III | 3 anos a 3 anos, 11 meses e 29 dias | 24 | 35 |
| 4 | 1º Período | 4 anos a 4 anos, 11 meses e 29 dias | 36 | 47 |
| 5 | 2º Período | 5 anos a 5 anos, 11 meses e 29 dias | 48 | 59 |

> A data de corte para cálculo de idade é **31 de março** do ano letivo. As faixas podem ser ajustadas pela Secretaria Municipal mediante atualização do seed na tabela `definicoes_turma`.

### Apêndice C — Fluxo Principal do Sistema

```
[Login] → [Identificar período aberto]
    ↓
[Informar CPF da criança]
    ↓
[Verificar duplicidade] → [Duplicidade encontrada: bloquear e exibir inscrição existente]
    ↓ (sem duplicidade)
[Cadastrar responsável]
    ↓
[Cadastrar criança + solicitação de vaga]
    ↓
[Cadastrar irmãos?] → [Sim: repetir cadastro de criança com dados do responsável]
    ↓ (não)
[Conferir resumo da inscrição]
    ↓
[Confirmar e registrar]
    ↓
[Gerar e entregar comprovante PDF]
```

### Apêndice D — Decisões Técnicas Registradas

| Decisão | Justificativa |
|---------|---------------|
| CPF como PK de `responsaveis` e `criancas` | CPF é identificador único nacional. Elimina necessidade de surrogate key e simplifica consultas. |
| PK composta em `responsaveis_criancas` | Garante unicidade do vínculo responsável-criança por constraint natural, sem surrogate key. |
| FK composta em `inscricoes` referenciando `responsaveis_criancas` | Garante que inscrição só pode ser feita para vínculo responsável-criança previamente registrado. |
| FK composta tripla em `inscricoes` referenciando `unidade_turma` | Garante que inscrição só ocorre em combinação válida de unidade, turma e período. |
| `vagas` em `unidade_turma` e não em `turmas` | Vagas variam por unidade e por ano letivo — pertencem à oferta, não à turma em abstrato. |
| `parentesco` em `responsaveis_criancas` e não em `responsaveis` | Parentesco é atributo do vínculo, não do responsável — um responsável pode ter parentescos diferentes com crianças diferentes. |
| `audit_log` sem FK para `usuario_id` | O log deve sobreviver à desativação do usuário. Integridade referencial sacrificada intencionalmente em favor da imutabilidade histórica. |
| `TIMESTAMPTZ` em campos de data/hora | Armazena fuso horário — essencial para auditoria em sistemas públicos. |
| `RULE` para imutabilidade do `audit_log` | Bloqueia `UPDATE` e `DELETE` no banco, independentemente do usuário de aplicação utilizado. |
| `DEFAULT NOW()` em `criado_em` e `ocorrido_em` | Timestamp gerado pelo banco, não pela aplicação — evita manipulação. |
| Critérios de priorização fora do escopo | Evita risco jurídico. A Secretaria Municipal define critérios externamente ao sistema. |
| Sistema exclusivamente online | Garante visibilidade em tempo real pela Secretaria. |

---

*Documento gerado a partir do PRD v2.0, modelagem de dados DBML v3 e DDL PostgreSQL v1.0.*  
*Próximos artefatos previstos: Arc42 (arquitetura), Manual de Implantação, documento de infraestrutura e SLA.*
