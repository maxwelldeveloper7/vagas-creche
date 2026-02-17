Segue a **WBS — Work Breakdown Structure (Estrutura Analítica do Trabalho)** completa, alinhada ao seu **SRS v1.0**, aos **161 PF**, e à arquitetura **Flask + PostgreSQL (monólito)**.

Organizei em níveis profissionais conforme Pressman e boas práticas de Engenharia de Software.

---

# 1. Planejamento e Preparação (6 h)

## 1.1 Preparação do ambiente (2 h)

* instalar dependências
* criar estrutura do projeto Flask
* configurar PostgreSQL
* configurar SQLAlchemy
* configurar migrations (Alembic)

## 1.2 Configuração base do projeto (2 h)

* estrutura MVC
* configuração de ambiente
* configuração de logging

## 1.3 Controle de versão (2 h)

* repositório Git
* estrutura de branches
* .env e configurações

---

# 2. Modelagem e Banco de Dados (12 h)

## 2.1 Modelagem lógica (4 h)

Criar modelos:

* edital
* criterio
* unidade
* usuario
* aluno
* responsavel
* pre_matricula
* pre_matricula_criterio
* vaga_ofertada
* convocacao
* matricula
* checklist_documental
* auditoria
* notificacao

## 2.2 Implementação SQLAlchemy (6 h)

* classes ORM
* relacionamentos
* constraints
* UNIQUE vaga_ofertada

## 2.3 Migrações e testes (2 h)

---

# 3. Autenticação e Segurança (10 h)

## 3.1 Login/logout (4 h)

* autenticação
* hash senha
* sessão

## 3.2 Controle de acesso por perfil (6 h)

* ADMIN
* SECRETARIA
* DIRETOR
* SECRETARIO

---

# 4. Cadastros Administrativos (18 h)

## 4.1 Cadastro de edital (4 h)

## 4.2 Cadastro de critérios (6 h)

* associação com campo_formulario
* validação RN-13

## 4.3 Cadastro de documentos obrigatórios (2 h)

## 4.4 Cadastro de vagas (6 h)

* entidade vaga_ofertada
* validação de unicidade

---

# 5. Cadastro de Pré-matrícula (20 h)

## 5.1 Formulário completo (10 h)

* dados aluno
* responsável
* socioeconômico
* critérios dinâmicos

## 5.2 Consentimento LGPD (2 h)

* flag de confirmação
* bloqueio RN-15

## 5.3 Persistência (4 h)

* pre_matricula
* pre_matricula_criterio

## 5.4 Testes (4 h)

---

# 6. Classificação Dinâmica (18 h)

## 6.1 Consulta SQL classificação (10 h)

* cálculo soma pontos
* ordenação
* desempate

## 6.2 Segregação por unidade (4 h)

## 6.3 Otimização e testes (4 h)

---

# 7. Convocação (10 h)

## 7.1 Interface convocação (4 h)

## 7.2 Persistência convocacao (3 h)

## 7.3 Auditoria e notificação (3 h)

---

# 8. Matrícula (18 h)

## 8.1 Efetivar matrícula (8 h)

* validações RN-06, RN-11
* criação matricula

## 8.2 Atualizar vagas (3 h)

## 8.3 Remover outras pré-matrículas (3 h)

## 8.4 Auditoria (4 h)

---

# 9. Ficha de Matrícula (10 h)

## 9.1 Template HTML (4 h)

## 9.2 Geração PDF / impressão (4 h)

## 9.3 Testes (2 h)

---

# 10. Checklist Documental (10 h)

## 10.1 Interface checklist (5 h)

## 10.2 Persistência (3 h)

## 10.3 Validação obrigatória (2 h)

---

# 11. Dashboard Institucional (14 h)

## 11.1 Backend consultas (8 h)

## 11.2 Interface (6 h)

Indicadores:

* total pré-matrículas
* vagas ocupadas
* vagas disponíveis
* matriculados

---

# 12. Auditoria e Logs (10 h)

## 12.1 Implementar tabela auditoria (3 h)

## 12.2 Registrar eventos críticos (7 h)

---

# 13. Notificações (8 h)

## 13.1 Backend notificações (5 h)

## 13.2 Worker básico (3 h)

---

# 14. Testes (16 h)

## 14.1 Testes funcionais (10 h)

## 14.2 Testes integrados (6 h)

---

# 15. Implantação (8 h)

## 15.1 Configuração servidor (4 h)

## 15.2 Deploy (4 h)

---

# 16. Correções e Ajustes (10 h)

Margem de estabilização.

---

# Total Final

| Categoria       | Horas |
| --------------- | ----- |
| Planejamento    | 6     |
| Banco de dados  | 12    |
| Autenticação    | 10    |
| Cadastros       | 18    |
| Pré-matrícula   | 20    |
| Classificação   | 18    |
| Convocação      | 10    |
| Matrícula       | 18    |
| Ficha matrícula | 10    |
| Checklist       | 10    |
| Dashboard       | 14    |
| Auditoria       | 10    |
| Notificações    | 8     |
| Testes          | 16    |
| Deploy          | 8     |
| Correções       | 10    |

---

# TOTAL = 198 horas

---

# Prazo realista

6 horas/dia:

[
198 ÷ 6 = 33 dias úteis
]

≈ **6,5 semanas**

---

# Classificação final do projeto

| Métrica      | Valor         |
| ------------ | ------------- |
| Tamanho      | 161 PF        |
| Esforço      | 198 h         |
| Prazo        | 33 dias úteis |
| Risco        | baixo         |
| Complexidade | moderada      |
| Arquitetura  | simples       |

