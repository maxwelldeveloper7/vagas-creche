# PRD — Sistema de Inscrição em Creche
## Documento de Requisitos de Produto

**Versão:** 2.0  
**Licença:** GNU General Public License (GPL)  
**Última revisão:** 2026

---

## Sumário

1. [Visão Geral do Produto](#1-visão-geral-do-produto)
2. [Problema a Ser Resolvido](#2-problema-a-ser-resolvido)
3. [Usuários do Sistema](#3-usuários-do-sistema)
4. [Fluxo Principal do Sistema](#4-fluxo-principal-do-sistema)
5. [Funcionalidades do Sistema](#5-funcionalidades-do-sistema)
6. [Cadastro do Responsável](#6-cadastro-do-responsável)
7. [Cadastro da Criança](#7-cadastro-da-criança)
8. [Cadastro de Irmãos](#8-cadastro-de-irmãos)
9. [Conferência da Inscrição](#9-conferência-da-inscrição)
10. [Comprovante de Inscrição](#10-comprovante-de-inscrição)
11. [Consulta de Inscrições](#11-consulta-de-inscrições)
12. [Relatórios Administrativos](#12-relatórios-administrativos)
13. [Regras de Negócio Consolidadas](#13-regras-de-negócio-consolidadas)
14. [Requisitos Não Funcionais](#14-requisitos-não-funcionais)
15. [Auditoria e Registro de Operações](#15-auditoria-e-registro-de-operações)
16. [Regras Operacionais](#16-regras-operacionais)
17. [Decisões de Escopo](#17-decisões-de-escopo)

---

## 1. Visão Geral do Produto

### 1.1 Nome do Produto

**Sistema de Inscrição para Creche da Rede Municipal**

### 1.2 Propósito

Disponibilizar um sistema digital para **registro, controle e gerenciamento das inscrições de crianças em creches da rede municipal**, permitindo:

- cadastro padronizado das inscrições
- rastreabilidade administrativa das informações
- geração de comprovantes de inscrição
- consulta de inscrições realizadas por ano letivo
- geração de relatórios para planejamento educacional
- consolidação de dados para análise de demanda por vagas

O sistema funciona como **ferramenta institucional de apoio à gestão educacional**, garantindo transparência, organização administrativa e integridade das informações registradas.

> **Nota de escopo:** o sistema realiza o registro de pré-matrículas. Critérios de priorização e chamada de vagas são processos externos ao sistema, de responsabilidade da Secretaria Municipal de Educação. Essa delimitação é intencional e garante neutralidade jurídica do software.

### 1.3 Licença

O sistema é distribuído sob **GNU General Public License (GPL)**, garantindo que o código-fonte seja aberto, auditável e redistribuível conforme os termos da licença.

---

## 2. Problema a Ser Resolvido

O processo de inscrição pode apresentar:

- registros manuais ou dispersos entre unidades
- risco de duplicidade de inscrições para a mesma criança
- dificuldade de rastreamento e auditoria das informações
- ausência de padronização de dados entre unidades
- dificuldade de consolidar informações para planejamento de vagas
- falta de visibilidade centralizada pela Secretaria Municipal

O sistema proposto visa **centralizar, padronizar e registrar digitalmente o processo de inscrição**, garantindo maior confiabilidade, rastreabilidade e suporte à tomada de decisão administrativa.

---

## 3. Usuários do Sistema

O sistema possui quatro perfis distintos, com responsabilidades e permissões bem delimitadas.

> **Nomenclatura:** o termo "secretário" designa dois papéis completamente diferentes neste sistema. O **Secretário de Educação** é o gestor da rede municipal. O **Secretário Escolar** é o funcionário administrativo de uma unidade escolar, com perfil operacional equivalente ao Diretor.

---

### 3.1 Administrador

Responsável pela **configuração técnica do sistema** e cadastro inicial dos Secretários de Educação.

**Permissões:**
- configurar parâmetros do sistema
- cadastrar Secretários de Educação
- definir períodos de inscrição por ano letivo
- consultar todos os registros do sistema
- gerar relatórios administrativos globais

**Restrições:**
- não pode registrar, editar ou excluir inscrições

---

### 3.2 Secretário de Educação

Responsável pela **gestão da estrutura da rede municipal de educação** e pela supervisão administrativa das inscrições em todas as unidades.

**Permissões:**
- cadastrar unidades escolares
- cadastrar Diretores e vinculá-los às suas respectivas unidades
- cadastrar Secretários Escolares e vinculá-los às suas respectivas unidades
- **visualizar** inscrições e dados de **todas as unidades** da rede
- gerar relatórios administrativos de todas as unidades
- reemitir comprovantes de inscrição de qualquer unidade
- exportar CSV oficial ao encerramento do período

**Restrições:**
- não pode registrar, editar ou excluir inscrições
- não pode alterar dados de responsáveis ou crianças já registrados

---

### 3.3 Diretor

Responsável pelo **atendimento direto ao cidadão e registro das inscrições** na unidade à qual está vinculado.

**Permissões:**
- cadastrar e configurar turmas da própria unidade
- registrar inscrições na própria unidade
- cadastrar responsáveis e crianças durante o processo de inscrição
- editar registros de inscrições **durante o período oficial de inscrição**
- consultar inscrições da própria unidade
- reemitir comprovantes de inscrição da própria unidade

**Restrições:**
- acesso restrito à unidade à qual está vinculado
- não pode excluir inscrições
- não pode editar inscrições após o encerramento do período oficial

---

### 3.4 Secretário Escolar

Funcionário administrativo da unidade escolar. Possui as **mesmas permissões operacionais do Diretor**, sendo um segundo operador da mesma unidade. É cadastrado pelo Secretário de Educação e vinculado a uma única unidade.

**Permissões:** idênticas ao perfil Diretor — ver seção 3.3.

**Restrições:** idênticas ao perfil Diretor — ver seção 3.3.

> Cada unidade pode ter um Diretor e um Secretário Escolar, ambos com acesso operacional completo à própria unidade.

---

### 3.5 Matriz de Permissões

| Ação | Administrador | Secretário de Educação | Diretor | Secretário Escolar |
|---|:---:|:---:|:---:|:---:|
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

---

## 4. Fluxo Principal do Sistema

O fluxo operacional principal é organizado priorizando simplicidade e clareza para o operador:

1. autenticar usuário
2. gerenciar estrutura escolar (quando aplicável)
3. iniciar inscrição informando o CPF da criança
4. cadastrar responsável
5. cadastrar criança
6. cadastrar irmãos (se houver)
7. conferir dados da inscrição
8. editar informações se necessário
9. registrar inscrição
10. gerar e entregar comprovante
11. consultar inscrições
12. gerar relatórios administrativos

---

## 5. Funcionalidades do Sistema

### 5.1 Autenticação

O sistema permite login apenas de usuários previamente cadastrados e autorizados.

**Campos:**
- usuário (CPF ou e-mail institucional)
- senha

**Comportamento:**
- validar credenciais contra a base de usuários
- identificar perfil do usuário autenticado
- aplicar controle de acesso conforme o perfil
- redirecionar ao painel correspondente ao perfil
- registrar tentativas de login (com sucesso e falha) no log de auditoria
- bloquear conta após número configurável de tentativas inválidas consecutivas

**Recuperação de acesso:**
- o Diretor ou Secretário Escolar com acesso bloqueado ou senha esquecida deve acionar o Secretário de Educação vinculado à sua unidade para redefinição de credenciais
- o Secretário de Educação aciona o Administrador
- o processo de redefinição é registrado no log de auditoria

---

### 5.2 Gerenciamento da Estrutura Escolar

#### Cadastro de Unidades Escolares (Secretário de Educação)

**Campos:**
- nome da unidade
- endereço completo
- telefone
- diretor(es) vinculado(s)
- secretário(s) vinculado(s)
- status (ativa / inativa)

#### Cadastro de Turmas (Diretor)

Cada unidade deve ter turmas cadastradas antes do início do período de inscrição.

**Exemplos de turmas:**
- Berçário I
- Berçário II
- Berçário III
- 1º Período
- 2º Período

**Campos da turma:**
- unidade escolar
- nome da turma
- turno (manhã, tarde ou integral)
- faixa etária mínima (em meses ou anos completos em 31/03)
- faixa etária máxima (em meses ou anos completos em 31/03)
- número de vagas disponíveis
- ano letivo

---

### 5.3 Configuração do Período de Inscrição

O Administrador define os períodos oficiais de inscrição.

**Campos:**
- ano letivo
- data de início
- data de encerramento
- status (aberto / encerrado)

**Regras:**
- o período de inscrição ocorre uma vez por ano letivo
- a duração média é de 5 a 6 semanas
- fora do período, o sistema bloqueia o registro de novas inscrições
- após encerramento, inscrições existentes tornam-se imutáveis no sistema

---

### 5.4 Regra de Corte Etário

A elegibilidade da criança considera o **corte etário de 31 de março do ano letivo da inscrição**.

**Regra:** a idade considerada é a que a criança terá em 31 de março do ano letivo.

**Comportamento do sistema:**
- calcular automaticamente a idade na data de corte com base na data de nascimento
- determinar a faixa etária elegível
- sugerir a turma compatível com a faixa etária calculada
- bloquear seleção de turma incompatível com a idade calculada, exibindo mensagem explicativa

---

### 5.5 Início da Inscrição

O Diretor inicia uma inscrição informando o **CPF da criança**.

**Comportamento do sistema:**

1. verificar se já existe inscrição ativa associada ao CPF no ano letivo vigente
2. **se existir:** bloquear nova inscrição e exibir data, horário e unidade da inscrição já registrada
3. **se não existir:** prosseguir para o cadastro do responsável e da criança, pré-preenchendo o CPF no formulário da criança

> **Nota:** toda criança nascida no Brasil recebe CPF no momento do registro da certidão de nascimento. Para casos excepcionais (crianças nascidas no exterior ainda sem CPF regularizado), o responsável deve regularizar o CPF previamente em uma agência dos Correios. O CPF é campo obrigatório para inscrição.

---

## 6. Cadastro do Responsável

### 6.1 Dados de Identificação

- nome completo
- CPF
- RG
- parentesco com a criança (mãe, pai, responsável legal, familiar, cuidador)
- telefone de contato

### 6.2 Endereço

- logradouro, número, complemento, bairro
- município e UF
- CEP
- ponto de referência
- comprovante de endereço (registro lógico — o documento físico permanece arquivado na unidade)

### 6.3 Situação Socioeconômica

Estas informações são coletadas para fins de planejamento e análise de políticas públicas. A definição dos critérios de priorização de vagas é responsabilidade da Secretaria Municipal, fora do escopo deste sistema.

- mãe com vínculo empregatício
- comprovante de endereço do trabalho
- demonstrativo de crédito ou benefício
- LOAS / BPC / seguro-desemprego
- trabalhador(a) autônomo(a)
- mãe matriculada em rede pública de ensino
- situação de vulnerabilidade social
- declaração escolar de mãe adolescente
- renda per capita familiar

---

## 7. Cadastro da Criança

### 7.1 Identificação

- nome completo
- data de nascimento
- CPF (obrigatório — pré-preenchido a partir do início da inscrição)
- nome do pai
- nome da mãe

### 7.2 Solicitação de Vaga

- unidade escolar pretendida (o responsável pode escolher livremente qualquer unidade da rede)
- turma pretendida (sugerida automaticamente pelo sistema com base no corte etário; seleção de turma incompatível é bloqueada)

### 7.3 Situação Documental

- certidão em que não conste pai ou mãe
- irmão(ã) matriculado(a) em unidade escolar da rede municipal

### 7.4 Encaminhamentos Institucionais

- Vara da Família
- Conselho Tutelar
- CRAS
- CREAS
- Casa de acolhimento

### 7.5 Dados Sociais e de Saúde

- NIS (Número de Identificação Social)
- número do cartão SUS
- laudo de deficiência ou neoplasia
- laudo de intolerância alimentar
- laudo de neurodivergência

> Essas informações auxiliam no planejamento de políticas de inclusão e priorização social pela Secretaria Municipal.

---

## 8. Cadastro de Irmãos

Após concluir o cadastro de uma criança, o sistema pergunta:

> **Deseja cadastrar outra criança para este responsável?**

Se positivo:
- abre novo formulário de criança
- reutiliza automaticamente os dados do responsável já cadastrado
- pergunta: **é filho(a) do mesmo relacionamento?**
- se sim, preenche automaticamente nome do pai e nome da mãe

Todos os campos permanecem editáveis.

---

## 9. Conferência da Inscrição

Antes de salvar, o sistema exibe um **resumo completo das informações registradas**.

**Informações exibidas:**
- dados do responsável
- dados da criança
- situação socioeconômica informada
- documentos informados
- encaminhamentos institucionais informados
- dados sociais e de saúde informados
- unidade pretendida
- turma pretendida

> Campos lógicos (checkboxes, flags) aparecem no resumo **apenas quando marcados como verdadeiros**, evitando poluição visual.

O Diretor pode voltar a qualquer seção para corrigir informações antes de confirmar o registro.

---

## 10. Comprovante de Inscrição

Após registrar a inscrição, o sistema gera automaticamente um comprovante.

### 10.1 Conteúdo

**Identificação da inscrição:**
- número da inscrição
- data e hora do registro
- unidade onde foi realizada a inscrição
- ano letivo

**Dados da criança:**
- nome completo
- CPF
- data de nascimento
- nome do pai
- nome da mãe

**Dados do responsável:**
- nome completo
- CPF
- telefone
- endereço

**Solicitação:**
- unidade escolar pretendida
- turma pretendida

### 10.2 Formato

O comprovante pode ser:
- impresso diretamente na unidade
- gerado em PDF para download ou reimpressão

### 10.3 Segurança do PDF

O arquivo PDF é gerado com proteção de abertura por senha baseada no CPF da criança (apenas dígitos, sem formatação). Essa proteção serve para **controle de distribuição e rastreabilidade**, não como mecanismo de segurança de dados sensíveis — os dados pessoais são protegidos pelo controle de acesso ao sistema, conforme os requisitos de segurança da seção 14.

---

## 11. Consulta de Inscrições

### 11.1 Critérios de Busca

- nome da criança
- CPF da criança
- número da inscrição
- **ano letivo** (filtro obrigatório, padrão: ano letivo vigente)
- unidade escolar (disponível apenas para Secretário Municipal e Administrador)

### 11.2 Permissões de Acesso

- **Diretor / Secretário Escolar:** consulta apenas inscrições da própria unidade
- **Secretário de Educação:** consulta inscrições de todas as unidades
- **Administrador:** consulta todas as inscrições

### 11.3 Funcionalidades

- visualizar dados completos da inscrição selecionada
- reemitir comprovante de inscrição

---

## 12. Relatórios Administrativos

### 12.1 Tipos de Relatórios

**Lista geral de inscritos:**
- número da inscrição, nome da criança, unidade pretendida, turma pretendida, data da inscrição

**Inscrições por unidade escolar:**
análise de demanda por escola, útil para planejamento de abertura de turmas

**Inscrições por turma pretendida ou faixa etária:**
subsidia o planejamento da oferta de vagas

**Relatórios por critérios sociais:**
- renda per capita
- situação de vulnerabilidade social
- benefícios sociais declarados
- encaminhamentos institucionais registrados

### 12.2 Filtros

Todos os relatórios devem permitir filtragem por **ano letivo** e, quando aplicável, por unidade escolar.

### 12.3 Exportação

- todos os relatórios podem ser exportados em **CSV**
- após o encerramento do período de inscrição, o sistema disponibiliza a geração do **arquivo CSV oficial** contendo todos os registros do período, para fins de planejamento e arquivo institucional

---

## 13. Regras de Negócio Consolidadas

1. o CPF da criança é o identificador único de inscrição no sistema
2. não pode existir mais de uma inscrição por CPF no mesmo ano letivo
3. o CPF é campo obrigatório para inscrição
4. a idade da criança é calculada com base no corte etário de **31 de março** do ano letivo
5. o sistema sugere a turma compatível e bloqueia seleções incompatíveis com a faixa etária
6. campos lógicos são exibidos no resumo apenas quando verdadeiros
7. Diretores e Secretários Escolares acessam apenas dados da própria unidade
8. o Secretário de Educação visualiza dados de todas as unidades, sem permissão de edição
9. nenhuma inscrição pode ser excluída
10. após o encerramento do período de inscrição, nenhuma inscrição pode ser editada no sistema
11. comprovantes devem ser gerados em PDF com proteção por senha
12. registros ficam associados ao ano letivo e devem ser consultáveis por filtro de ano

---

## 14. Requisitos Não Funcionais

### Segurança

- autenticação obrigatória para todas as funcionalidades
- controle de acesso por perfil (RBAC)
- bloqueio de conta após tentativas inválidas consecutivas configuráveis
- criptografia de comprovantes em PDF
- transmissão de dados por HTTPS
- proteção de dados pessoais conforme LGPD

### Disponibilidade e Conectividade

- o sistema opera em modo **online**, com acesso via rede local ou internet
- em caso de indisponibilidade, o sistema deve exibir mensagem clara ao operador informando a falha de conexão
- formulários em andamento não devem ser perdidos em caso de queda de conexão momentânea — o sistema deve alertar o operador antes de qualquer perda de dados

### Usabilidade

- formulários simples e objetivos, adequados a operadores sem perfil técnico avançado
- preenchimento automático sempre que possível (CPF pré-preenchido, turma sugerida, dados do responsável reutilizados para irmãos)
- mensagens de erro claras e orientadas à ação

### Integridade de Dados

- validação de CPF (dígitos verificadores)
- prevenção de duplicidade por CPF no mesmo ano letivo
- validação de faixa etária conforme corte de 31 de março
- campos obrigatórios validados antes do registro

### Proteção de Dados (LGPD)

- controle de acesso segmentado por perfil e unidade
- registro de todos os acessos e operações (log de auditoria)
- armazenamento seguro de informações sensíveis (dados de saúde, situação social)
- rastreabilidade de todas as alterações (campo, valor anterior, valor novo)

### Backup e Recuperação

- rotina de backup automático dos dados com periodicidade mínima diária
- procedimento documentado de recuperação em caso de falha
- ambiente de homologação disponível para treinamento de operadores antes da implantação em produção

---

## 15. Auditoria e Registro de Operações

Todas as operações do sistema geram registros imutáveis de auditoria.

### 15.1 Operações Registradas

- **C** — criação de registros (inscrições, usuários, turmas, unidades)
- **R** — leitura de dados sensíveis (visualização de inscrições, reemissão de comprovantes)
- **U** — atualização de registros

Não haverá operação de exclusão de inscrições.

### 15.2 Informações Registradas por Evento

Cada evento de auditoria deve conter:

- identificador do usuário autenticado
- perfil do usuário
- operação realizada (C / R / U)
- entidade afetada (inscrição, turma, usuário, etc.)
- identificador do registro afetado
- data e hora (com fuso horário)
- unidade escolar vinculada ao usuário
- endereço IP ou identificador do dispositivo

### 15.3 Registro de Alterações (diff)

Para operações de edição (U), registrar adicionalmente:

- campo alterado
- valor anterior
- valor novo

### 15.4 Finalidade

Os registros de auditoria garantem:

- transparência administrativa
- rastreamento de responsabilidades
- suporte a processos administrativos ou jurídicos
- conformidade com a LGPD

Os registros de auditoria são **imutáveis e protegidos contra alteração manual**, inclusive por administradores do sistema.

---

## 16. Regras Operacionais

- a rede possui **14 unidades escolares**
- o volume anual de inscrições costuma ficar **abaixo de 400 crianças**
- o atendimento é **presencial nas unidades escolares**
- o atendimento ocorre por **ordem de chegada com distribuição de senha física** (gestão da fila é feita fora do sistema)
- o responsável pode escolher livremente qualquer unidade da rede como unidade pretendida
- o sistema registra **pré-matrículas**, utilizadas para organização da demanda — não são matrículas definitivas
- algumas documentações são apenas conferidas na unidade, podendo permanecer arquivadas fisicamente
- o cadastro pode ser realizado por responsável legal, familiar ou cuidador, mediante assinatura de **termo físico** na unidade

### Persistência de Registros

- nenhuma pré-matrícula poderá ser excluída do sistema
- todos os registros permanecem armazenados para auditoria e análise histórica
- registros são associados ao ano letivo e recuperáveis por filtro

### Bloqueio de Alterações

Após o encerramento do período oficial de inscrição:

- nenhuma inscrição poderá ser editada no sistema
- nenhuma informação de responsável ou criança poderá ser alterada

Correções posteriores ao encerramento do período ocorrem por **procedimento administrativo externo ao sistema**, sob responsabilidade da Secretaria de Educação.

### Exportação Oficial

Após o encerramento do período de inscrição, o sistema disponibiliza a geração do **arquivo CSV oficial** contendo todos os registros realizados no período, para uso pela Secretaria de Educação no planejamento de vagas.

---

## 17. Decisões de Escopo

Esta seção documenta decisões explícitas de escopo tomadas durante a especificação do produto, com o objetivo de preservar a intenção original do sistema e blindar futuras solicitações de expansão indevida de funcionalidades.

| Decisão | Justificativa |
|---|---|
| Critérios de priorização de vagas estão **fora do escopo** | Evita risco jurídico. A definição de critérios é responsabilidade da Secretaria Municipal. O sistema coleta dados neutros. |
| Convocação e chamada de vagas estão **fora do escopo** | O sistema encerra seu papel no registro da pré-matrícula. O processo de oferta de vagas é conduzido externamente. |
| Gestão de fila de atendimento presencial está **fora do escopo** | A distribuição de senhas é feita fisicamente nas unidades. O sistema não gerencia filas. |
| O sistema opera exclusivamente **online** | Garante visibilidade em tempo real pela Secretaria Municipal. Risco de indisponibilidade pontual por falha de conexão é aceito e mitigado por mensagens de erro claras ao operador. |
| CPF é campo **obrigatório** para inscrição | Toda criança nascida no Brasil recebe CPF na certidão de nascimento. Casos excepcionais (nascimento no exterior) devem ser regularizados previamente nos Correios. |

---

*Documento gerado a partir da versão 1.0, revisado com base em análise de requisitos e esclarecimentos dos stakeholders.*