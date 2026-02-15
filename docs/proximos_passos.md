# Próximos passos

## 1) Congelar o escopo do MVP(Produto Mínimo Viável)

Definir, por escrito, o que entra na **primeira versão**:

* Inscrição presencial pela unidade (cadastro completo)
* Cálculo automático de pontuação
* Lista ordenada por unidade/modalidade
* Convocação/alocação (integral/parcial)
* Matrícula com validação documental (na matrícula)
* Logs mínimos (quem fez o quê e quando)

Tudo o que for “desejável”, mas não essencial (ex.: WhatsApp/SMS, relatórios avançados) fica como **Fase 2**.

## 2) Especificação funcional “executável”

Transformar requisitos em artefatos que viram desenvolvimento direto:

* Casos de uso finais + fluxos
* Regras de negócio consolidadas (A–D)
* Protótipo de telas (wireframes) com campos e validações
* Critérios de aceite por funcionalidade (checklist)

## 3) Projeto técnico

Com a modelagem fechada:

* Definir arquitetura (web app + banco + autenticação)
* Definir perfis e permissões (RBAC) com matriz de acesso
* Definir trilha de auditoria (eventos críticos)
* Definir estratégia de backup, recuperação e retenção

## 4) Planejamento de implementação

* Backlog (épicos → histórias → tarefas)
* Prioridade e entregas por sprint
* Cronograma realista com marcos:

  * versão alfa (cadastro + pontuação)
  * beta (lista + convocação)
  * release (matrícula + relatórios básicos)

## 5) Implementação incremental

Ordem recomendada para reduzir retrabalho:

1. Autenticação + perfis + instituições
2. Ciclo letivo + parametrização (critérios/pesos)
3. Inscrição completa + validações
4. Cálculo de pontuação + lista ordenada
5. Convocação/alocação + integral/parcial
6. Matrícula + validação documental
7. Relatórios + exportação
8. Logs e ajustes finos

## 6) Testes (o que mais evita dor de cabeça)

* Testes de regras (pontuação, desempate, duplicidade)
* Testes de permissão (uma unidade não vê outra)
* Testes de fluxo completo (inscreve → convoca → matrícula)
* Testes de auditoria (logs e histórico)

## 7) Piloto controlado

Antes de “colocar na rede toda”:

* Escolher 1 ou 2 unidades piloto
* Rodar um ciclo simulado com dados fictícios
* Corrigir usabilidade e pontos de erro
* Produzir manual rápido para operadores

## 8) Implantação e governança

* Treinamento curto por perfil (SME vs unidades)
* Plano de suporte (canal e prazo de resposta)
* Processo para mudanças (ex.: alterar vagas pós-bloqueio)
* Documento de responsabilidades (quem responde por quê)
