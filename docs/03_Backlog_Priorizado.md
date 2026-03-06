# Backlog Priorizado do Sistema de Inscrição em Creche

## Versão 1 — MVP (Sistema Operacional Básico)

Objetivo: permitir que as escolas **realizem inscrições completas e gerem comprovantes**.

### Autenticação

**US-01** — Acessar tela de login
**US-02** — Informar usuário e senha
**US-03** — Identificar perfil de acesso
**US-04** — Redirecionar para painel do sistema

---

### Estrutura mínima do sistema

**US-05** — Cadastrar unidade escolar
**US-06** — Cadastrar diretor
**US-07** — Cadastrar secretário

(Administrador executa essas funções)

---

### Inscrição

**US-09** — Iniciar nova inscrição informando CPF da criança
**US-10** — Verificar duplicidade de inscrição
**US-11** — Preencher automaticamente CPF da criança no cadastro
**US-12** — Informar duplicidade quando existir

---

### Cadastro do responsável

**US-13** — Registrar dados do responsável
**US-14** — Registrar dados socioeconômicos
**US-15** — Associar responsável à inscrição

---

### Cadastro da criança

**US-16** — Registrar dados da criança
**US-17** — Perguntar se deseja cadastrar outra criança
**US-18** — Reutilizar dados para cadastro de irmãos
**US-19** — Permitir editar campos preenchidos automaticamente

---

### Conferência da inscrição

**US-20** — Exibir resumo completo da inscrição
**US-21** — Mostrar dados em formato de formulário institucional
**US-22** — Ocultar campos lógicos não marcados

---

### Comprovante

**US-23** — Gerar comprovante de inscrição
**US-24** — Gerar número único de inscrição
**US-25** — Gerar PDF criptografado
**US-26** — Permitir abrir PDF com CPF da criança

---

# Versão 2 — Gestão administrativa

Objetivo: permitir **consulta e acompanhamento de inscrições**.

### Consulta de inscrições

**US-27** — Consultar inscrições da própria unidade
**US-28** — Administrador consultar todas as inscrições
**US-29** — Buscar por nome ou CPF da criança
**US-30** — Visualizar detalhes da inscrição
**US-31** — Reemitir comprovante

---

# Versão 3 — Inteligência administrativa

Objetivo: fornecer **informações para planejamento da rede escolar**.

### Relatórios

**US-32** — Relatório geral de inscritos
**US-33** — Relatório por unidade escolar
**US-34** — Relatório por faixa etária / vaga pretendida
**US-35** — Relatório com critérios sociais

---

# Backlog resumido por prioridade

| Prioridade | Entregas                                                              |
| ---------- | --------------------------------------------------------------------- |
| **MVP**    | Login, cadastro de estrutura escolar, inscrição completa, comprovante |
| **V2**     | Consulta de inscrições                                                |
| **V3**     | Relatórios administrativos                                            |

---

# Estimativa realista de complexidade

| Versão | Complexidade | Observação            |
| ------ | ------------ | --------------------- |
| MVP    | Média        | CRUD + geração de PDF |
| V2     | Baixa        | consultas e filtros   |
| V3     | Média        | agregação de dados    |
