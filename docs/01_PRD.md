# PRD — Sistema de Inscrição em Creche

## Documento de Requisitos de Produto

---

# 1. Visão Geral do Produto

## 1.1 Nome do Produto

**Sistema de Inscrição para Creche da Rede Municipal**

---

## 1.2 Propósito

Disponibilizar um sistema digital para **registro, controle e gerenciamento das inscrições de crianças em creches da rede municipal**, permitindo:

* cadastro padronizado das inscrições
* rastreabilidade administrativa das informações
* geração de comprovantes de inscrição
* consulta de inscrições realizadas
* geração de relatórios para planejamento educacional
* consolidação de dados para análise de demanda por vagas

O sistema deve funcionar como **ferramenta institucional de apoio à gestão educacional**, garantindo transparência, organização administrativa e integridade das informações registradas.

---

# 2. Problema a Ser Resolvido

Atualmente o processo de inscrição pode apresentar:

* registros manuais ou dispersos
* risco de duplicidade de inscrições
* dificuldade de rastreamento das informações
* ausência de padronização de dados
* dificuldade de consolidar informações para planejamento de vagas
* dificuldade de auditoria administrativa

O sistema proposto visa **centralizar, padronizar e registrar digitalmente o processo de inscrição**, garantindo maior confiabilidade e rastreabilidade administrativa.

---

# 3. Usuários do Sistema

## 3.1 Administrador

Responsável pela **configuração institucional e supervisão administrativa do sistema**.

### Permissões

* cadastrar unidades escolares
* cadastrar diretores
* cadastrar secretários
* cadastrar e configurar turmas
* definir períodos de inscrição
* editar cadastros institucionais
* consultar todas as inscrições
* gerar relatórios administrativos

### Restrições

O administrador **não pode alterar inscrições registradas**, nem modificar dados de responsáveis ou crianças.

Essa restrição garante **segurança institucional e integridade das informações registradas durante o atendimento**.

---

## 3.2 Operador (Diretor ou Secretário)

Responsável pelo **atendimento direto ao cidadão e registro das inscrições**.

### Permissões

* registrar inscrições
* cadastrar responsável
* cadastrar criança
* editar registros quando necessário
* consultar inscrições da própria unidade
* reemitir comprovantes de inscrição

### Restrições

* acesso apenas às inscrições da unidade vinculada
* não pode excluir inscrições

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

Esse fluxo foi organizado conforme abordagem de **User Story Mapping**, priorizando simplicidade operacional e clareza para o usuário.

---

# 5. Funcionalidades do Sistema

---

# 5.1 Autenticação

O sistema deve permitir login de usuários autorizados.

### Campos

* usuário
* senha

### Comportamento

O sistema deve:

* validar credenciais
* identificar perfil do usuário
* aplicar controle de acesso por perfil
* redirecionar o usuário ao painel correspondente

---

# 5.2 Gerenciamento da Estrutura Escolar

Apenas administradores podem cadastrar e gerenciar:

* unidades escolares
* diretores
* secretários
* turmas da educação infantil

### Cadastro de Turmas

Cada unidade escolar deve possuir turmas previamente cadastradas.

Exemplo de turmas:

* Berçário I
* Berçário II
* Berçário III
* 1º Período
* 2º Período

### Campos da Turma

* unidade escolar
* nome da turma
* idade mínima
* idade máxima
* ano letivo

Essa estrutura permite **planejamento e organização das vagas ofertadas**.

---

# 5.3 Configuração do Período de Inscrição

O sistema deve permitir definir períodos oficiais de inscrição.

### Campos

* ano letivo
* data de início
* data de encerramento
* status (aberto ou encerrado)

O sistema deve **bloquear novas inscrições fora do período configurado**, salvo autorização administrativa.

---

# 5.4 Regra de Corte Etário

A elegibilidade da criança para vagas deve considerar o **corte etário oficial de 31 de março do ano letivo**.

### Regra

A idade considerada da criança será a idade que ela possui em:

**31 de março do ano letivo da inscrição.**

### Comportamento do Sistema

O sistema deve:

* calcular automaticamente a idade na data de corte
* determinar a faixa etária elegível
* sugerir a turma compatível
* impedir cadastro de vaga incompatível com a idade

---

# 5.5 Início da Inscrição

O operador inicia uma inscrição informando:

**CPF da criança**

### Regras

O sistema deve:

1. verificar se já existe inscrição associada ao CPF

2. se existir:

   * bloquear nova inscrição
   * informar data e local da inscrição existente

3. se não existir:

   * permitir continuidade do cadastro
   * preencher automaticamente o CPF no cadastro da criança

---

# 6. Cadastro do Responsável

## 6.1 Dados de Identificação

* nome do responsável
* CPF
* RG
* parentesco com a criança
* telefone

---

## 6.2 Endereço

* endereço completo
* ponto de referência
* comprovante de endereço (registro lógico)

---

## 6.3 Situação Socioeconômica

* mãe com vínculo empregatício
* comprovante de endereço do trabalho
* demonstrativo de crédito ou benefício
* LOAS / BPC / seguro-desemprego
* trabalhador autônomo
* mãe matriculada em rede pública
* vulnerabilidade social
* declaração escolar de mãe adolescente
* renda per capita

Essas informações permitem **análise social e planejamento de políticas públicas**.

---

# 7. Cadastro da Criança

## 7.1 Identificação

* nome
* data de nascimento
* CPF
* nome do pai
* nome da mãe

---

## 7.2 Situação Educacional

* unidade escolar pretendida
* vaga pretendida
* status da inscrição

### Status possíveis

* inscrito
* em análise
* lista de espera
* contemplado
* indeferido

---

## 7.3 Situação Documental

* certidão em que não conste pai ou mãe
* irmão matriculado em unidade escolar

---

## 7.4 Encaminhamentos Institucionais

* Vara da Família
* Conselho Tutelar
* CRAS
* CREAS
* casa de acolhimento

---

## 7.5 Dados Sociais e de Saúde

* NIS
* cartão SUS
* laudo de deficiência ou neoplasia
* laudo de intolerância alimentar
* laudo de neurodivergência

Essas informações auxiliam **políticas de inclusão e priorização social**.

---

# 8. Cadastro de Irmãos

Após cadastrar uma criança, o sistema pergunta:

**Deseja cadastrar outra criança para este responsável?**

Se a resposta for positiva:

* o sistema abre novo formulário de criança
* reutiliza dados comuns do responsável

Em seguida o sistema pergunta:

**É filho do mesmo relacionamento?**

Se sim, o sistema preenche automaticamente:

* nome do pai
* nome da mãe

Todos os campos permanecem **editáveis**.

---

# 9. Conferência da Inscrição

Antes de salvar a inscrição o sistema deve exibir **um resumo completo das informações registradas**.

### Layout

Formato semelhante a **formulário institucional de conferência**.

### Informações exibidas

* dados do responsável
* dados da criança
* dados socioeconômicos
* documentos informados
* unidade pretendida
* vaga pretendida

Campos lógicos aparecem **apenas quando verdadeiros**.

---

# 10. Comprovante de Inscrição

Após registrar a inscrição, o sistema deve gerar um comprovante.

---

## 10.1 Conteúdo

### Identificação

* número da inscrição
* data e hora do registro
* unidade de registro

### Dados da Criança

* nome
* CPF
* data de nascimento
* nome do pai
* nome da mãe

### Dados do Responsável

* nome
* CPF
* telefone
* endereço

### Solicitação

* unidade pretendida
* vaga pretendida

---

## 10.2 Formato

O comprovante pode ser:

* impresso diretamente
* gerado em PDF

### Segurança

O PDF deve ser:

* criptografado
* protegido por senha baseada no CPF da criança

---

# 11. Consulta de Inscrições

## 11.1 Critérios de Busca

* nome da criança
* CPF da criança
* número da inscrição

---

## 11.2 Permissões

**Operador**

* consulta apenas inscrições da própria unidade

**Administrador**

* consulta todas as inscrições

---

## 11.3 Funcionalidades

* visualizar dados completos
* reemitir comprovante

---

# 12. Relatórios Administrativos

## 12.1 Tipos de Relatórios

### Lista geral de inscritos

* número da inscrição
* nome da criança
* unidade pretendida
* vaga pretendida
* data da inscrição

---

### Inscrições por unidade escolar

Permite analisar a demanda por escola.

---

### Inscrições por faixa etária ou vaga pretendida

Permite planejar abertura de turmas.

---

### Relatórios por critérios sociais

Incluem informações como:

* renda per capita
* vulnerabilidade social
* benefícios sociais
* encaminhamentos institucionais

---

## 12.2 Exportação

Relatórios podem ser exportados em:

* CSV

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

## 14.1 Segurança

* autenticação obrigatória
* controle de acesso por perfil
* criptografia de comprovantes
* proteção de dados pessoais

---

## 14.2 Usabilidade

* formulários simples
* preenchimento automático quando possível
* reutilização de dados para irmãos

---

## 14.3 Integridade de Dados

* validação de CPF
* prevenção de duplicidade
* validação de idade conforme corte etário

---

## 14.4 Proteção de Dados (LGPD)

O sistema deve garantir proteção dos dados pessoais coletados, incluindo:

* controle de acesso aos dados
* registro de acessos
* armazenamento seguro de informações sensíveis
* rastreabilidade de alterações

---

# 15. Fluxo de Edição de Registros (CRUD)

O sistema deve permitir **edição controlada de registros**, preservando a integridade das informações.

---

## 15.1 Princípios Gerais

A edição de dados deve:

* permitir correção de erros de digitação
* preservar integridade da inscrição
* manter rastreabilidade de alterações

Nenhuma alteração pode gerar duplicidade de inscrição.

---

## 15.2 Permissões de Edição

### Operador

Pode editar:

* dados do responsável
* dados da criança
* dados socioeconômicos
* documentos informados

Restrições:

* apenas inscrições da própria unidade
* não pode excluir inscrições

---

### Administrador

Pode editar apenas:

* unidades escolares
* diretores
* secretários
* turmas
* períodos de inscrição

Restrições:

* não pode editar inscrições
* não pode alterar dados das crianças
* não pode alterar dados dos responsáveis

---

## 15.3 Fluxo de Edição

1. usuário localiza inscrição
2. sistema exibe dados
3. usuário seleciona Editar Registro
4. sistema abre formulário preenchido
5. usuário altera dados
6. sistema executa validações
7. sistema exibe confirmação
8. alterações são gravadas

---

## 15.4 Validações de Edição

O sistema deve validar:

* formato do CPF
* duplicidade de inscrição
* campos obrigatórios
* consistência entre dados da criança e responsável

Caso haja inconsistência, a alteração deve ser bloqueada.

---

## 15.5 Registro de Auditoria (Logs de CRUD)

Todas as operações devem ser registradas para auditoria.

---

### Operações registradas

* Create
* Read
* Update
* Delete (Não será registrado pois não haverá botões de exclusão nos formários de cadastro)

---

### Informações registradas

Cada evento deve registrar:

* usuário autenticado
* perfil do usuário
* operação realizada
* entidade afetada
* identificador do registro
* data e hora
* unidade escolar vinculada
* endereço IP ou dispositivo

---

### Registro de alterações

Para operações de edição o sistema deve registrar:

* campo alterado
* valor anterior
* valor novo

---

### Finalidade

Os logs devem garantir:

* transparência administrativa
* rastreamento institucional
* auditoria
* suporte a eventuais processos administrativos ou jurídicos

Os registros devem ser **imutáveis e protegidos contra alteração manual**.
