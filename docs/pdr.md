# PRD — Sistema de Inscrição em Creche

## 1. Visão Geral do Produto

### 1.1 Nome do Produto

Sistema de Inscrição para Creche da Rede Municipal

### 1.2 Propósito

Disponibilizar um sistema digital para **registro e gerenciamento das inscrições de crianças em creches da rede municipal**, permitindo:

* cadastro padronizado das inscrições
* rastreabilidade administrativa
* geração de comprovantes
* consulta de inscrições
* geração de relatórios para planejamento educacional

---

# 2. Problema a Ser Resolvido

Atualmente o processo de inscrição pode apresentar:

* registros manuais ou dispersos
* risco de duplicidade de inscrições
* dificuldade de rastreamento
* dificuldade de consolidar dados para planejamento de vagas

O sistema proposto visa **centralizar e padronizar o processo de inscrição**.

---

# 3. Usuários do Sistema

## 3.1 Administrador

Responsável por configuração institucional e análise administrativa.

Permissões:

* cadastrar unidades escolares
* cadastrar diretores
* cadastrar secretários
* consultar todas as inscrições
* gerar relatórios administrativos

---

## 3.2 Operador (Diretor ou Secretário)

Responsável pelo atendimento e registro das inscrições.

Permissões:

* registrar inscrições
* cadastrar responsável
* cadastrar criança
* consultar inscrições da própria unidade
* reemitir comprovantes

---

# 4. Fluxo Principal do Sistema

Fluxo operacional principal:

1. Autenticar usuário
2. Gerenciar estrutura escolar
3. Realizar inscrição na creche
4. Cadastrar responsável
5. Cadastrar criança
6. Conferir dados da inscrição
7. Gerar comprovante de inscrição
8. Consultar inscrições
9. Gerar relatórios administrativos

Esse fluxo foi organizado conforme abordagem de **User Story Mapping**.

---

# 5. Funcionalidades do Sistema

## 5.1 Autenticação

O sistema deve permitir login de usuários.

### Campos

* usuário
* senha

### Comportamento

* validar credenciais
* identificar perfil
* redirecionar para painel do sistema

---

# 5.2 Gerenciamento da Estrutura Escolar

Apenas administradores podem cadastrar:

* unidades escolares
* diretores
* secretários

Observação:

O administrador **não pode alterar dados inseridos por diretores ou secretários**.

---

# 5.3 Início da Inscrição

O operador inicia uma inscrição informando:

* **CPF da criança**

### Regras

O sistema deve:

1. verificar se já existe inscrição para o CPF informado
2. se existir:

   * bloquear nova inscrição
   * informar onde e quando foi realizada
3. se não existir:

   * armazenar temporariamente o CPF
   * preencher automaticamente no cadastro da criança

---

# 6. Cadastro do Responsável

## Dados de identificação

* nome do responsável
* CPF
* RG
* parentesco com a criança
* telefone

---

## Endereço

* endereço completo
* ponto de referência
* comprovante de endereço (lógico)

---

## Situação socioeconômica

* mãe com vínculo empregatício
* comprovante de endereço do trabalho
* demonstrativo de crédito ou benefício
* LOAS / BPC / seguro desemprego
* autônomo
* mãe matriculada em rede pública
* vulnerabilidade social
* declaração escolar de mãe adolescente
* renda per capita

---

# 7. Cadastro da Criança

## Identificação

* nome
* data de nascimento
* CPF
* nome do pai
* nome do mãe

---

## Situação educacional

* unidade escolar pretendida
* situação
* vaga pleiteada

---

## Situação documental

* certidão em que não conste pai ou mãe
* irmão matriculado em unidade escolar

---

## Encaminhamentos institucionais

* Vara da Família
* Conselho Tutelar
* CRAS
* CREAS
* Casa de acolhimento

---

## Dados sociais e de saúde

* NIS
* cartão SUS
* laudo de deficiência ou neoplasia
* laudo de intolerância alimentar
* laudo de neurodivergência

---

# 8. Cadastro de Irmãos

Após cadastrar uma criança, o sistema pergunta:

**Deseja cadastrar outra criança para este responsável?**

Se sim:

* abre novo formulário de criança
* reutiliza dados comuns

O sistema pergunta:

**É filho do mesmo relacionamento?**

Se sim:

* preenche automaticamente

  * nome do pai
  * nome da mãe

Todos os campos permanecem **editáveis**.

---

# 9. Conferência da Inscrição

Antes de salvar, o sistema deve exibir um **resumo completo**.

### Layout

Formato semelhante a **formulário institucional de impressão**.

### Seções

* dados do responsável
* dados da criança
* dados sociais
* documentos apresentados

Campos lógicos aparecem **apenas quando verdadeiros**.

---

# 10. Comprovante de Inscrição

Após salvar a inscrição, o sistema deve gerar um comprovante.

## Conteúdo

### Identificação

* número da inscrição
* data e hora
* unidade de registro

### Dados da criança

* nome
* CPF
* data de nascimento
* nome do pai
* nome da mãe

### Dados do responsável

* nome
* CPF
* telefone
* endereço

### Solicitação

* unidade pretendida
* vaga pleiteada

---

## Formato

* impressão direta
* geração de PDF

### Segurança

O PDF deve ser:

* **criptografado**
* aberto somente com **CPF da criança**

---

# 11. Consulta de Inscrições

## Critérios de busca

* nome da criança
* CPF da criança
* número da inscrição

---

## Permissões

Operador:

* consulta apenas inscrições da própria unidade

Administrador:

* consulta todas as inscrições

---

## Funcionalidades

* visualizar dados completos
* reemitir comprovante

---

# 12. Relatórios Administrativos

## Tipos de relatórios

### 1. Lista geral de inscritos

* número da inscrição
* nome da criança
* unidade pretendida
* data da inscrição

---

### 2. Inscrições por unidade escolar

Permite analisar demanda por escola.

---

### 3. Inscrições por faixa etária ou vaga pretendida

Permite planejar turmas.

---

### 4. Relatório por critérios sociais

Inclui:

* renda per capita
* vulnerabilidade social
* benefícios sociais
* encaminhamentos institucionais

---

## Exportação

Relatórios podem ser exportados em:

* **CSV**

---

# 13. Regras Importantes do Sistema

1. CPF da criança identifica a inscrição.
2. Não pode existir **mais de uma inscrição por CPF**.
3. Campos lógicos são exibidos apenas quando verdadeiros.
4. PDF do comprovante deve ser criptografado.
5. Operadores só acessam dados de sua unidade.

---

# 14. Requisitos Não Funcionais

## Segurança

* autenticação obrigatória
* controle de acesso por perfil
* criptografia do comprovante

---

## Usabilidade

* formulários simples
* preenchimento automático quando possível
* reutilização de dados para irmãos

---

## Integridade de dados

* validação de CPF
* prevenção de duplicidade
