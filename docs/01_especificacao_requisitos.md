# Levantamento de requisitos
## Etapa 1 — Contexto e Objetivo do Sistema

O sistema terá como finalidade **mapear e gerenciar a demanda por vagas em creches e educação infantil**, envolvendo:
* **Instituições participantes**
  * Creches públicas municipais
  * Creches privadas conveniadas à prefeitura

* **Faixas etárias / modalidades**
  * Berçário I: 6 meses a 1 ano
  * Berçário II: 2 anos a 2 anos, 11 meses e 29 dias
  * Berçário III: 3 anos a 3 anos, 11 meses e 29 dias
  * Educação Infantil:
    * 1º período: 4 anos a 4 anos, 11 meses e 29 dias
    * 2º período: 5 anos a 5 anos, 11 meses e 29 dias

* **Perfis de usuários**
  * Secretaria Municipal de Educação (acesso total aos dados, cadastram instituições e diretores)
  * Diretores das instituições (cadastram turmas e previsão de vagas; alocam crianças)
  * Responsáveis legais (realizam a inscrição da criança)

* **Fluxo macro**
  1. Diretores cadastram instituições, turmas e previsão de vagas para o ano seguinte
  2. Responsáveis realizam inscrições online das crianças
  3. Encerrado o período de inscrição, diretores acessam a lista de espera
  4. Diretores alocam crianças nas vagas disponíveis
  5. Sistema gera documento de matrícula (para impressão)
  6. Sistema envia notificação ao responsável com orientações para comparecimento

* **Volume estimado**
  * Entre 1.000 e 1.500 crianças por ciclo de inscrição


## Etapa 2 — Cadastro da Criança

### Dados obrigatórios
* Nome completo
* Data de nascimento
* Sexo
* CPF
* Cartão SUS
* NIS (opcional)

### Regras automáticas
* Cálculo automático da faixa etária com base na data de nascimento
* Bloqueio de inscrição em modalidade incompatível com a idade

### Situação educacional
* Situação atual da criança:
  * Em casa
  * Em outra escola
  * Transferência
* Não será registrado histórico escolar anterior

### Necessidades específicas e prioridade
* Indicação de:
  * Deficiência ou necessidades educacionais especiais
  * Existência de laudo (sem upload)
  * Prioridade legal (ex.: deficiência, vulnerabilidade social)

### Documentação
* Inscrição realizada apenas por preenchimento de dados
* Conferência e autenticação documental ocorrerão presencialmente, no ato da matrícula


## Etapa 3 — Cadastro dos Responsáveis

### Estrutura de responsáveis
* Permitido cadastrar **mais de dois responsáveis** por criança
* Abrange responsável legal, pais, avós, tutores, entre outros

### Dados obrigatórios do responsável
* Nome completo
* CPF
* RG
* Data de nascimento
* Grau de parentesco
* Endereço completo
* Telefone
* E-mail

### Comunicação
* **Não haverá responsável principal**
* Todos os responsáveis cadastrados receberão comunicações do sistema

### Autenticação e segurança
* Criação de login e senha obrigatória
* Acesso via **CPF + senha**
* Verificação adicional por **código de confirmação** (e-mail e/ou SMS)

### Canais de notificação
* E-mail
* SMS
* WhatsApp


## Etapa 4 — Instituições, Turmas e Vagas

### Cadastro da instituição
Campos obrigatórios:
* Nome da instituição
* INEP
* Tipo:
  * Pública municipal
  * Privada conveniada
* Endereço completo
* Telefone
* E-mail institucional

### Gestão de cadastro da instituição
* As instituições e seus usuários serão cadastrados pela Secretaria de Educação

### Gestão de usuários da instituição
* Cada instituição terá **apenas um diretor responsável e/ou uma secretária**
* Será permitido um usuário com perfil de direção/gestão e outro com perfil de secretaria

### Cadastro de turmas
Para cada turma:
* Modalidade:
  * Berçário I, II, III
  * Educação Infantil – 1º ou 2º período
* Turno:
  * Manhã
  * Tarde
  * Integral
* Quantidade total de vagas
* Ano letivo de referência

### Regras de vagas
* A previsão de vagas **só poderá ser alterada** após o cadastro inicial mediante **solicitação por email ao suporte técnico** justificando o motivo da alteração, e o suporte fará a alteração.
* Edição **bloqueada automaticamente** após o início do período de inscrições

### Alocação de crianças
* O sistema **não realizará alocação automática**
* O sistema **ordenará a lista de espera** com base em:
  * Pontuação por prioridade
  * Regras definidas e parametrizadas pela Secretaria de Educação
* Diretores visualizam a lista ordenada e realizam a alocação


## Etapa 5 — Fluxo de Inscrição, Pontuação e Lista de Espera

### Período de inscrições
* Haverá **um único período anual** de inscrições
* Datas de início e término:
  * Definidas pela Secretaria de Educação
  * Formalizadas por **edital de chamamento**

### Escolha de instituições
* O responsável poderá escolher **duas instituições**
  * 1ª opção: principal
  * 2ª opção: alternativa

### Regras de pontuação
* Critérios de prioridade:
  * **Fixos por ano letivo**
  * Não editáveis após publicação
  * Cumulativos (somatório de pontos)
* Parametrização realizada exclusivamente pela Secretaria de Educação

### Lista de espera
* Lista **única por instituição e modalidade**
* Turno **não influencia a ordenação**
  * Definição do turno ocorre no ato da matrícula, conforme disponibilidade e preferência do responsável

### Atualizações e auditoria
* Ao ser alocada, a criança:
  * É removida automaticamente das demais listas
* O sistema manterá:
  * **Histórico completo (log)** de todas as movimentações


## Etapa 6 — Matrícula, Documentos e Notificações

### Documento de matrícula
* Será gerado **um modelo único para toda a rede**
* Documento no formato de **ficha de matrícula**
* Campos pré-preenchidos pelo sistema:
  * Nome da criança
  * Data de nascimento
  * Naturalidade
  * Nacionalidade
  * Estado
  * Cor/Raça
  * NIS
  * Cartão SUS
  * Modalidade e período:
    * Creche:
      * Berçário I, II ou III
      * Indicação de atendimento parcial
    * Pré-escola:
      * 1º período (4 anos)
      * 2º período (5 anos)
  * Dados do(s) responsável(is)
  * Dados do local de trabalho dos responsáveis (quando existentes)

* Campos não coletados pelo sistema permanecerão **em branco**, para preenchimento manual na instituição

### Prazo para matrícula
* O sistema controlará **prazo máximo para comparecimento**
* Prazo:
  * **Configurável pela Secretaria de Educação**
  * Não fixo

### Perda e gestão da vaga
* A vaga **não será liberada automaticamente**
* O sistema:
  * Sinalizará a próxima criança da lista de espera
  * Manterá controle manual pela instituição/secretaria

### Notificações aos responsáveis
* Momentos de notificação:
  * Alocação da vaga
  * Lembrete de prazo
  * Perda da vaga
* Canais:
  * E-mail
  * SMS
  * WhatsApp
    (utilizados conforme configuração institucional)

### Confirmação da matrícula
* A instituição deverá:
  * Confirmar no sistema a efetivação presencial da matrícula
* Essa confirmação:
  * **Encerra o processo da criança no sistema**


## Etapa 7 — Perfis de Usuário, Permissões e Auditoria

### Perfis de usuário
Perfis definidos e validados:
1. **Administrador do Sistema (TI / Prefeitura)**
   * Usuário inserido manualmente
   * Não visível para os demais perfis
   * Acesso técnico e administrativo total

2. **Secretaria Municipal de Educação**
   * Perfil institucional de gestão normativa

3. **Diretor de Instituição**
   * Perfil operacional restrito à própria unidade

4. **Responsável Legal**
   * Perfil cidadão para inscrição e acompanhamento

---

### Permissões por perfil

#### Secretaria Municipal de Educação
* Cadastrar Instituições, Diretores e/ou Secretários: **Sim**
* Visualizar todos os cadastros: **Sim**
* Editar dados de crianças e responsáveis: **Não**
* Alterar status de inscrições e alocações: **Não**
* Gerenciar critérios e pontuações:
  * **Sim**, exclusivamente na fase de criação do edital
  * **Bloqueado** após o início das inscrições e do processo de matrícula

#### Diretor e Secretário de Instituição
* Visualizar apenas dados da própria instituição: **Sim**
* Alocar crianças nas vagas: **Sim**
* Confirmar matrícula presencial: **Sim**
* Editar dados cadastrais da criança ou responsáveis: **Não**

#### Responsável Legal
* Editar dados após a inscrição: **Sim**
* Acompanhar posição na lista de espera:

  * **Sim**, apenas sua própria posição
  * Sem acesso a dados de outros inscritos
* Cancelar inscrição: **Sim**

---

### Auditoria e rastreabilidade
O sistema deverá manter **registro completo (logs)** de:
* Acessos ao sistema
* Alterações de dados
* Alocações e cancelamentos
* Emissão de documentos

Esses registros garantem:
* Transparência administrativa
* Rastreabilidade de decisões
* Conformidade com princípios de controle público
