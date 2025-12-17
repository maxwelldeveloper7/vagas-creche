# Requisitos Funcionais


## 1. Requisitos Funcionais — Gestão de Usuários e Perfis

**RF-01**
O sistema deve permitir o cadastro manual de usuários com perfil **Administrador do Sistema**.

**RF-02**
O sistema deve permitir que a **Secretaria Municipal de Educação** cadastre instituições de ensino.

**RF-03**
O sistema deve permitir que a Secretaria cadastre usuários com perfil de **Diretor** e/ou **Secretário** vinculados a uma instituição específica.

**RF-04**
O sistema deve permitir que responsáveis legais realizem **autocadastro**, criando credenciais de acesso.

**RF-05**
O sistema deve autenticar usuários por meio de **CPF e senha**.

**RF-06**
O sistema deve realizar **verificação adicional de acesso** por código de confirmação enviado por e-mail e/ou SMS.

**RF-07**
O sistema deve restringir o acesso às funcionalidades conforme o **perfil do usuário** autenticado.

---

## 2. Requisitos Funcionais — Cadastro de Crianças

**RF-08**
O sistema deve permitir o cadastro de crianças com os seguintes dados obrigatórios: nome completo, data de nascimento, sexo, CPF e Cartão SUS.

**RF-09**
O sistema deve permitir o cadastro opcional do NIS da criança.

**RF-10**
O sistema deve calcular automaticamente a **faixa etária/modalidade** da criança com base na data de nascimento.

**RF-11**
O sistema deve impedir a inscrição da criança em modalidade incompatível com sua faixa etária.

**RF-12**
O sistema deve permitir o registro da situação educacional atual da criança.

**RF-13**
O sistema deve permitir a indicação de deficiência, necessidades educacionais especiais e prioridade legal, sem exigência de upload de documentos.

---

## 3. Requisitos Funcionais — Cadastro de Responsáveis

**RF-14**
O sistema deve permitir o cadastro de **mais de dois responsáveis** vinculados a uma mesma criança.

**RF-15**
O sistema deve exigir, para cada responsável, os dados obrigatórios definidos no levantamento de requisitos.

**RF-16**
O sistema não deve exigir a definição de responsável principal.

**RF-17**
O sistema deve associar todos os responsáveis cadastrados à mesma criança para fins de comunicação.

---

## 4. Requisitos Funcionais — Instituições, Turmas e Vagas

**RF-18**
O sistema deve permitir o cadastro de instituições com identificação, tipo, endereço e dados de contato.

**RF-19**
O sistema deve permitir o cadastro de turmas por instituição, contendo modalidade, turno, quantidade de vagas e ano letivo.

**RF-20**
O sistema deve bloquear a edição da quantidade de vagas após o início do período de inscrições.

**RF-21**
O sistema deve permitir alteração de vagas apenas por usuários administrativos, mediante solicitação formal registrada.

---

## 5. Requisitos Funcionais — Inscrição e Escolha de Instituições

**RF-22**
O sistema deve permitir a abertura de um único período anual de inscrições, com datas definidas pela Secretaria.

**RF-23**
O sistema deve permitir que o responsável inscreva a criança escolhendo **até duas instituições**, indicando primeira e segunda opção.

**RF-24**
O sistema deve impedir inscrições fora do período oficial definido.

---

## 6. Requisitos Funcionais — Pontuação e Lista de Espera

**RF-25**
O sistema deve permitir que a Secretaria configure critérios de pontuação por edital.

**RF-26**
O sistema deve bloquear a edição dos critérios de pontuação após o início das inscrições.

**RF-27**
O sistema deve calcular automaticamente a pontuação total da criança com base nos critérios definidos.

**RF-28**
O sistema deve gerar uma **lista de espera única por instituição e modalidade**, ordenada pela pontuação.

**RF-29**
O sistema não deve considerar o turno como critério de ordenação da lista de espera.

---

## 7. Requisitos Funcionais — Alocação e Matrícula

**RF-30**
O sistema deve permitir que diretores visualizem a lista de espera ordenada de sua instituição.

**RF-31**
O sistema deve permitir que diretores realizem a **alocação manual** de crianças nas vagas disponíveis.

**RF-32**
O sistema deve remover automaticamente a criança das demais listas de espera após a alocação.

**RF-33**
O sistema deve gerar um **documento de matrícula padronizado**, com dados pré-preenchidos.

**RF-34**
O sistema deve controlar o prazo máximo para comparecimento, conforme parametrização da Secretaria.

**RF-35**
O sistema deve permitir que a instituição confirme a efetivação presencial da matrícula.

**RF-36**
O sistema deve encerrar o processo da criança após a confirmação da matrícula.

---

## 8. Requisitos Funcionais — Notificações

**RF-37**
O sistema deve enviar notificações aos responsáveis nos eventos de alocação, lembrete de prazo e perda de vaga.

**RF-38**
O sistema deve suportar envio de notificações por e-mail, SMS e WhatsApp, conforme configuração.

---

## 9. Requisitos Funcionais — Auditoria e Rastreabilidade

**RF-39**
O sistema deve registrar logs de acesso de todos os usuários.

**RF-40**
O sistema deve registrar logs de alterações de dados cadastrais.

**RF-41**
O sistema deve registrar logs de alocações, cancelamentos e confirmações de matrícula.

**RF-42**
O sistema deve registrar logs de emissão de documentos.
