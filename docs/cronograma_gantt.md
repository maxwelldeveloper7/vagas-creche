Segue o **Cronograma Gantt completo**, baseado na WBS de **198 horas / 33 dias úteis**, considerando:

* 1 desenvolvedor
* 6 horas efetivas por dia
* arquitetura Flask + PostgreSQL
* dependências técnicas corretas (Pressman – modelo incremental controlado)

Vou apresentar em formato técnico e depois explico a lógica de dependências.

---

# Cronograma Gantt — Sistema de Gestão de Vagas

## Visão geral

| Fase                      | Início | Fim    | Duração |
| ------------------------- | ------ | ------ | ------- |
| Planejamento              | Dia 1  | Dia 1  | 1 dia   |
| Banco de dados            | Dia 2  | Dia 3  | 2 dias  |
| Autenticação              | Dia 4  | Dia 5  | 2 dias  |
| Cadastros administrativos | Dia 6  | Dia 8  | 3 dias  |
| Pré-matrícula             | Dia 9  | Dia 12 | 4 dias  |
| Classificação             | Dia 13 | Dia 15 | 3 dias  |
| Convocação                | Dia 16 | Dia 17 | 2 dias  |
| Matrícula                 | Dia 18 | Dia 20 | 3 dias  |
| Ficha matrícula           | Dia 21 | Dia 22 | 2 dias  |
| Checklist                 | Dia 23 | Dia 24 | 2 dias  |
| Dashboard                 | Dia 25 | Dia 27 | 3 dias  |
| Auditoria                 | Dia 28 | Dia 29 | 2 dias  |
| Notificações              | Dia 30 | Dia 31 | 2 dias  |
| Testes                    | Dia 32 | Dia 33 | 2 dias  |
| Deploy e ajustes          | Dia 34 | Dia 35 | 2 dias  |

---

# Gantt detalhado por tarefa

```
Dia  1  █ Planejamento e ambiente

Dia  2  █ Banco de dados (modelagem)
Dia  3  █ Banco de dados (ORM + migrations)

Dia  4  █ Autenticação
Dia  5  █ Controle de acesso

Dia  6  █ Cadastro edital
Dia  7  █ Cadastro critérios
Dia  8  █ Cadastro vagas e documentos

Dia  9  █ Pré-matrícula (formulário)
Dia 10  █ Pré-matrícula (persistência)
Dia 11  █ LGPD e validações
Dia 12  █ Testes pré-matrícula

Dia 13  █ Classificação SQL
Dia 14  █ Segregação por unidade
Dia 15  █ Testes classificação

Dia 16  █ Convocação backend
Dia 17  █ Convocação interface

Dia 18  █ Matrícula backend
Dia 19  █ Atualização vagas
Dia 20  █ Auditoria matrícula

Dia 21  █ Ficha matrícula template
Dia 22  █ Geração impressão

Dia 23  █ Checklist documental
Dia 24  █ Validações checklist

Dia 25  █ Dashboard backend
Dia 26  █ Dashboard interface
Dia 27  █ Dashboard testes

Dia 28  █ Auditoria sistema
Dia 29  █ Auditoria validação

Dia 30  █ Notificações backend
Dia 31  █ Worker notificações

Dia 32  █ Testes integrados
Dia 33  █ Correções

Dia 34  █ Deploy servidor
Dia 35  █ Ajustes finais
```

---

# Diagrama lógico de dependência (sequência correta)

```
Banco de Dados
     ↓
Autenticação
     ↓
Cadastros Administrativos
     ↓
Pré-matrícula
     ↓
Classificação
     ↓
Convocação
     ↓
Matrícula
     ↓
Ficha matrícula
     ↓
Checklist
     ↓
Dashboard
     ↓
Auditoria
     ↓
Notificações
     ↓
Testes
     ↓
Deploy
```

---

# Caminho crítico (Critical Path)

Este é o caminho que determina o prazo total:

```
Banco → Autenticação → Cadastros → Pré-matrícula → Classificação → Matrícula → Testes → Deploy
```

Duração total:

**35 dias úteis**

---

# Prazo calendário real

Considerando 5 dias úteis por semana:

**7 semanas**

---

# Cronograma realista com datas (exemplo)

Se iniciar em:

**Segunda-feira, 23 Fevereiro 2026**

Conclusão:

**Sexta-feira, 10 Abril 2026**

---

# Distribuição percentual do esforço

| Fase           | %   |
| -------------- | --- |
| Banco de dados | 6%  |
| Autenticação   | 5%  |
| Cadastros      | 9%  |
| Pré-matrícula  | 10% |
| Classificação  | 9%  |
| Matrícula      | 9%  |
| Dashboard      | 7%  |
| Outros         | 45% |

---

# Nível de risco do cronograma

Muito baixo, porque:

* arquitetura simples
* sem integrações externas
* sem alta concorrência
* SRS completo
* escopo bem definido

---

# Resultado final do planejamento

| Métrica          | Valor         |
| ---------------- | ------------- |
| Tamanho          | 161 PF        |
| Esforço          | 198 h         |
| Prazo técnico    | 35 dias úteis |
| Prazo calendário | 7 semanas     |
| Equipe           | 1 dev         |
| Viabilidade      | Excelente     |

