# Casos de Uso Formais
## UC-01 — Autenticar Usuário no Sistema

- **Atores:** Administrador do Sistema, Secretaria de Educação, Diretor, Secretário, Responsável Legal
- **Descrição:** Permite que um usuário autenticado acesse o sistema conforme seu perfil.
- **Pré-condições:** Usuário previamente cadastrado.
- **Pós-condições:** Usuário autenticado e sessão iniciada.

**Fluxo principal:**

1. O usuário informa CPF e senha.
2. O sistema valida as credenciais.
3. O sistema envia código de confirmação.
4. O usuário informa o código recebido.
5. O sistema libera o acesso conforme o perfil.

**Fluxos alternativos:**

* 2a. Credenciais inválidas → acesso negado.
* 4a. Código inválido ou expirado → nova tentativa.

---

## UC-02 — Cadastrar Instituição de Ensino

- **Ator:** Secretaria Municipal de Educação
- **Descrição:** Permite cadastrar instituições públicas ou conveniadas.
- **Pré-condições:** Usuário autenticado com perfil Secretaria.
- **Pós-condições:** Instituição registrada no sistema.

**Fluxo principal:**

1. A Secretaria acessa o cadastro de instituições.
2. Informa os dados obrigatórios.
3. Confirma o cadastro.
4. O sistema valida e salva as informações.

---

## UC-03 — Cadastrar Usuário Institucional

- **Ator:** Secretaria Municipal de Educação
- **Descrição:** Permite cadastrar Diretor e/ou Secretário vinculados à instituição.
- **Pré-condições:** Instituição cadastrada.
- **Pós-condições:** Usuário institucional ativo.

**Fluxo principal:**

1. A Secretaria seleciona a instituição.
2. Informa os dados do usuário.
3. Define o perfil (Diretor ou Secretário).
4. O sistema cria o usuário e envia credenciais.

---

## UC-04 — Realizar Cadastro do Responsável Legal

- **Ator:** Responsável Legal
- **Descrição:** Permite o autocadastro de responsáveis.
- **Pré-condições:** Nenhuma.
- **Pós-condições:** Responsável cadastrado e autenticável.

**Fluxo principal:**

1. O responsável informa seus dados.
2. Cria login e senha.
3. O sistema envia código de confirmação.
4. O responsável valida o cadastro.

---

## UC-05 — Cadastrar Criança

- **Ator:** Responsável Legal
- **Descrição:** Permite cadastrar os dados da criança para inscrição.
- **Pré-condições:** Responsável autenticado.
- **Pós-condições:** Criança cadastrada.

**Fluxo principal:**

1. O responsável acessa o cadastro de criança.
2. Informa os dados obrigatórios.
3. O sistema calcula a faixa etária.
4. O sistema valida a modalidade.
5. O cadastro é confirmado.

**Fluxos alternativos:**

* 4a. Modalidade incompatível → cadastro bloqueado.

---

## UC-06 — Vincular Responsáveis à Criança

- **Ator:** Responsável Legal
- **Descrição:** Permite vincular múltiplos responsáveis a uma criança.
- **Pré-condições:** Criança cadastrada.
- **Pós-condições:** Responsáveis associados.

**Fluxo principal:**

1. O responsável adiciona novos responsáveis.
2. Informa os dados obrigatórios.
3. O sistema vincula todos à criança.

---

## UC-07 — Inscrever Criança no Processo Seletivo

- **Ator:** Responsável Legal
- **Descrição:** Permite realizar a inscrição anual da criança.
- **Pré-condições:** Período de inscrição aberto.
- **Pós-condições:** Inscrição registrada.

**Fluxo principal:**

1. O responsável seleciona a criança.
2. Escolhe primeira e segunda instituição.
3. Confirma a inscrição.
4. O sistema registra a inscrição.

**Fluxos alternativos:**

* 1a. Período encerrado → inscrição negada.

---

## UC-08 — Configurar Critérios de Pontuação

-**Ator:** Secretaria Municipal de Educação
-**Descrição:** Permite definir critérios e pesos de pontuação por edital.
-**Pré-condições:** Período de inscrições ainda não iniciado.
-**Pós-condições:** Critérios publicados e bloqueados.

**Fluxo principal:**

1. A Secretaria define os critérios.
2. Atribui pontuações.
3. Publica o edital.
4. O sistema bloqueia alterações.

---

## UC-09 — Gerar Lista de Espera

- **Ator:** Sistema
- **Descrição:** Ordena automaticamente as inscrições por instituição e modalidade.
- **Pré-condições:** Inscrições registradas.
- **Pós-condições:** Lista de espera ordenada.

**Fluxo principal:**

1. O sistema calcula a pontuação.
2. Ordena a lista conforme regras.
3. Disponibiliza a lista aos diretores.

---

## UC-10 — Alocar Criança em Vaga

- **Ator:** Diretor / Secretário da Instituição
- **Descrição:** Permite alocação manual da criança em vaga disponível.
- **Pré-condições:** Lista de espera disponível.
- **Pós-condições:** Criança alocada.

**Fluxo principal:**

1. O diretor visualiza a lista.
2. Seleciona a criança.
3. Confirma a alocação.
4. O sistema remove a criança das demais listas.

---

## UC-11 — Gerar Documento de Matrícula

- **Ator:** Sistema
- **Descrição:** Gera ficha de matrícula padronizada.
- **Pré-condições:** Criança alocada.
- **Pós-condições:** Documento disponível para impressão.

**Fluxo principal:**

1. O sistema consolida os dados.
2. Preenche o modelo padrão.
3. Disponibiliza o documento.

---

## UC-12 — Notificar Responsáveis

- **Ator:** Sistema
- **Descrição:** Envia notificações automáticas aos responsáveis.
- **Pré-condições:** Evento configurado.
- **Pós-condições:** Notificação enviada.

**Fluxo principal:**

1. O sistema identifica o evento.
2. Seleciona os canais configurados.
3. Envia a notificação.

---

## UC-13 — Confirmar Matrícula Presencial

- **Ator:** Diretor / Secretário da Instituição
- **Descrição:** Confirma a efetivação da matrícula no sistema.
- **Pré-condições:** Comparecimento presencial.
- **Pós-condições:** Processo da criança encerrado.

**Fluxo principal:**

1. O usuário confirma a matrícula.
2. O sistema encerra o processo.
3. O registro é auditado.

---

## UC-14 — Acompanhar Inscrição

- **Ator:** Responsável Legal
- **Descrição:** Permite acompanhar a posição na lista de espera.
- **Pré-condições:** Inscrição realizada.
- **Pós-condições:** Status exibido ao responsável.

---

## UC-15 — Auditar Ações do Sistema

- **Ator:** Administrador do Sistema
- **Descrição:** Permite consultar logs e rastreabilidade.
- **Pré-condições:** Usuário administrador autenticado.
- **Pós-condições:** Registros auditados.
