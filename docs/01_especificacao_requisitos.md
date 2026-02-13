# LEVANTAMENTO DE REQUISITOS

## Sistema Municipal de Gestão de Demanda por Vagas na Educação Infantil

---

# ETAPA 1 — CONTEXTO, FINALIDADE E GOVERNANÇA

## 1.1 Finalidade

O sistema terá como objetivo:

* Mapear e gerenciar a demanda por vagas em creches e pré-escolas;
* Aplicar automaticamente os critérios de prioridade definidos no edital anual;
* Gerar lista de espera unificada e auditável;
* Controlar alocação, matrícula e histórico de movimentações;
* Garantir transparência, rastreabilidade e conformidade administrativa.

O sistema substituirá planilhas e cadastros manuais, mantendo base única municipal.

---

## 1.2 Abrangência Institucional

### Instituições participantes

* Creches públicas municipais
* Escolas municipais com pré-escola
* Creches privadas conveniadas (quando previsto em edital)

Todas vinculadas à Secretaria Municipal de Educação.

---

## 1.3 Modalidades e Faixas Etárias

As faixas etárias serão **parametrizáveis por ciclo letivo**, conforme edital vigente.

Exemplo base (ajustável anualmente):

* Berçário I
* Berçário II
* Berçário III
* 1º Período
* 2º Período

O sistema calculará automaticamente a faixa etária com base:

* Na data de nascimento
* No corte etário definido para o ano letivo

Não haverá parametrização fixa no código.

---

## 1.4 Perfis de Usuário

### 1. Administrador do Sistema (TI)

* Acesso técnico total
* Gestão estrutural do sistema

### 2. Secretaria Municipal de Educação

* Cadastro de instituições
* Cadastro de diretores/secretários
* Parametrização anual:

  * Critérios de prioridade
  * Pesos
  * Calendário
  * Modalidades
  * Faixas etárias
* Visualização global
* Alterações extraordinárias com justificativa obrigatória e registro em log especial

### 3. Diretor / Secretário de Instituição

* Acesso restrito à própria unidade
* Cadastro presencial das crianças
* Cadastro de turmas e previsão de vagas
* Alocação de vagas
* Confirmação de matrícula

---

## 1.5 Autenticação

* Apenas usuários institucionais realizarão login.
* Responsáveis **não possuirão login ou acesso ao sistema**.
* A autenticação será realizada por:

  * CPF institucional + senha
  * Verificação adicional (quando aplicável)

---

# ETAPA 2 — ESTRUTURA DO CICLO LETIVO

O sistema trabalhará por **Ciclo Letivo Anual**.

Cada ciclo conterá:

* Critérios e pesos
* Período de inscrição
* Período de matrícula
* Modalidades ativas
* Vagas por unidade

Encerrado o ciclo:

* Dados permanecem arquivados
* Novo ciclo é criado
* Não há sobreposição de regras

---

# ETAPA 3 — CADASTRO DA CRIANÇA (INSCRIÇÃO)

## 3.1 Forma de Inscrição

* Inscrição exclusivamente presencial na instituição.
* Registro realizado pelo diretor ou servidor designado.
* Não haverá upload de documentos nesta etapa.
* Conferência documental ocorrerá apenas na matrícula.

---

## 3.2 Dados Obrigatórios da Criança

* Nome completo
* Data de nascimento
* Sexo
* CPF
* Cartão SUS
* NIS (quando houver)
* Situação educacional atual

---

## 3.3 Regras Automáticas

* Cálculo automático da faixa etária
* Bloqueio de modalidade incompatível
* Validação de duplicidade municipal (CPF + Data de Nascimento)

Caso haja duplicidade:

* Sistema alerta
* Não permite novo cadastro sem justificativa formal registrada

---

## 3.4 Critérios de Prioridade

* Parametrizados anualmente pela Secretaria
* Fixos após publicação do edital
* Cumulativos
* Pontuação automática
* Não editáveis após início das inscrições

O sistema:

* Calcula pontuação automaticamente
* Ordena lista por pontuação (quando aplicável)

---

# ETAPA 4 — CADASTRO DOS RESPONSÁVEIS

## 4.1 Estrutura

* Permitido cadastrar múltiplos responsáveis
* Não haverá login para responsáveis
* Todos poderão receber comunicações

---

## 4.2 Dados Obrigatórios

* Nome completo
* CPF
* RG
* Data de nascimento
* Grau de parentesco
* Endereço completo
* Telefone
* E-mail (quando houver)

---

## 4.3 LGPD

* No momento da inscrição, será assinado em papel:

  * Termo de ciência e autorização de tratamento de dados
* O sistema registrará:

  * Campo “Termo LGPD assinado: Sim/Não”
* O documento físico permanecerá arquivado na instituição

---

# ETAPA 5 — INSTITUIÇÕES, TURMAS E VAGAS

## 5.1 Cadastro da Instituição

Realizado pela Secretaria.

Campos:

* Nome
* INEP
* Tipo
* Endereço
* Telefone
* E-mail

---

## 5.2 Gestão de Usuários

Cada instituição poderá ter:

* 1 Diretor
* 1 Secretário

Não será permitido número ilimitado de usuários.

---

## 5.3 Cadastro de Turmas

Para cada turma:

* Modalidade
* Ano letivo
* Turno:

  * Manhã
  * Tarde
  * Integral
* Quantidade de vagas

Alteração de vagas:

* Apenas antes da abertura das inscrições
* Após abertura: somente por solicitação formal à Secretaria
* Sistema bloqueia edição automática

---

# ETAPA 6 — LISTA DE ESPERA E ORDENAÇÃO

## 6.1 Lista

* Lista única por instituição e modalidade
* Ordenação automática:

  * Pontuação
  * Critérios parametrizados
  * Ordem definida em edital

---

## 6.2 Turno

O turno **não interfere na ordenação**.

No momento da alocação, o diretor deverá informar:

* Se a vaga será:

  * Integral
  * Parcial
  * Manhã
  * Tarde

---

## 6.3 Alocação

* Sistema sugere o próximo da lista
* Diretor confirma alocação
* Caso não siga a ordem:

  * Justificativa obrigatória
  * Registro em log especial

Ao ser alocada:

* A criança é removida das demais listas automaticamente

---

# ETAPA 7 — MATRÍCULA E VALIDAÇÃO DOCUMENTAL

## 7.1 Documento de Matrícula

* Modelo único municipal
* Gerado automaticamente
* Campos pré-preenchidos

---

## 7.2 Validação de Documentos

A validação ocorrerá **somente na matrícula presencial**.

Documentos serão:

* Conferidos fisicamente
* Validados pela instituição
* Sistema marcará como:

  * Documentação completa
  * Pendência
  * Indeferido

---

## 7.3 Prazo

* Prazo configurável pela Secretaria
* Sistema envia notificações
* Não haverá liberação automática de vaga
* Diretor controlará manualmente a perda de vaga

---

# ETAPA 8 — STATUS DO PROCESSO

Cada inscrição possuirá estados:

* Inscrito
* Em análise
* Classificado
* Convocado
* Matriculado
* Desistente
* Indeferido
* Encerrado

Transições registradas em log.

---

# ETAPA 9 — AUDITORIA E RASTREABILIDADE

O sistema manterá registro completo de:

* Acessos
* Alterações
* Alocações
* Cancelamentos
* Justificativas
* Emissão de documentos

Logs não editáveis.

---

# ETAPA 10 — SEGURANÇA E CONTROLE

* Controle de acesso por perfil
* Restrição por unidade
* Criptografia em trânsito
* Backup automático
* Histórico por ciclo letivo
* Impossibilidade de edição retroativa sem registro

---

# AVALIAÇÃO FINAL

O modelo agora:

* Elimina risco de manipulação manual de pontuação
* Mantém descentralização com controle
* Separa inscrição e validação documental
* Atende à exigência de lista unificada
* Mantém rastreabilidade jurídica
* Reduz risco institucional
