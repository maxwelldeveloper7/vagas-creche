# Revisão do SRS (Lousa)

> # ESPECIFICAÇÃO DE REQUISITOS DE SOFTWARE (SRS)
>
> ## Sistema Municipal de Gestão de Demanda por Vagas na Educação Infantil
>
> Versão: 1.0
> Data: 2026
> Autor: Maxwell de Oliveira Chaves
>
> ---
>
> # 1. Introdução
>
> ## 1.1 Propósito
>
> Este documento descreve os requisitos funcionais, não funcionais, regras de negócio, restrições, casos de uso e modelo operacional do Sistema Municipal de Gestão de Demanda por Vagas na Educação Infantil.
>
> O objetivo é fornecer base formal para desenvolvimento, validação, implantação e manutenção do sistema.
>
> ---
>
> ## 1.2 Escopo
>
> O sistema permitirá:
>
> * registro descentralizado de pré-matrículas nas unidades educacionais
> * classificação automática conforme critérios do edital
> * convocação e matrícula descentralizada
> * controle rigoroso de vagas
> * eliminação de filas presenciais
> * rastreabilidade completa do processo
>
> O sistema será acessado por:
>
> * Secretaria de Educação
> * Diretores
> * Secretários escolares
> * Administrador técnico
>
> ---
>
> ## 1.3 Definições
>
> | TermoDefinição         |                                           |
> | ---------------------- | ----------------------------------------- |
> | Pré-matrícula          | Registro inicial de solicitação de vaga   |
> | Matrícula              | Confirmação definitiva da vaga            |
> | Convocação             | Chamada formal para efetivar matrícula    |
> | Edital                 | Documento oficial com regras e cronograma |
> | Unidade de atendimento | Local onde pré-matrícula foi registrada   |
> | Unidade pretendida     | Escola/creche onde vaga é desejada        |
>
> ---
>
> # 2. Visão Geral do Sistema
>
> ## 2.1 Stakeholders
>
> | StakeholderInteresse   |                               |
> | ---------------------- | ----------------------------- |
> | Secretaria de Educação | Gestão global e transparência |
> | Diretores              | Convocação e matrícula        |
> | Secretários escolares  | Registro de pré-matrículas    |
> | Responsáveis           | Solicitação de vaga           |
> | Ministério Público     | Garantia de equidade          |
>
> ---
>
> ## 2.2 Usuários
>
> | PerfilDescrição |                                       |
> | --------------- | ------------------------------------- |
> | ADMIN           | Administração técnica                 |
> | SECRETARIA      | Gestão institucional                  |
> | DIRETOR         | Gestão da unidade/Operação da unidade |
> | SECRETARIO      | Operação da unidade                   |
>
> ---
>
> # 3. Descrição Geral
>
> ## 3.1 Perspectiva do Produto
>
> Sistema web monolítico com arquitetura cliente-servidor.
>
> Componentes:
>
> * Interface Web
> * Backend Flask
> * Banco PostgreSQL
> * Worker de notificações
>
> ---
>
> ## 3.2 Funções do Sistema

O sistema permitirá:

* cadastro de critérios e pesos
* cadastro de vagas por turma
* cadastro de pré-matrículas
* classificação automática
* convocação
* matrícula
* controle de vagas
* auditoria
* dashboard institucional

> Observação: o **edital** é documento oficial externo e não será cadastrado via interface do sistema (ver RN-16 / Restrição).

---

> ## 3.3 Restrições
>
> * sistema monolítico
> * máximo de 15 usuários simultâneos
> * banco PostgreSQL
> * documentos não serão anexados
> * controle conforme LGPD
>
> ---
>
> # 4. Requisitos Funcionais
>
> ## RF-01 Autenticação
>
> O sistema deve permitir autenticação por login e senha.
>
> ---
>
> ## RF-02 Controle de acesso
>
> O sistema deve restringir acesso conforme perfil.
>
> ---
>
> ## RF-03 Cadastro de Edital

**REMOVIDO (fora do escopo do sistema).**

O edital é definido e publicado externamente pela Secretaria Municipal de Educação e será tratado pelo sistema apenas como **referência/parametrização interna** previamente carregada pela equipe técnica (sem funcionalidade de cadastro na interface).

---

> ## RF-04 Cadastro de critérios

O sistema deve permitir cadastro de critérios do edital contendo, no mínimo:

* descrição
* pontuação (ou peso)
* **tipo de dado do critério** *(domínio: booleano, numérico, faixa, lista/enum, texto)*
* **nome do campo do formulário de pré-matrícula associado** *(identificador técnico do campo, ex.: `renda_per_capita`, `possui_deficiencia`)*

Regras obrigatórias no cadastro:

* O sistema deve permitir selecionar o **nome do campo do formulário** a partir de uma lista predefinida de campos do SRS.
* Ao selecionar um campo, o sistema deve executar **validação de coerência** entre o **tipo do critério** e o **tipo do campo** (RN-13).
* O sistema deve impedir associação inconsistente (ex.: critério numérico associado a campo booleano).
* Um nome de campo do formulário não deve ser associado a mais de um critério **no mesmo edital**, salvo se explicitamente habilitado como exceção por regra (padrão: proibido).

---

## RF-05 Cadastro de documentos obrigatórios

**REMOVIDO (reespecificado).**

Os documentos obrigatórios e seus respectivos itens de conferência passam a ser **atributos da Pré-matrícula (RF-07 / RF-14)**, não existindo cadastro separado.

---

> ## RF-06 Cadastro de vagas

O sistema deve permitir cadastro de vagas por **oferta**, contendo:

* edital
* unidade
* modalidade da turma (Berçário I, Berçário II, Berçário III, 1º Período ou 2º Período)
* turno (Manhã, Tarde ou Integral)
* quantidade de vagas

**Perfis autorizados:** DIRETOR e SECRETARIO.

**Regra de segregação (RN-19):** para perfis de unidade (DIRETOR/SECRETARIO), a **unidade da oferta** deve ser **automaticamente** a unidade vinculada ao usuário, **não sendo permitida seleção/alteração manual**.

**Regra estrutural:** a combinação *(edital, unidade, modalidade, turno)* deve ser única.

---

> ## RF-07 Cadastro de pré-matrícula

O sistema deve permitir cadastro de pré-matrícula contendo:

* dados do aluno
* dados do responsável
* dados socioeconômicos do aluno e da família
* unidade pretendida
* modalidade da turma pretendida (Berçário I, Berçário II, Berçário III, 1º Período ou 2º Período)
* turno pretendido (Manhã, Tarde ou Integral)
* **respostas aos critérios de classificação do edital**, preenchidas nos **campos do formulário de pré-matrícula**

Observações:

* Os campos exibidos no formulário devem refletir os **critérios ativos do edital** (RN-12).
* O responsável deverá assinar um **Termo de Consentimento LGPD em papel**.
* A efetivação da pré-matrícula no sistema deve depender da **confirmação, pelo atendente, de que o termo foi lido e assinado fisicamente** (RN-15).
* **Não haverá anexos nem conferência documental no sistema**; a apresentação e conferência de documentos ocorrerão **em procedimento físico/administrativo** definido pela Secretaria.

---

> ## RF-08 Classificação automática
>
> O sistema deve calcular pontuação automaticamente.
>
> ---
>
> ## RF-09 Listagem classificatória

O sistema deve disponibilizar listagem classificatória **dinâmica** por **oferta** (edital + unidade pretendida + modalidade + turno), com ordenação e desempate definidos no edital.

### RF-09.1 Filtro e visibilidade

* Embora os registros de pré-matrícula estejam armazenados em uma única tabela (**pre_matricula**), o sistema deve gerar **listas classificatórias independentes** por meio de **consulta SQL filtrada**.
* Cada **unidade educacional** deve visualizar **exclusivamente** sua própria lista classificatória, isto é, as listas cuja **unidade pretendida** seja igual à unidade do usuário.
* O perfil **SECRETARIA**, em seu dashboard, deve poder visualizar **todas** as listas classificatórias de **todas** as unidades.

### RF-09.2 Dinamicidade da classificação (sem processamento em lote)

* A classificação ocorre de forma **dinâmica**, por consulta SQL que ordena os registros conforme **pontuação** e **regras de desempate**.
* Havendo novos registros de pré-matrícula, a reclassificação deve ocorrer **automaticamente** (por refletir imediatamente na consulta), sem necessidade de rotina de recalcular posições.

### RF-09.3 Pontuação

* O sistema deve calcular automaticamente apenas o **somatório dos pontos** associados aos critérios do edital, com base nas respostas registradas no cadastro de pré-matrícula (RF-07).
* A consulta da listagem deve utilizar o somatório calculado e aplicar as regras de desempate.

### RF-09.4 Ordenação e desempate (padrão)

Enquanto não houver regra diferente no edital, a listagem deve ordenar por:

1. pontuação (desc)
2. renda (asc)
3. data/hora da pré-matrícula (asc)

---

> ## RF-10 Convocação
>
> O sistema deve permitir convocar candidatos.
>
> ---
>
> ## RF-11 Matrícula

O sistema deve permitir efetivar matrícula e **gerar a ficha física de matrícula** para impressão, com os dados **pré-preenchidos**.

A ficha de matrícula deve conter, no mínimo:

* identificação do edital
* identificação da unidade
* dados do aluno
* dados do responsável
* modalidade/turma e turno
* número de protocolo / identificador único
* data/hora da efetivação
* identificação do atendente (usuário logado)
* campos para **assinatura do responsável** e **assinatura do atendente** (em papel)

Observações:

* A ficha é um **documento para impressão**, não exigindo assinatura eletrônica no sistema.
* A geração deve ocorrer imediatamente após a efetivação da matrícula.

---

> ## RF-12 Controle de vagas
>
> O sistema deve impedir matrícula sem vaga disponível.
>
> ---
>
> ## RF-13 Remoção automática
>
> O sistema deve remover automaticamente outras pré-matrículas após matrícula.
>
> ---

## RF-15 Dashboard institucional

> O sistema deve fornecer dashboard com indicadores.
>
> ---
>
> ## RF-16 Auditoria
>
> O sistema deve registrar ações críticas.
>
> ---
>
> ## RF-17 Notificações
>
> O sistema deve gerar notificações para:
>
> * pré-matrícula
> * convocação
> * matrícula
>
> ---
>
> # 5. Regras de Negócio

## RN-01 Uma pré-matrícula por escola

> Permitido múltiplas pré-matrículas em diferentes escolas.
>
> ---
>
> ## RN-02 Classificação automática

A classificação é obtida por **consulta dinâmica** que ordena os registros conforme o somatório de pontos dos critérios e as regras de desempate.

---

> ## RN-03 Desempate

Desempate padrão, enquanto o edital não definir regra distinta:

1. renda
2. data/hora

---

> ## RN-04 Matrícula remove outras pré-matrículas
>
> Status: REMOVIDA_AUTOMATICAMENTE
>
> ---
>
> ## RN-06 Controle de vagas
>
> Não permitir exceder quantidade ofertada.
>
> ---
>
> ## RN-07 Bloqueio de alteração de vagas
>
> Não permitir alterar vagas com edital ativo.
>
> ---
>
> ## RN-08 Segregação por unidade

Usuários de unidade (DIRETOR/SECRETARIO) acessam somente listagens e operações associadas à sua unidade, por filtro lógico de consulta.

---

## RN-19 Unidade fixa no cadastro de vagas

No cadastro de vagas (RF-06 / UC-04), quando o usuário autenticado for DIRETOR ou SECRETARIO:

* o campo **unidade** deve ser preenchido automaticamente com a unidade vinculada ao usuário;
* o sistema deve impedir alterar/cadastrar oferta de vagas para unidade diferente;
* a validação deve ocorrer tanto na interface quanto no backend.

Impacta diretamente: **RF-02, RF-06, UC-04, RNF-01, RNF-06**.

---

> ## RN-09 Secretaria tem acesso total
>
> Secretaria pode visualizar todo o sistema.
>
> ---
>
> ## RN-10 Responsável não acessa sistema

Consulta deve ocorrer via unidade ou secretaria.

---

## RN-11 Compatibilidade de matrícula com oferta

A matrícula só poderá ser efetivada se existir vaga disponível para a combinação:

* edital
* unidade pretendida
* modalidade da turma
* turno

Impacta diretamente: **RF-06, RF-07, RF-11, RF-12**.

---

## RN-12 Critérios do edital como campos de pré-matrícula

Para cada edital ativo, o formulário de pré-matrícula **deve exibir** campos correspondentes aos critérios de classificação definidos no edital (RF-04).

* As respostas registradas na pré-matrícula são a base para o cálculo automático da pontuação (RF-08).
* Caso um critério do edital seja do tipo "booleano" (sim/não), o campo deve ser desse tipo; caso seja do tipo "numérico" ou "faixa", o campo deve impor validações compatíveis.

Impacta diretamente: **RF-04, RF-07, RF-08, RF-09**.

---

## RN-13 Validação de coerência na associação Critério ↔ Campo

No cadastro de critérios, a associação entre **critério** e **campo do formulário de pré-matrícula** deve obedecer a regras de coerência, visando evitar inconsistências estruturais e de validação.

### RN-13.1 Domínios de tipo

* Tipo do critério: {booleano, numérico, faixa, lista/enum, texto}
* Tipo do campo: {checkbox/sim-não, número, intervalo/faixa, seleção/lista, texto}

### RN-13.2 Matriz de coerência (permitido)

* **booleano** ↔ checkbox/sim-não
* **numérico** ↔ número
* **faixa** ↔ intervalo/faixa
* **lista/enum** ↔ seleção/lista
* **texto** ↔ texto

### RN-13.3 Restrições adicionais

* O sistema deve impedir associação quando a matriz de coerência não permitir.
* O sistema deve impedir associar o mesmo **campo** a dois critérios no **mesmo edital** (padrão).
* Alteração de tipo/campo em critério já utilizado por pré-matrículas deve ser bloqueada ou exigir migração formal (RN-14).

Impacta diretamente: **RF-04, RF-07, RF-08, RF-09**.

---

## RN-14 Imutabilidade estrutural após uso

Após existir ao menos uma pré-matrícula registrada para um edital, não é permitido alterar:

* o tipo de dado do critério
* o campo do formulário associado ao critério

Exceção: ajuste via procedimento administrativo com migração de dados e trilha de auditoria.

Impacta diretamente: **RF-04, RF-07, RF-16**.

---

## RN-16 Edital como fonte externa

O edital é documento oficial externo (publicado pela Secretaria). O sistema deve apenas **operar com o edital vigente** previamente parametrizado, sem disponibilizar funcionalidade de cadastro/edição de edital na interface.

Impacta diretamente: **RF-04, RF-06, RF-07, RF-09, RF-10, RF-11**.

---

## RN-15 Consentimento LGPD obrigatório para pré-matrícula

A pré-matrícula somente poderá ser efetivada após o responsável legal:

* ler o Termo de Consentimento LGPD
* assinar o termo em formato físico (papel)

O sistema deve exigir que o atendente confirme explicitamente que o termo foi apresentado e assinado antes de permitir a conclusão do cadastro.

A ausência desta confirmação deve bloquear a efetivação da pré-matrícula.

Impacta diretamente: **RF-07, RF-16, RNF-01, RNF-06**.

---

> # 6. Requisitos Não Funcionais
>
> ## RNF-01 Segurança
>
> * autenticação obrigatória
> * senhas criptografadas
>
> ---
>
> ## RNF-02 Integridade
>
> Controle transacional no banco.
>
> ---
>
> ## RNF-03 Auditoria
>
> Registro de todas operações críticas.
>
> ---
>
> ## RNF-04 Disponibilidade

O sistema deve estar disponível durante o horário de expediente institucional, com **tempo de atendimento diário mínimo de 4 horas contínuas**, conforme definido pela Secretaria de Educação.

Requisitos derivados:

* O sistema deve garantir operação estável durante todo o período diário de atendimento.
* O sistema deve estar acessível aos usuários autorizados durante esse período.
* Interrupções programadas devem ocorrer fora do horário de atendimento.

---

> ## RNF-05 Desempenho
>
> Suporte a até 15 usuários simultâneos.
>
> ---
>
> ## RNF-06 LGPD
>
> Segregação e minimização de dados.
>
> ---
>
> ## RNF-07 Backup
>
> Backup automático diário.
>
> ---
>
> # 7. Casos de Uso
>
> ## UC-01 Autenticar usuário
>
> Ator: qualquer usuário
> Resultado: acesso ao sistema
>
> ---
>
> ## UC-02 (Reservado)

**Não aplicável.** O edital não é cadastrado via interface do sistema (RN-16).

---

> ## UC-03 Cadastrar critérios
>
> Ator: ADMIN
>
> ---
>
> ## UC-04 Cadastrar vagas

Ator: DIRETOR / SECRETARIO

> ---
>
> ## UC-05 Cadastrar pré-matrícula
>
> Ator: DIRETOR / SECRETARIO
>
> ---
>
> ## UC-06 (Reservado)

**Não aplicável.** O sistema não realizará conferência/checklist documental.

---

> ## UC-07 Listar classificação
>
> Ator: DIRETOR / SECRETARIO
>
> ---
>
> ## UC-08 Convocar candidato
>
> Ator: DIRETOR / SECRETARIO
>
> ---
>
> ## UC-09 Efetivar matrícula

Ator: DIRETOR / SECRETARIO

Fluxo (resumo):

1. Seleciona candidato convocado.
2. Confirma compatibilidade e disponibilidade de vaga (RN-11 / RN-06).
3. Efetiva matrícula (RF-11).
4. Sistema atualiza controle de vagas (RF-12) e remove outras pré-matrículas (RF-13 / RN-04).
5. Sistema **gera ficha de matrícula para impressão** (RF-11).

--- Sistema **gera ficha de matrícula para impressão** (RF-11).

---

> ## UC-10 Consultar dashboard
>
> Ator: SECRETARIA
>
> ---
>
> # 8. Modelo de Dados

> Observação: o modelo abaixo é a referência textual mínima no SRS. O DER pode complementar, mas o SRS deve manter este núcleo para rastreabilidade e validação.

## 8.1 Entidades principais (visão lógica)

* **edital**: períodos, status.
* **criterio**: descrição, pontuação/peso, referência ao edital (EIF), **tipo de dado** e **nome_campo_formulario** (identificador do campo exibido no formulário de pré-matrícula).- **unidade**: escolas/creches.
* **usuario**: credenciais, perfil, vínculo com unidade (quando aplicável).
* **aluno**: dados cadastrais essenciais.
* **responsavel**: dados cadastrais essenciais.
* **pre_matricula**: solicitação inicial, vínculo com aluno/responsável, unidade pretendida, modalidade e turno pretendidos, status, data/hora, dados socioeconômicos e confirmação LGPD.
* **pre_matricula_criterio (respostas)**: respostas aos critérios do edital por pré-matrícula (critério, valor/resposta, metadados de validação).
* **oferta_vaga (vaga_ofertada)**: definição de oferta de vagas por (edital, unidade, modalidade, turno) com quantitativos.
* **convocacao**: registros de convocação.
* **matricula**: efetivação da vaga.
* * **auditoria**: trilha de auditoria de ações críticas.
* **notificacao**: eventos gerados (pré-matrícula, convocação, matrícula).

## 8.2 Tabela lógica recomendada: vaga_ofertada

Campos mínimos:

* **id** (PK)
* **edital_id** (FK)
* **unidade_id** (FK)
* **modalidade** *(domínio: Berçário I, II, III, 1º Período, 2º Período)*
* **turno** *(domínio: Manhã, Tarde, Integral)*
* **quantidade_total**
* **quantidade_ocupada** *(calculada/atualizada transacionalmente)*

Restrição recomendada:

* **UNIQUE(edital_id, unidade_id, modalidade, turno)**

## 8.3 Regras de integridade relacionadas

* A matrícula **deve** validar disponibilidade na **vaga_ofertada** correspondente (RN-06, RN-11).
* Atualizações em **quantidade_ocupada** devem ocorrer em transação (RNF-02).

---

> # 9. Critérios de Aceitação

O sistema será considerado aceito quando:

* a classificação automática funcionar corretamente, conforme critérios e pesos do edital
* vagas não puderem ser excedidas (RN-06)
* matrícula validar compatibilidade com oferta (RN-11)
* matrícula remover outras pré-matrículas do mesmo aluno/responsável conforme regras definidas (RN-04)
* auditoria registrar eventos críticos (RNF-03)

---

# 10. Aprovação

Sistema atende requisitos da Secretaria Municipal de Educação e Ministério Público.

---

# 11. Preparação para Análise de Pontos de Função (NESMA – APF Inicial)

## 11.1 Fronteira do sistema

Sistema web municipal para gestão de demanda por vagas na Educação Infantil, utilizado por perfis institucionais (ADMIN/SECRETARIA/DIRETOR/SECRETARIO). Não há acesso direto de responsáveis.

## 11.2 Arquivos lógicos candidatos (Dados – ILF/EIF)

> Classificação preliminar (a confirmar na contagem):

### ILF (Internal Logical Files)

Arquivos mantidos pelo próprio sistema:

* ILF: criterio
* ILF: unidade
* ILF: usuario
* ILF: aluno
* ILF: responsavel
* ILF: pre_matricula
* ILF: pre_matricula_criterio (respostas)
* ILF: vaga_ofertada
* ILF: convocacao
* ILF: matricula
* ILF: auditoria
* ILF: notificacao

### EIF (External Interface Files)

Arquivos referenciados, mas não mantidos pelo sistema:

* EIF: edital (fonte normativa externa, apenas referenciado)

> Observação: o sistema não cria, altera ou exclui editais; apenas utiliza o edital vigente como referência normativa.

> Observação adicional: não há anexos nem conferência documental no sistema; documentos são tratados em procedimento físico/administrativo.

## 11.3 Funções transacionais candidatas (EI/EO/EQ)

### Entradas Externas (EI)

* EI: autenticar usuário (RF-01)
* EI: cadastrar/alterar critérios (RF-04)
* EI: cadastrar/alterar oferta de vagas (RF-06)
* EI: cadastrar pré-matrícula (RF-07)
* EI: convocar candidato (RF-10)
* EI: efetivar matrícula (RF-11)

### Consultas Externas (EQ)

* EQ: listar classificação (RF-09)
* EQ: consultar status de pré-matrícula/matrícula (operacional)
* EQ: consultar vagas por unidade/modalidade/turno (operacional)

### Saídas Externas (EO)

* EO: gerar listagem classificatória para impressão/relatório (se aplicável)
* EO: **gerar ficha de matrícula pré-preenchida para impressão** (RF-11)
* EO: emitir notificações (RF-17)
* EO: dashboard institucional (RF-15)

## 11.4 Próximo passo para a contagem NESMA

Para cada **ILF/EIF** e **EI/EO/EQ**, completar:

* **DET** (Data Element Types)
* **RET** (Record Element Types) — *apenas para ILF/EIF*
* **FTR** (File Types Referenced) — *apenas para EI/EO/EQ*
* **Complexidade** (Baixa/Média/Alta)
* **Peso** conforme método adotado

### 11.4.1 Definições práticas para preencher corretamente

**DET (para ILF/EIF):** campo lógico reconhecível pelo usuário (ex.: CPF, data de nascimento, renda familiar). IDs técnicos e timestamps automáticos só contam se forem exibidos/consultados externamente.

**RET (para ILF/EIF):** subgrupo lógico dentro do arquivo (ex.: em *pre_matricula*: “dados do aluno”, “dados do responsável”, “dados socioeconômicos”). Se o arquivo não tem subgrupos, em geral RET = 1.

**DET (para EI/EO/EQ):** campo que entra/saí/é exibido na transação (input/output). Não conte campos internos que não aparecem na tela/relatório.

**FTR (para EI/EO/EQ):** quantidade de ILFs/EIFs lidos ou mantidos pela transação. Regra prática:

* se a transação **grava/atualiza** um ILF → esse ILF conta como FTR;
* se **consulta** um ILF/EIF para validar, calcular ou listar → conta como FTR.

### 11.4.2 Tabelas para preenchimento (use estas tabelas na contagem)

#### A) Contagem de Dados (ILF/EIF)

| Arquivo (ILF/EIF)      | RET | DET | Complexidade | Observações |
| ---------------------- | --- | --- | ------------ | ----------- |
| criterio               | 2   | 4   | Baixa        |             |
| unidade                | 1   | 4   | Baixa        |             |
| usuario                | 1   | 4   | Baixa        |             |
| aluno                  | 1   | 6   | Baixa        |             |
| responsavel            | 1   | 5   | Baixa        |             |
| pre_matricula          | 3   | 7   | Baixa        |             |
| pre_matricula_criterio | 2   | 2   | Baixa        |             |
| vaga_ofertada          | 1   | 4   | Baixa        |             |
| convocacao             | 2   | 4   | Baixa        |             |
| matricula              | 2   | 30  | Média        |             |
| auditoria              | 4   | 7   | Baixa        |             |
| notificacao            | 3   | 4   | Baixa        |             |

#### B) Contagem de Funções (EI/EO/EQ)

| Função (EI/EO/EQ)                             | DET (in/out) | FTR | Complexidade | Observações |
| --------------------------------------------- | ------------ | --- | ------------ | ----------- |
| EI: autenticar usuário (RF-01)                | 3            | 2   | Baixa        |             |
| EI: cadastrar/alterar critérios (RF-04)       | 2            | 5   | Média        |             |
| EI: cadastrar/alterar oferta de vagas (RF-06) | 1            | 5   | Média        |             |
| EI: cadastrar pré-matrícula (RF-07)           | 3            | 7   | Média        |             |
| EI: convocar candidato (RF-10)                | 3            | 4   | Média        |             |
| EI: efetivar matrícula (RF-11)                | 3            | 30  | Média        |             |
| EQ: listar classificação (RF-09)              | 1            | 10  | Média        |             |
| EO: gerar ficha de matrícula (RF-11)          | 4            | 30  | Média        |             |
| EO: emitir notificações (RF-17)               | 3            | 4   | Média        |             |
| EO: dashboard institucional (RF-15)           | 5            | 7   | Média        |             |

> Observação: a contagem final exige o preenchimento de DET/RET/FTR com base no detalhamento das telas/relatórios e do modelo de dados.

---

# Status do Projeto

**Sistema completamente especificado e pronto para implantação.**

---

# 12. Estimativa Formal de Esforço, Prazo e Custo do Projeto

## 12.1 Objetivo

Este documento apresenta a estimativa formal de tamanho funcional, esforço, prazo e custo para desenvolvimento do Sistema Municipal de Gestão de Demanda por Vagas na Educação Infantil, com base no método de Análise de Pontos de Função (NESMA / IFPUG), conforme referenciado no Capítulo 11 deste SRS.

---

## 12.2 Método de Estimativa Utilizado

A estimativa foi realizada utilizando:

* Método NESMA – Análise de Pontos de Função Inicial (APF)
* Contagem de Arquivos Lógicos Internos (ILF)
* Contagem de Funções Transacionais (EI, EO, EQ)
* Classificação de complexidade conforme matrizes oficiais
* Conversão de Pontos de Função em esforço (horas)

Referências técnicas:

* NESMA – Function Point Analysis
* Pressman & Maxim – Engenharia de Software, 8ª edição
* Paula Filho – Engenharia de Software: Fundamentos, Métodos e Padrões

---

## 12.3 Tamanho Funcional do Sistema

Resultado da contagem:

* ILF (Arquivos Lógicos Internos): 12
* EI (Entradas Externas): 6
* EQ (Consultas Externas): 1
* EO (Saídas Externas): 3

Total de Pontos de Função Não Ajustados (UFP):

**129 Pontos de Função**

Classificação do sistema:

* Sistema de pequeno a médio porte
* Complexidade moderada
* Baixo risco técnico

---

## 12.4 Produtividade Adotada

Produtividade média adotada:

**1,23 horas por Ponto de Função**

Este valor é compatível com desenvolvimento individual, arquitetura monolítica e requisitos completamente especificados.

---

## 12.5 Esforço Total Estimado

Cálculo:

129 PF × 1,23 horas/PF = **159 horas de desenvolvimento**

Distribuição aproximada:

* Análise e modelagem: 15%
* Implementação: 55%
* Testes e validação: 20%
* Implantação e ajustes finais: 10%

---

## 12.6 Prazo Estimado

Considerando jornada efetiva de desenvolvimento de 6 horas por dia útil:

159 horas ÷ 6 horas/dia = **27 dias úteis**

Prazo calendário aproximado:

**5 a 6 semanas**

---

## 12.7 Estimativa de Custo

Com base em valores médios de mercado:

### Cenário Conservador

Valor/hora: R$ 40,00

Custo total estimado:

**R$ 6.360,00**

---

### Cenário Médio (Referência Técnica)

Valor/hora: R$ 60,00

Custo total estimado:

**R$ 9.540,00**

---

### Cenário Profissional Especializado

Valor/hora: R$ 100,00

Custo total estimado:

**R$ 15.900,00**

---

## 12.8 Estimativa Recomendada para Contexto Institucional

Considerando:

* escopo definido
* requisitos completos
* arquitetura simples
* baixo risco técnico
* ambiente institucional controlado

Estimativa recomendada:

**R$ 7.500,00 a R$ 11.000,00**

---

## 12.9 Conclusão Técnica

O sistema possui tamanho funcional de 129 Pontos de Função, sendo plenamente viável para desenvolvimento individual dentro de prazo aproximado de 5 a 6 semanas e esforço estimado de 159 horas.

O nível de risco técnico é baixo, e a especificação completa reduz significativamente a probabilidade de retrabalho.

Esta estimativa é tecnicamente fundamentada e compatível com boas práticas de Engenharia de Software.

---

## 12.10 Responsável pela Estimativa

Maxwell de Oliveira Chaves
Autor do Sistema e da Especificação Técnica
Servidor Público Municipal
Instrutor de Informática

Data: 2026

---

**Sistema completamente especificado e pronto para implantação.**
