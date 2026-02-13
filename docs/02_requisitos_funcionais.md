# ESPECIFICAÇÃO DE REQUISITOS DE SOFTWARE (SRS)

## Sistema Municipal de Gestão de Demanda por Vagas na Educação Infantil

Padrão: IEEE 830

---

# 1. Introdução

## 1.1 Propósito

Este documento especifica os requisitos funcionais do Sistema Municipal de Gestão de Demanda por Vagas na Educação Infantil, destinado à Secretaria Municipal de Educação e às instituições vinculadas.

## 1.2 Escopo

O sistema permitirá:

* Registro de inscrições presenciais;
* Parametrização anual de critérios;
* Cálculo automático de pontuação;
* Geração de lista de espera;
* Controle de alocação;
* Emissão de ficha de matrícula;
* Registro de auditoria.

---

# 2. Descrição Geral

## 2.1 Perspectiva do Produto

Sistema web institucional com acesso restrito a usuários autorizados (Secretaria e Instituições).

## 2.2 Classes de Usuários

* Administrador do Sistema
* Secretaria Municipal de Educação
* Diretor/Secretário de Instituição

Responsáveis legais não possuirão acesso ao sistema.

---

# 3. Requisitos Funcionais

---

# 3.1 Gestão de Ciclo Letivo

**RF-001** O sistema deverá permitir a criação de um novo Ciclo Letivo anual.

**RF-002** O sistema deverá permitir configurar período de inscrição para cada ciclo.

**RF-003** O sistema deverá impedir inscrição fora do período configurado.

**RF-004** O sistema deverá permitir parametrizar faixas etárias por ciclo letivo.

**RF-005** O sistema deverá impedir sobreposição de ciclos ativos.

---

# 3.2 Gestão de Usuários e Acessos

**RF-006** O sistema deverá permitir que o Administrador cadastre usuários institucionais.

**RF-007** O sistema deverá vincular cada usuário institucional a uma única unidade.

**RF-008** O sistema deverá restringir o acesso de Diretores/Secretários aos dados de sua própria unidade.

**RF-009** O sistema deverá exigir autenticação por CPF e senha.

**RF-010** O sistema deverá permitir redefinição segura de senha.

---

# 3.3 Cadastro de Instituições

**RF-011** O sistema deverá permitir que a Secretaria cadastre instituições.

**RF-012** O sistema deverá permitir definir tipo da instituição (Pública / Conveniada).

**RF-013** O sistema deverá permitir registrar endereço e dados institucionais.

---

# 3.4 Cadastro de Turmas e Vagas

**RF-014** O sistema deverá permitir cadastrar turmas por ciclo letivo.

**RF-015** O sistema deverá permitir definir modalidade da turma.

**RF-016** O sistema deverá permitir definir turno (Manhã, Tarde, Integral).

**RF-017** O sistema deverá permitir definir quantidade de vagas.

**RF-018** O sistema deverá bloquear edição de vagas após início das inscrições.

**RF-019** O sistema deverá registrar em log qualquer alteração de vagas.

---

# 3.5 Cadastro de Criança (Inscrição)

**RF-020** O sistema deverá permitir registro presencial de inscrição.

**RF-021** O sistema deverá registrar dados obrigatórios da criança.

**RF-022** O sistema deverá calcular automaticamente a faixa etária.

**RF-023** O sistema deverá impedir inscrição em modalidade incompatível com a idade.

**RF-024** O sistema deverá verificar duplicidade por CPF e data de nascimento.

**RF-025** O sistema deverá impedir novo cadastro duplicado sem justificativa formal.

**RF-026** O sistema deverá registrar se o termo LGPD foi assinado.

---

# 3.6 Cadastro de Responsáveis

**RF-027** O sistema deverá permitir cadastrar múltiplos responsáveis por criança.

**RF-028** O sistema deverá registrar dados obrigatórios do responsável.

**RF-029** O sistema não deverá exigir login para responsáveis.

---

# 3.7 Critérios e Pontuação

**RF-030** O sistema deverá permitir parametrizar critérios de prioridade por ciclo.

**RF-031** O sistema deverá permitir definir peso para cada critério.

**RF-032** O sistema deverá calcular automaticamente a pontuação total.

**RF-033** O sistema deverá impedir alteração de critérios após abertura das inscrições.

**RF-034** O sistema deverá ordenar automaticamente a lista por pontuação.

---

# 3.8 Lista de Espera

**RF-035** O sistema deverá gerar lista única por instituição e modalidade.

**RF-036** O sistema deverá atualizar automaticamente a posição na lista.

**RF-037** O sistema deverá remover automaticamente a criança das demais listas após alocação.

---

# 3.9 Alocação de Vagas

**RF-038** O sistema deverá sugerir o próximo candidato elegível.

**RF-039** O sistema deverá permitir que o Diretor confirme a alocação.

**RF-040** O sistema deverá exigir justificativa caso a ordem da lista não seja seguida.

**RF-041** O sistema deverá registrar o tipo de vaga (Integral/Parcial/Turno) no momento da alocação.

**RF-042** O sistema deverá alterar o status da inscrição para “Convocado” após alocação.

---

# 3.10 Matrícula

**RF-043** O sistema deverá gerar ficha de matrícula padronizada.

**RF-044** O sistema deverá permitir imprimir o documento.

**RF-045** O sistema deverá permitir registrar validação documental no ato da matrícula.

**RF-046** O sistema deverá permitir registrar status:

* Documentação Completa
* Pendência
* Indeferido

**RF-047** O sistema deverá permitir configurar prazo de comparecimento.

**RF-048** O sistema deverá enviar notificações de convocação.

**RF-049** O sistema deverá permitir registrar matrícula efetivada.

**RF-050** O sistema deverá alterar status para “Matriculado” após confirmação.

---

# 3.11 Notificações

**RF-051** O sistema deverá permitir envio de notificação por e-mail.

**RF-052** O sistema deverá permitir envio por SMS (quando configurado).

**RF-053** O sistema deverá permitir envio por WhatsApp (quando configurado).

**RF-054** O sistema deverá registrar envio de notificações em log.

---

# 3.12 Controle de Status

**RF-055** O sistema deverá manter estados do processo:

* Inscrito
* Classificado
* Convocado
* Matriculado
* Desistente
* Indeferido
* Encerrado

**RF-056** O sistema deverá registrar histórico de transições de status.

---

# 3.13 Auditoria e Logs

**RF-057** O sistema deverá registrar log de acessos.

**RF-058** O sistema deverá registrar log de alterações cadastrais.

**RF-059** O sistema deverá registrar log de alocações.

**RF-060** O sistema deverá registrar justificativas formais.

**RF-061** Os logs não deverão ser editáveis por usuários institucionais.

---

# 3.14 Relatórios

**RF-062** O sistema deverá permitir exportar lista de espera.

**RF-063** O sistema deverá permitir exportar relatório de classificados.

**RF-064** O sistema deverá permitir gerar relatório por unidade.

**RF-065** O sistema deverá permitir gerar relatório consolidado municipal.

---

# 3.15 Segurança

**RF-066** O sistema deverá controlar acesso por perfil.

**RF-067** O sistema deverá impedir acesso entre unidades distintas.

**RF-068** O sistema deverá manter histórico por ciclo letivo.

---

# 4. Requisitos Não Funcionais (Resumo)

* Controle de acesso seguro
* Backup periódico
* Registro de logs imutáveis
* Conformidade com LGPD
* Disponibilidade durante período de inscrição

---

# 5. Critérios de Aceitação

O sistema será considerado conforme se:

* Aplicar corretamente critérios do edital 
* Gerar lista ordenada automaticamente
* Impedir manipulação indevida
* Registrar histórico completo
