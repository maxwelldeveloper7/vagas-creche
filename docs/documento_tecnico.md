# PREFEITURA MUNICIPAL DE NANUQUE

## SECRETARIA MUNICIPAL DE EDUCAÇÃO

# DOCUMENTO TÉCNICO

## Sistema Municipal de Gestão de Demanda por Vagas na Educação Infantil

---

## 1. APRESENTAÇÃO

Este documento apresenta a especificação técnica do **Sistema Municipal de Gestão de Demanda por Vagas na Educação Infantil**, a ser utilizado pela Rede Municipal de Ensino para organizar, classificar e acompanhar a demanda por vagas em creches e pré-escolas.

O sistema será implementado em conformidade com o Edital de Chamamento Público vigente , garantindo:

* Lista de espera unificada;
* Aplicação automática de critérios de prioridade;
* Transparência administrativa;
* Rastreabilidade das decisões;
* Segurança e controle institucional.

---

## 2. JUSTIFICATIVA

Até o momento, o cadastro e classificação da demanda vêm sendo realizados por meio de ferramentas auxiliares e procedimentos manuais, o que:

* Aumenta o risco de inconsistências;
* Exige retrabalho operacional;
* Fragiliza a rastreabilidade;
* Dificulta auditoria;
* Gera dependência de operador único.

O presente sistema visa:

* Padronizar procedimentos;
* Descentralizar o atendimento com controle centralizado;
* Reduzir riscos jurídicos;
* Assegurar equidade na classificação.

---

## 3. OBJETIVO GERAL

Implantar um sistema informatizado municipal para:

* Registrar inscrições presenciais realizadas nas unidades escolares;
* Calcular automaticamente a pontuação conforme critérios do edital;
* Gerar lista de espera ordenada;
* Controlar alocação de vagas;
* Emitir ficha de matrícula padronizada;
* Registrar histórico e auditoria.

---

## 4. ABRANGÊNCIA

### 4.1 Instituições participantes

* Creches públicas municipais;
* Escolas municipais com oferta de pré-escola;
* Creches privadas conveniadas (quando previsto em edital).

---

### 4.2 Modalidades atendidas

As faixas etárias e modalidades serão parametrizadas a cada ciclo letivo, conforme edital anual.

O sistema calculará automaticamente:

* Faixa etária com base na data de nascimento;
* Compatibilidade com a modalidade pretendida;
* Corte etário definido para o ano vigente.

---

## 5. GOVERNANÇA E PERFIS DE ACESSO

### 5.1 Administrador do Sistema (TI)

* Gestão técnica integral;
* Manutenção estrutural;
* Controle de permissões.

---

### 5.2 Secretaria Municipal de Educação

Competências:

* Cadastro de instituições;
* Cadastro de diretores e secretários;
* Parametrização anual:

  * Critérios de prioridade;
  * Pesos;
  * Calendário;
  * Modalidades;
  * Período de inscrições;
* Visualização global dos dados;
* Alterações extraordinárias mediante justificativa formal (registradas em log especial).

---

### 5.3 Diretor / Secretário da Unidade

Competências:

* Cadastro presencial das inscrições;
* Cadastro de turmas e previsão de vagas;
* Alocação de vagas;
* Confirmação de matrícula presencial;
* Registro de validação documental.

O acesso será restrito à própria unidade.

---

## 6. ESTRUTURA DO CICLO LETIVO

O sistema operará por **Ciclo Letivo Anual**, contendo:

* Regras e critérios próprios;
* Períodos configuráveis;
* Vagas vinculadas ao ano letivo.

Ao final do ciclo:

* Dados permanecerão arquivados;
* Novo ciclo será criado;
* Não haverá sobreposição normativa.

---

## 7. CADASTRO (INSCRIÇÃO)

### 7.1 Forma de inscrição

* Exclusivamente presencial;
* Realizada pela unidade;
* Sem upload de documentos;
* Registro digital no sistema.

---

### 7.2 Dados da criança

Campos obrigatórios:

* Nome completo;
* Data de nascimento;
* Sexo;
* CPF;
* Cartão SUS;
* NIS (quando houver);
* Situação educacional atual.

---

### 7.3 Validações automáticas

* Cálculo da faixa etária;
* Bloqueio de modalidade incompatível;
* Controle de duplicidade municipal (CPF + data de nascimento);
* Cálculo automático da pontuação.

---

## 8. CRITÉRIOS E PONTUAÇÃO

* Parametrizados anualmente pela Secretaria;
* Fixos após publicação do edital;
* Cumulativos;
* Cálculo automático;
* Não editáveis após início das inscrições.

A ordenação da lista obedecerá integralmente aos critérios definidos no edital vigente .

---

## 9. CADASTRO DOS RESPONSÁVEIS

* Permitido múltiplos responsáveis;
* Não haverá login para responsáveis;
* Todos poderão receber notificações.

### Dados obrigatórios:

* Nome completo;
* CPF;
* RG;
* Data de nascimento;
* Grau de parentesco;
* Endereço completo;
* Telefone;
* E-mail (quando houver).

---

## 10. LGPD E TRATAMENTO DE DADOS

Considerando tratar-se de dados pessoais e dados sensíveis (inclusive de crianças), o sistema adotará as seguintes medidas:

* Termo de ciência e autorização assinado em formulário físico no momento da inscrição;
* Registro no sistema indicando assinatura do termo;
* Controle de acesso por perfil;
* Registro de logs;
* Criptografia de dados em trânsito;
* Restrição de visualização por unidade.

---

## 11. TURMAS E VAGAS

Para cada turma:

* Modalidade;
* Ano letivo;
* Turno (Manhã / Tarde / Integral);
* Quantidade de vagas.

Após abertura das inscrições:

* Alterações de vagas serão bloqueadas;
* Modificações somente mediante solicitação formal à Secretaria.

---

## 12. LISTA DE ESPERA

* Lista única por instituição e modalidade;
* Ordenação automática por pontuação;
* Turno não interfere na ordenação.

No momento da alocação, o diretor informará:

* Se a vaga será:

  * Integral;
  * Parcial;
  * Manhã;
  * Tarde.

---

## 13. ALOCAÇÃO DE VAGAS

* Sistema sugere o próximo da lista;
* Diretor confirma a alocação;
* Caso haja exceção à ordem:

  * Justificativa obrigatória;
  * Registro em log especial.

Ao ser alocada:

* A criança é removida automaticamente das demais listas.

---

## 14. MATRÍCULA

### 14.1 Emissão de documento

O sistema gerará:

* Ficha de matrícula padronizada municipal;
* Campos pré-preenchidos;
* Impressão para assinatura física.

---

### 14.2 Validação documental

A conferência ocorrerá exclusivamente no ato da matrícula presencial.

O sistema registrará:

* Documentação completa;
* Pendência;
* Indeferimento.

---

### 14.3 Prazo de comparecimento

* Prazo configurável pela Secretaria;
* Notificações enviadas;
* Liberação de vaga realizada manualmente pela instituição.

---

## 15. STATUS DO PROCESSO

Cada inscrição possuirá status:

* Inscrito;
* Classificado;
* Convocado;
* Matriculado;
* Desistente;
* Indeferido;
* Encerrado.

Todas as mudanças serão registradas em log.

---

## 16. AUDITORIA E RASTREABILIDADE

O sistema manterá:

* Registro de acessos;
* Alterações cadastrais;
* Movimentações de lista;
* Justificativas;
* Emissão de documentos.

Os logs serão:

* Imutáveis;
* Não editáveis;
* Disponíveis para auditoria institucional.

---

## 17. SEGURANÇA E CONTROLE

* Controle de acesso por perfil;
* Restrição por unidade;
* Backup periódico;
* Criptografia de dados;
* Impossibilidade de alteração retroativa sem registro.

---

## 18. BENEFÍCIOS INSTITUCIONAIS

A implantação proporcionará:

* Transparência no processo de classificação;
* Redução de risco jurídico;
* Eliminação de planilhas paralelas;
* Padronização municipal;
* Maior controle e segurança;
* Registro histórico permanente.

---

# CONCLUSÃO

O Sistema Municipal de Gestão de Demanda por Vagas representa modernização administrativa, alinhamento normativo e fortalecimento da governança pública na Educação Infantil.

Sua implementação assegura:

* Equidade no acesso;
* Rastreabilidade das decisões;
* Segurança institucional;
* Eficiência operacional.
