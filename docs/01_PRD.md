# PRD — Sistema de Inscrição em Creche

## Documento de Requisitos de Produto

---

# 1. Visão Geral do Produto

## 1.1 Nome do Produto

**Sistema de Inscrição para Creche da Rede Municipal**

---

## 1.2 Propósito

Disponibilizar um sistema digital para **registro, controle e gerenciamento das inscrições de crianças em creches da rede municipal**, permitindo:

- cadastro padronizado das inscrições
- rastreabilidade administrativa das informações
- geração de comprovantes de inscrição
- consulta de inscrições realizadas
- geração de relatórios para planejamento educacional
- consolidação de dados para análise de demanda por vagas

O sistema deve funcionar como **ferramenta institucional de apoio à gestão educacional**, garantindo transparência, organização administrativa e integridade das informações registradas.

---

# 2. Problema a Ser Resolvido

Atualmente o processo de inscrição pode apresentar:

- registros manuais ou dispersos
- risco de duplicidade de inscrições
- dificuldade de rastreamento das informações
- ausência de padronização de dados
- dificuldade de consolidar informações para planejamento de vagas
- dificuldade de auditoria administrativa

O sistema proposto visa **centralizar, padronizar e registrar digitalmente o processo de inscrição**, garantindo maior confiabilidade e rastreabilidade administrativa.

---

# 3. Usuários do Sistema

## 3.1 Administrador

Responsável pela **configuração institucional e supervisão administrativa do sistema**.

### Permissões

- cadastrar unidades escolares
- cadastrar diretores
- cadastrar secretários
- cadastrar e configurar turmas
- definir períodos de inscrição
- editar cadastros institucionais
- consultar todas as inscrições
- gerar relatórios administrativos

### Restrições

O administrador **não pode alterar inscrições registradas**, nem modificar dados de responsáveis ou crianças. Essa restrição garante **segurança institucional e integridade das informações registradas durante o atendimento**.

---

## 3.2 Operador (Diretor ou Secretário)

Responsável pelo **atendimento direto ao cidadão e registro das inscrições**.

### Permissões

- registrar inscrições
- cadastrar responsável
- cadastrar criança
- editar registros quando necessário
- consultar inscrições da própria unidade
- reemitir comprovantes de inscrição

### Restrições

- acesso apenas às inscrições da unidade vinculada
- não pode excluir inscrições

---

# 4. Fluxo Principal do Sistema

Fluxo operacional principal:

1. autenticar usuário
2. gerenciar estrutura escolar
3. iniciar inscrição
4. cadastrar responsável
5. cadastrar criança
6. conferir dados da inscrição
7. editar informações se necessário
8. registrar inscrição
9. gerar comprovante
10. consultar inscrições
11. gerar relatórios administrativos

Esse fluxo foi organizado priorizando **simplicidade operacional e clareza para o usuário**.

---

# 5. Funcionalidades do Sistema

## 5.1 Autenticação

O sistema deve permitir login de usuários autorizados.

### Campos

- usuário
- senha

### Comportamento

O sistema deve:

- validar credenciais
- identificar perfil do usuário
- aplicar controle de acesso por perfil
- redirecionar o usuário ao painel correspondente

---

## 5.2 Gerenciamento da Estrutura Escolar

Apenas administradores podem cadastrar e gerenciar:

- unidades escolares
- diretores
- secretários
- turmas da educação infantil

### Cadastro de Turmas

Cada unidade escolar deve possuir turmas previamente cadastradas.

Exemplo de turmas:

- Berçário I
- Berçário II
- Berçário III
- 1º Período
- 2º Período

### Campos da Turma

- unidade escolar
- nome da turma
- turno (manhã, tarde ou integral)
- idade mínima
- idade máxima
- número de vagas disponíveis
- ano letivo

Essa estrutura permite **planejamento e organização das vagas ofertadas**.

---

## 5.3 Configuração do Período de Inscrição

O sistema deve permitir definir períodos oficiais de inscrição.

### Campos

- ano letivo
- data de início
- data de encerramento
- status (aberto ou encerrado)

### Regras

- o período de inscrição ocorre **uma vez por ano**
- duração média entre **5 e 6 semanas**
- fora do período o sistema **não permitirá novos registros**

---

## 5.4 Regra de Corte Etário

A elegibilidade da criança para vagas deve considerar o **corte etário oficial de 31 de março do ano letivo**.

### Regra

A idade considerada será a idade da criança em **31 de março do ano letivo da inscrição**.

### Comportamento do Sistema

O sistema deve:

- calcular automaticamente a idade na data de corte
- determinar a faixa etária elegível
- sugerir a turma compatível
- impedir cadastro de vaga incompatível com a idade

---

## 5.5 Início da Inscrição

O operador inicia uma inscrição informando:

**CPF da criança**

### Regras

O sistema deve:

1. verificar se já existe inscrição associada ao CPF
2. se existir:
   - bloquear nova inscrição
   - informar data e local da inscrição existente
3. se não existir:
   - permitir continuidade do cadastro
   - preencher automaticamente o CPF no cadastro da criança

---

# 6. Cadastro do Responsável

## 6.1 Dados de Identificação

- nome do responsável
- CPF
- RG
- parentesco com a criança
- telefone

## 6.2 Endereço

- endereço completo
- ponto de referência
- comprovante de endereço (registro lógico)

## 6.3 Situação Socioeconômica

- mãe com vínculo empregatício
- comprovante de endereço do trabalho
- demonstrativo de crédito ou benefício
- LOAS / BPC / seguro-desemprego
- trabalhador autônomo
- mãe matriculada em rede pública
- vulnerabilidade social
- declaração escolar de mãe adolescente
- renda per capita

Essas informações permitem **análise social e planejamento de políticas públicas**.

---

# 7. Cadastro da Criança

## 7.1 Identificação

- nome
- data de nascimento
- CPF
- nome do pai
- nome da mãe

## 7.2 Situação Educacional

- unidade escolar pretendida
- vaga pretendida

Observação: o sistema registra **pré‑matrículas**, utilizadas para organização da demanda por vagas.

## 7.3 Situação Documental

- certidão em que não conste pai ou mãe
- irmão matriculado em unidade escolar

## 7.4 Encaminhamentos Institucionais

- Vara da Família
- Conselho Tutelar
- CRAS
- CREAS
- casa de acolhimento

## 7.5 Dados Sociais e de Saúde

- NIS
- cartão SUS
- laudo de deficiência ou neoplasia
- laudo de intolerância alimentar
- laudo de neurodivergência

Essas informações auxiliam **políticas de inclusão e priorização social**.

---

# 8. Cadastro de Irmãos

Após cadastrar uma criança, o sistema pergunta:

**Deseja cadastrar outra criança para este responsável?**

Se a resposta for positiva:

- o sistema abre novo formulário de criança
- reutiliza dados do responsável

Em seguida o sistema pergunta:

**É filho do mesmo relacionamento?**

Se sim, o sistema preenche automaticamente:

- nome do pai
- nome da mãe

Todos os campos permanecem **editáveis**.

---

# 9. Conferência da Inscrição

Antes de salvar a inscrição o sistema deve exibir **um resumo completo das informações registradas**.

### Informações exibidas

- dados do responsável
- dados da criança
- dados socioeconômicos
- documentos informados
- unidade pretendida
- vaga pretendida

Campos lógicos aparecem **apenas quando verdadeiros**.

---

# 10. Comprovante de Inscrição

Após registrar a inscrição, o sistema deve gerar um comprovante.

## Conteúdo

### Identificação

- número da inscrição
- data e hora do registro
- unidade de registro

### Dados da Criança

- nome
- CPF
- data de nascimento
- nome do pai
- nome da mãe

### Dados do Responsável

- nome
- CPF
- telefone
- endereço

### Solicitação

- unidade pretendida
- vaga pretendida

## Formato

O comprovante pode ser:

- impresso
- gerado em PDF

### Segurança

O PDF deve ser:

- criptografado
- protegido por senha baseada no CPF da criança

---

# 11. Consulta de Inscrições

## Critérios de Busca

- nome da criança
- CPF da criança
- número da inscrição

## Permissões

**Operador**

- consulta apenas inscrições da própria unidade

**Administrador**

- consulta todas as inscrições

## Funcionalidades

- visualizar dados completos
- reemitir comprovante

---

# 12. Relatórios Administrativos

## Tipos de Relatórios

### Lista geral de inscritos

- número da inscrição
- nome da criança
- unidade pretendida
- vaga pretendida
- data da inscrição

### Inscrições por unidade escolar

Permite analisar a demanda por escola.

### Inscrições por faixa etária ou vaga pretendida

Permite planejar abertura de turmas.

### Relatórios por critérios sociais

- renda per capita
- vulnerabilidade social
- benefícios sociais
- encaminhamentos institucionais

## Exportação

Relatórios podem ser exportados em:

- CSV

---

# 13. Regras Importantes do Sistema

1. O CPF da criança identifica a inscrição.
2. Não pode existir mais de uma inscrição por CPF.
3. A idade da criança deve considerar o corte etário de **31 de março**.
4. Campos lógicos são exibidos apenas quando verdadeiros.
5. Operadores acessam apenas dados de sua unidade.
6. O comprovante de inscrição deve ser criptografado.

---

# 14. Requisitos Não Funcionais

## Segurança

- autenticação obrigatória
- controle de acesso por perfil
- criptografia de comprovantes
- proteção de dados pessoais

## Usabilidade

- formulários simples
- preenchimento automático quando possível
- reutilização de dados para irmãos

## Integridade de Dados

- validação de CPF
- prevenção de duplicidade
- validação de idade conforme corte etário

## Proteção de Dados (LGPD)

O sistema deve garantir:

- controle de acesso aos dados
- registro de acessos
- armazenamento seguro de informações sensíveis
- rastreabilidade de alterações

---

# 15. Auditoria e Registro de Operações

Todas as operações do sistema devem gerar registros de auditoria.

### Operações registradas

- Create
- Read
- Update

Não haverá operações de exclusão de inscrições.

### Informações registradas

Cada evento deve registrar:

- usuário autenticado
- perfil do usuário
- operação realizada
- entidade afetada
- identificador do registro
- data e hora
- unidade escolar vinculada
- endereço IP ou dispositivo

### Registro de alterações

Para operações de edição devem ser registrados:

- campo alterado
- valor anterior
- valor novo

### Finalidade

Os logs garantem:

- transparência administrativa
- rastreamento institucional
- auditoria
- suporte a processos administrativos ou jurídicos

Os registros devem ser **imutáveis e protegidos contra alteração manual**.

---

# 16. Regras Operacionais Consolidadas

- A rede possui **14 unidades escolares**.
- O volume anual de inscrições costuma ficar **abaixo de 400 crianças**.
- O atendimento será **presencial nas unidades escolares**.
- O atendimento ocorre por **ordem de chegada com distribuição de senha**.
- O responsável pode **escolher livremente a unidade escolar pretendida**.
- O sistema registra **pré‑matrículas**, utilizadas para organização da demanda.
- Algumas documentações são **apenas conferidas**, podendo permanecer arquivadas fisicamente.
- O cadastro pode ser realizado por **responsável legal, familiar ou cuidador**, mediante assinatura de termo físico.

### Persistência de Registros

- nenhuma pré‑matrícula poderá ser excluída
- registros permanecem armazenados para auditoria e análise histórica

### Bloqueio de Alterações

Após o encerramento do período oficial de inscrição:

- nenhuma inscrição poderá ser editada
- nenhuma informação poderá ser alterada

Correções posteriores devem ocorrer **por procedimento administrativo externo ao sistema**.

### Exportação Oficial

Após o encerramento do período de inscrição o sistema deve permitir a geração de **arquivo CSV oficial contendo todos os registros realizados**.

