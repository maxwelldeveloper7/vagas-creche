A seguir está um **Formulário Técnico Completo** (pronto para implementação) baseado nos campos do **ANEXO III — Ficha de Cadastramento** do edital , já organizado por seções, com **tipos de dados, regras de validação e observações**.

> Observação operacional alinhada às suas regras: **os documentos serão validados na matrícula**, porém **os campos de elegibilidade/declaração** continuam sendo registrados na inscrição (Sim/Não), conforme o edital.

---

# Formulário Técnico — Inscrição (Cadastro de Demanda Educação Infantil)

## 0) Metadados da Inscrição (controle interno do sistema)

| Campo                                              | Nome técnico         |     Tipo | Obrigatório | Validação/Regras                            |
| -------------------------------------------------- | -------------------- | -------: | :---------: | ------------------------------------------- |
| Ciclo letivo                                       | `cycle_id`           | UUID/INT |     Sim     | Deve existir e estar com inscrições abertas |
| Unidade de atendimento (onde foi feito o cadastro) | `service_unit_id`    | UUID/INT |     Sim     | Vinculada ao usuário logado                 |
| Usuário cadastrador                                | `created_by_user_id` | UUID/INT |     Sim     | Preenchido automaticamente                  |
| Data/hora do cadastro                              | `created_at`         | DATETIME |     Sim     | Preenchido automaticamente                  |
| Nº de cadastro/protocolo                           | `protocol_number`    |   STRING |     Sim     | Gerado automaticamente; único por ciclo     |
| Termo LGPD assinado em papel                       | `lgpd_paper_signed`  |  BOOLEAN |     Sim     | Sim/Não                                     |
| Observações do cadastrador                         | `notes`              |     TEXT |     Não     | Livre                                       |

---

## 1) Dados da Criança

| Campo                       | Nome técnico                     |   Tipo | Obrigatório | Validação/Regras                                            |
| --------------------------- | -------------------------------- | -----: | :---------: | ----------------------------------------------------------- |
| Nome da criança             | `child_full_name`                | STRING |     Sim     | 3–120 caracteres; sem números                               |
| Data de nascimento          | `child_birth_date`               |   DATE |     Sim     | Não pode ser futura                                         |
| Certidão de nascimento (nº) | `child_birth_certificate_number` | STRING |     Sim     | Texto livre com máscara opcional                            |
| CPF da criança              | `child_cpf`                      | STRING |     Sim     | Validação de CPF; **chave anti-duplicidade** com data nasc. |
| Nº do NIS da criança        | `child_nis`                      | STRING |     Não     | Se informado, validar tamanho/formato (somente dígitos)     |
| Nº do cartão SUS            | `child_sus_card`                 | STRING |     Sim     | Somente dígitos (recomendado)                               |

**Campos derivados (não editáveis):**

* Modalidade sugerida/calculada: `calculated_modality` (com base em `child_birth_date` e corte etário do ciclo). 

---

## 2) Filiação / Responsáveis (modelo do edital)

> O anexo pede **Nome do Pai** e **Nome da Mãe** e também dados do responsável. 
> Para implementação, recomenda-se permitir **múltiplos responsáveis**, mas manter campos de pai/mãe para compatibilidade com relatórios.

### 2.1 Campos “Pai/Mãe” (textuais)

| Campo                                                                         | Nome técnico  |   Tipo | Obrigatório | Validação/Regras                                   |
| ----------------------------------------------------------------------------- | ------------- | -----: | :---------: | -------------------------------------------------- |
| Nome do Pai                                                                   | `father_name` | STRING |     Não*    | Permitir vazio (há critério “registro incompleto”) |
| Nome da Mãe                                                                   | `mother_name` | STRING |     Não*    | Permitir vazio                                     |
| * Não obrigar para permitir registros sem pai/mãe, conforme o próprio edital. |               |        |             |                                                    |

### 2.2 Responsável principal de contato (institucional)

| Campo                               | Nome técnico         |   Tipo | Obrigatório | Validação/Regras                   |
| ----------------------------------- | -------------------- | -----: | :---------: | ---------------------------------- |
| Nome do responsável                 | `guardian_full_name` | STRING |     Sim     | 3–120 caracteres                   |
| Documento identidade do responsável | `guardian_rg`        | STRING |     Sim     | Texto livre                        |
| CPF do responsável                  | `guardian_cpf`       | STRING |     Sim     | Validar CPF                        |
| Telefone                            | `guardian_phone`     | STRING |     Sim     | Máscara; permitir celular/WhatsApp |
| (Opcional) E-mail                   | `guardian_email`     | STRING |     Não     | Validar e-mail                     |

> Se você mantiver “múltiplos responsáveis” no sistema, estes campos podem ser o “responsável atendido no balcão” e outros ficam em uma lista relacionada.

---

## 3) Endereço Residencial

| Campo               | Nome técnico              |   Tipo | Obrigatório | Validação/Regras   |
| ------------------- | ------------------------- | -----: | :---------: | ------------------ |
| Endereço completo   | `address_full`            | STRING |     Sim     | 5–200 caracteres   |
| Bairro              | `address_neighborhood`    | STRING |     Sim     | 2–80 caracteres    |
| Ponto de referência | `address_reference_point` | STRING |     Não     | Até 120 caracteres |

**Regras recomendadas:**

* Município: fixo/selecionável (`address_city`) com validação para Nanuque/MG, conforme edital. 

---

## 4) Local de Trabalho do Responsável

| Campo                      | Nome técnico                 |   Tipo | Obrigatório | Validação/Regras   |
| -------------------------- | ---------------------------- | -----: | :---------: | ------------------ |
| Endereço local de trabalho | `guardian_work_address`      | STRING |     Não     | Até 200 caracteres |
| Bairro do trabalho         | `guardian_work_neighborhood` | STRING |     Não     | Até 80 caracteres  |

---

## 5) Unidade Pretendida e Situação da Vaga

| Campo                      | Nome técnico              |     Tipo | Obrigatório | Validação/Regras                                             |
| -------------------------- | ------------------------- | -------: | :---------: | ------------------------------------------------------------ |
| Unidade escolar pretendida | `desired_school_unit_id`  | UUID/INT |     Sim     | Deve existir no cadastro do ciclo                            |
| Situação                   | `child_current_situation` |     ENUM |     Sim     | Ex.: “Em casa”, “Em outra unidade”, “Transferência”, “Outro” |
| Vaga pleiteada             | `requested_place_type`    |     ENUM |     Sim     | Ex.: “Creche”, “Pré-escola”, ou “Conforme faixa etária”      |

> Se você usar sua regra de “duas instituições”, inclua também `desired_school_unit_id_2` (opcional).

---

## 6) Indicadores e Critérios (Sim/Não) — Elegibilidade/Pontuação

> Estes campos representam **declaração/indicação no ato da inscrição**, e serão **comprovados/validados na matrícula**, conforme sua decisão. 

| Campo (rótulo)                                            | Nome técnico                                 |    Tipo | Obrigatório | Observação |
| --------------------------------------------------------- | -------------------------------------------- | ------: | :---------: | ---------- |
| Comprovante de endereço no nome do responsável            | `has_proof_address_in_guardian_name`         | BOOLEAN |     Sim     | Sim/Não    |
| Mãe com vínculo empregatício                              | `mother_has_employment_bond`                 | BOOLEAN |     Sim     | Sim/Não    |
| DCB / Bolsa Família / crédito de benefício                | `has_benefit_dcb_bolsa`                      | BOOLEAN |     Sim     | Sim/Não    |
| LOAS/BPC ou seguro desemprego                             | `has_loas_bpc_or_unemployment`               | BOOLEAN |     Sim     | Sim/Não    |
| Autônomo com declaração de renda                          | `self_employed_has_income_declaration`       | BOOLEAN |     Sim     | Sim/Não    |
| Criança afastada do convívio familiar                     | `child_removed_from_family`                  | BOOLEAN |     Sim     | Sim/Não    |
| Registro civil sem pai ou mãe                             | `civil_registry_missing_parent`              | BOOLEAN |     Sim     | Sim/Não    |
| Mãe matriculada na rede pública                           | `mother_enrolled_public_school`              | BOOLEAN |     Sim     | Sim/Não    |
| Reside em comunidade vulnerável                           | `lives_in_vulnerable_community`              | BOOLEAN |     Sim     | Sim/Não    |
| Laudo médico deficiência/neoplasia                        | `has_medical_report_disability_or_neoplasia` | BOOLEAN |     Sim     | Sim/Não    |
| Irmão matriculado em unidade escolar                      | `has_sibling_enrolled_in_unit`               | BOOLEAN |     Sim     | Sim/Não    |
| Encaminhamento por órgão (Vara/CT/CRAS/CREAS/Acolhimento) | `has_referral_protection_agency`             | BOOLEAN |     Sim     | Sim/Não    |

---

## 7) Dados Complementares do Edital

| Campo            | Nome técnico             |     Tipo | Obrigatório | Validação/Regras |
| ---------------- | ------------------------ | -------: | :---------: | ---------------- |
| Renda per capita | `per_capita_income`      |  DECIMAL |     Sim     | >= 0; moeda (R$) |
| Nº do cadastro   | `protocol_number`        |   STRING |     Sim     | Já em metadados  |
| Unidade escolar  | `desired_school_unit_id` | UUID/INT |     Sim     | Já acima         |

---

## 8) Campos do Edital (itens específicos do Anexo)

| Campo                                        | Nome técnico                           |    Tipo | Obrigatório | Observação |
| -------------------------------------------- | -------------------------------------- | ------: | :---------: | ---------- |
| Declaração escolar de mãe adolescente        | `has_teen_mother_school_declaration`   | BOOLEAN |     Não     | Sim/Não    |
| Laudo para intolerância alimentar            | `has_food_intolerance_report`          | BOOLEAN |     Não     | Sim/Não    |
| Laudo para deficiência/TGD/altas habilidades | `has_disability_tgd_giftedness_report` | BOOLEAN |     Não     | Sim/Não    |

---

# Regras de Validação Essenciais (para implementar)

1. **Anti-duplicidade**: bloquear inscrição se (`child_cpf` + `child_birth_date`) já existir no mesmo `cycle_id`.
2. **Corte etário**: modalidade calculada deve ser compatível com a “vaga pleiteada” (se você permitir escolher). 
3. **Campos booleanos**: todos os critérios devem ser explicitamente marcados (Sim/Não) para evitar “nulo”.
4. **LGPD**: `lgpd_paper_signed` obrigatório (Sim/Não), com alerta administrativo se “Não”.
5. **Residência**: exigir município configurado como Nanuque/MG (bloqueio se outro). 

---

# Saídas (outputs) do formulário

Ao salvar com sucesso, o sistema deve:

* Gerar `protocol_number` (único por ciclo);
* Calcular pontuação (com base nos critérios do ciclo) e armazenar detalhamento;
* Inserir a inscrição na lista (unidade/modalidade);
* Registrar log (criação, usuário, unidade, data/hora).

---

# Formulário Técnico — Alocação / Convocação de Vaga

## A) Metadados do Ato de Alocação

| Campo                 | Nome técnico           |     Tipo | Obrigatório | Validação/Regras                              |
| --------------------- | ---------------------- | -------: | :---------: | --------------------------------------------- |
| ID da inscrição       | `enrollment_id`        | UUID/INT |     Sim     | Deve existir e estar no status “Classificado” |
| Ciclo letivo          | `cycle_id`             | UUID/INT |     Sim     | Derivado da inscrição                         |
| Unidade executora     | `allocating_unit_id`   | UUID/INT |     Sim     | Deve ser a unidade do usuário logado          |
| Usuário alocador      | `allocated_by_user_id` | UUID/INT |     Sim     | Automático                                    |
| Data/hora da alocação | `allocated_at`         | DATETIME |     Sim     | Automático                                    |

---

## B) Seleção de Vaga/Turma

| Campo                           | Nome técnico               |     Tipo | Obrigatório | Validação/Regras                    |
| ------------------------------- | -------------------------- | -------: | :---------: | ----------------------------------- |
| Turma alvo                      | `target_class_id`          | UUID/INT |     Sim     | Deve pertencer à unidade e ao ciclo |
| Modalidade                      | `modality`                 |     ENUM |     Sim     | Deve ser compatível com a inscrição |
| Quantidade de vagas disponíveis | `available_slots_snapshot` |      INT |     Sim     | “Snapshot” no ato (para auditoria)  |

---

## C) Tipo de Atendimento (conforme sua regra)

| Campo               | Nome técnico   | Tipo | Obrigatório | Validação/Regras                                                      |
| ------------------- | -------------- | ---: | :---------: | --------------------------------------------------------------------- |
| Tipo de atendimento | `service_type` | ENUM |     Sim     | {Integral, Parcial}                                                   |
| Turno               | `shift`        | ENUM | Condicional | {Manhã, Tarde}. Obrigatório se a unidade trabalhar com turno separado |
| Observação do turno | `shift_notes`  | TEXT |     Não     | Ex.: “Preferência informada pela família”                             |

> Nota: “Integral/Parcial” é sempre obrigatório. Turno é obrigatório apenas se aplicável à modalidade/unidade.

---

## D) Controle de Ordem e Justificativa

| Campo                                    | Nome técnico                 |    Tipo | Obrigatório | Validação/Regras                                    |
| ---------------------------------------- | ---------------------------- | ------: | :---------: | --------------------------------------------------- |
| Posição do candidato na lista no momento | `rank_position_snapshot`     |     INT |     Sim     | Capturado automaticamente                           |
| É o primeiro elegível?                   | `is_first_eligible_snapshot` | BOOLEAN |     Sim     | Calculado automaticamente                           |
| Justificativa (fora da ordem)            | `out_of_order_justification` |    TEXT | Condicional | Obrigatório se `is_first_eligible_snapshot = false` |

---

## E) Convocação e Prazos

| Campo                      | Nome técnico        |     Tipo | Obrigatório | Validação/Regras          |
| -------------------------- | ------------------- | -------: | :---------: | ------------------------- |
| Data/hora início do prazo  | `deadline_start_at` | DATETIME |     Sim     | Automático na alocação    |
| Prazo em dias (config SME) | `deadline_days`     |      INT |     Sim     | Parametrizado no ciclo    |
| Data limite comparecimento | `deadline_end_at`   | DATETIME |     Sim     | Calculado automaticamente |
| Observações da convocação  | `convocation_notes` |     TEXT |     Não     | Livre                     |

---

## F) Notificações (registro)

| Campo                   | Nome técnico          |     Tipo | Obrigatório | Validação/Regras                    |
| ----------------------- | --------------------- | -------: | :---------: | ----------------------------------- |
| Notificar responsáveis? | `notify_enabled`      |  BOOLEAN |     Sim     | Conforme configuração institucional |
| Canais usados           | `notify_channels`     | SET/JSON |     Não     | Ex.: {email, sms, whatsapp}         |
| Resultado do envio      | `notify_status`       |     ENUM |     Não     | {Sucesso, Falha, Não configurado}   |
| Data/hora envio         | `notify_sent_at`      | DATETIME |     Não     | Preenchido se envio ocorrer         |
| Detalhe do erro         | `notify_error_detail` |     TEXT |     Não     | Em caso de falha                    |

---

## G) Efeito do Salvamento (ações do sistema)

Ao confirmar alocação, o sistema deverá:

* Alterar status da inscrição para **“Convocado”**
* Remover automaticamente a inscrição de outras listas do ciclo (se houver)
* Debitar 1 vaga da turma (`target_class_id`)
* Registrar logs imutáveis (alocação, justificativa, prazos, notificações)

---

# Formulário Técnico — Matrícula (Validação Documental + Confirmação)

## 0) Metadados da Matrícula

| Campo                    | Nome técnico            |     Tipo | Obrigatório | Validação/Regras                     |
| ------------------------ | ----------------------- | -------: | :---------: | ------------------------------------ |
| ID da inscrição          | `enrollment_id`         | UUID/INT |     Sim     | Deve estar no status “Convocado”     |
| Unidade da matrícula     | `enrolling_unit_id`     | UUID/INT |     Sim     | Deve ser a unidade do usuário logado |
| Usuário responsável      | `enrolled_by_user_id`   | UUID/INT |     Sim     | Automático                           |
| Data/hora do atendimento | `enrollment_service_at` | DATETIME |     Sim     | Automático                           |

---

## 1) Presença e Comparecimento

| Campo                         | Nome técnico          |     Tipo | Obrigatório | Validação/Regras                         |
| ----------------------------- | --------------------- | -------: | :---------: | ---------------------------------------- |
| Responsável compareceu?       | `guardian_present`    |  BOOLEAN |     Sim     | Sim/Não                                  |
| Data/hora comparecimento      | `guardian_present_at` | DATETIME | Condicional | Obrigatório se `guardian_present = true` |
| Observações do comparecimento | `attendance_notes`    |     TEXT |     Não     | Livre                                    |

---

## 2) Validação Documental (somente na matrícula)

### 2.1 Resultado geral

| Campo                   | Nome técnico                 |      Tipo | Obrigatório | Validação/Regras                  |
| ----------------------- | ---------------------------- | --------: | :---------: | --------------------------------- |
| Resultado da validação  | `document_validation_status` |      ENUM |     Sim     | {Completa, Pendência, Indeferido} |
| Observação geral        | `document_validation_notes`  |      TEXT |     Não     | Livre                             |
| Motivo do indeferimento | `denial_reason`              | ENUM/TEXT | Condicional | Obrigatório se `Indeferido`       |

### 2.2 Checklist documental (baseado no edital)

> O edital lista documentos necessários para matrícula e impõe vacinação atualizada. 
> O sistema registrará presença/ausência (sem upload).

| Documento                                 | Nome técnico                          |    Tipo | Obrigatório | Regra                  |
| ----------------------------------------- | ------------------------------------- | ------: | :---------: | ---------------------- |
| Declaração de trabalho / vínculo          | `doc_work_declaration_present`        | BOOLEAN |     Não     | Exigível conforme caso |
| Comprovante residência (energia, 60 dias) | `doc_address_proof_present`           | BOOLEAN |     Sim     | Sim/Não                |
| Documento foto do responsável             | `doc_guardian_id_present`             | BOOLEAN |     Sim     | Sim/Não                |
| Certidão nascimento da criança            | `doc_birth_certificate_present`       | BOOLEAN |     Sim     | Sim/Não                |
| Cartão NIS (se possui)                    | `doc_nis_present`                     | BOOLEAN |     Não     | Sim/Não                |
| Cartão SUS                                | `doc_sus_present`                     | BOOLEAN |     Sim     | Sim/Não                |
| CPF criança e responsável                 | `doc_cpf_present`                     | BOOLEAN |     Sim     | Sim/Não                |
| Cartão vacinação / Declaração atualizada  | `doc_vaccination_present`             | BOOLEAN |     Sim     | Sim/Não                |
| Laudo intolerância alimentar              | `doc_food_intolerance_report_present` | BOOLEAN |     Não     | Sim/Não                |
| Laudo deficiência/TGD/altas habilidades   | `doc_disability_report_present`       | BOOLEAN |     Não     | Sim/Não                |
| Transferência (se aplicável)              | `doc_transfer_present`                | BOOLEAN |     Não     | Sim/Não                |
| Guarda em tramitação (termo + anexos)     | `doc_guard_process_present`           | BOOLEAN |     Não     | Sim/Não                |

> Você pode manter a regra: alguns documentos são **condicionais**, mas os obrigatórios “sempre” (residência, identidade do responsável, certidão, SUS, CPF, vacinação) devem influenciar o resultado geral.

---

## 3) Definição Final da Vaga (confirmação de turma/atendimento)

| Campo                          | Nome técnico             |     Tipo | Obrigatório | Validação/Regras                  |
| ------------------------------ | ------------------------ | -------: | :---------: | --------------------------------- |
| Turma confirmada               | `confirmed_class_id`     | UUID/INT |     Sim     | Normalmente igual à turma alocada |
| Tipo de atendimento confirmado | `confirmed_service_type` |     ENUM |     Sim     | {Integral, Parcial}               |
| Turno confirmado               | `confirmed_shift`        |     ENUM | Condicional | {Manhã, Tarde} se aplicável       |
| Observações                    | `final_slot_notes`       |     TEXT |     Não     | Livre                             |

---

## 4) Emissão da Ficha de Matrícula (documento impresso)

| Campo                     | Nome técnico                |     Tipo | Obrigatório | Validação/Regras                             |
| ------------------------- | --------------------------- | -------: | :---------: | -------------------------------------------- |
| Gerar ficha de matrícula? | `generate_enrollment_form`  |  BOOLEAN |     Sim     | Permitido somente se documentação “Completa” |
| Número da ficha           | `enrollment_form_number`    |   STRING | Condicional | Gerado ao emitir                             |
| Data/hora emissão         | `enrollment_form_issued_at` | DATETIME | Condicional | Gerado ao emitir                             |

> A ficha segue o modelo municipal (Anexo de matrícula do edital). 

---

## 5) Confirmação da Matrícula

| Campo                 | Nome técnico              |     Tipo | Obrigatório | Validação/Regras                                       |
| --------------------- | ------------------------- | -------: | :---------: | ------------------------------------------------------ |
| Confirmar matrícula   | `confirm_enrollment`      |  BOOLEAN |     Sim     | Só permitir se `document_validation_status = Completa` |
| Data/hora confirmação | `enrollment_confirmed_at` | DATETIME | Condicional | Automático ao confirmar                                |
| Status final          | `final_status`            |     ENUM |     Sim     | {Matriculado, Pendente, Indeferido}                    |

**Regras:**

* Se **Completa** → permite confirmar → status **Matriculado**
* Se **Pendência** → não confirma → status **Convocado/Pendente** (conforme regra do ciclo)
* Se **Indeferido** → status **Indeferido** (gera vaga remanescente após liberação manual)

---

## 6) Notificações (matrícula)

| Campo               | Nome técnico                  |     Tipo | Obrigatório | Validação/Regras                  |
| ------------------- | ----------------------------- | -------: | :---------: | --------------------------------- |
| Enviar confirmação? | `notify_confirmation_enabled` |  BOOLEAN |     Sim     | Conforme configuração             |
| Status envio        | `notify_confirmation_status`  |     ENUM |     Não     | {Sucesso, Falha, Não configurado} |
| Data/hora envio     | `notify_confirmation_sent_at` | DATETIME |     Não     | Se houver                         |
| Erro                | `notify_confirmation_error`   |     TEXT |     Não     | Se falha                          |

---

# Formulário Técnico — Liberação Manual de Vaga (para remanescentes)

(Complementar e recomendado para fechar o ciclo)

| Campo             | Nome técnico          |     Tipo | Obrigatório | Validação/Regras                                                  |
| ----------------- | --------------------- | -------: | :---------: | ----------------------------------------------------------------- |
| ID da inscrição   | `enrollment_id`       | UUID/INT |     Sim     | Deve estar em {Desistente, Indeferido, PerdaDePrazo}              |
| Motivo            | `release_reason`      |     ENUM |     Sim     | {Desistência, PerdaDePrazo, Indeferido, Transferência, Ampliação} |
| Observação        | `release_notes`       |     TEXT |     Não     | Livre                                                             |
| Usuário liberador | `released_by_user_id` | UUID/INT |     Sim     | Automático                                                        |
| Data/hora         | `released_at`         | DATETIME |     Sim     | Automático                                                        |

Ação do sistema:

* Creditar 1 vaga na turma (se necessário/compatível com sua modelagem)
* Sugerir próximo elegível para convocação


