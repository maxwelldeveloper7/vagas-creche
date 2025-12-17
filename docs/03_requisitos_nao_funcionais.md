# Requisitos não Funcionais

## 1. RNF — Segurança da Informação

**RNF-01**
O sistema deve exigir autenticação obrigatória para todos os usuários, exceto nas telas públicas de informação.

**RNF-02**
O sistema deve utilizar **CPF como identificador único** de autenticação, associado a senha protegida por criptografia.

**RNF-03**
O sistema deve armazenar senhas utilizando algoritmo de **hash seguro com salt**.

**RNF-04**
O sistema deve implementar **verificação em dois fatores** para acesso de responsáveis legais, por meio de código temporário.

**RNF-05**
O sistema deve bloquear automaticamente tentativas consecutivas de acesso malsucedidas, conforme política configurável.

**RNF-06**
O sistema deve garantir que usuários acessem apenas dados compatíveis com seu perfil e escopo institucional.

---

## 2. RNF — Privacidade e LGPD

**RNF-07**
O sistema deve estar em conformidade com a **Lei Geral de Proteção de Dados (LGPD)**.

**RNF-08**
O sistema deve coletar apenas os dados estritamente necessários para os fins definidos.

**RNF-09**
O sistema deve permitir rastreabilidade de consentimento para uso dos dados dos responsáveis e crianças.

**RNF-10**
O sistema deve restringir a visualização de dados pessoais sensíveis exclusivamente a perfis autorizados.

**RNF-11**
O sistema deve manter logs de acesso a dados pessoais para fins de auditoria.

---

## 3. RNF — Desempenho e Capacidade

**RNF-12**
O sistema deve suportar, no mínimo, **1.500 inscrições** em um único ciclo anual sem degradação funcional.

**RNF-13**
O sistema deve responder às operações críticas em até **3 segundos**, em condições normais de carga.

**RNF-14**
O sistema deve suportar acessos simultâneos durante os períodos de pico de inscrição.

---

## 4. RNF — Disponibilidade e Continuidade

**RNF-15**
O sistema deve estar disponível **24 horas por dia, 7 dias por semana**, durante o período de inscrições.

**RNF-16**
O sistema deve possuir mecanismo de **backup automático diário**.

**RNF-17**
O sistema deve permitir restauração de dados a partir de backups.

**RNF-18**
O sistema deve apresentar mensagens claras ao usuário em caso de indisponibilidade temporária.

---

## 5. RNF — Confiabilidade e Integridade

**RNF-19**
O sistema deve garantir **integridade referencial** entre crianças, responsáveis, instituições e inscrições.

**RNF-20**
O sistema deve impedir duplicidade de inscrições para a mesma criança no mesmo ciclo.

**RNF-21**
O sistema deve garantir consistência dos dados mesmo em falhas parciais de processamento.

---

## 6. RNF — Usabilidade e Acessibilidade

**RNF-22**
O sistema deve possuir interface web responsiva, compatível com dispositivos móveis e desktops.

**RNF-23**
O sistema deve utilizar linguagem clara e acessível ao público geral.

**RNF-24**
O sistema deve seguir as diretrizes de **acessibilidade WCAG 2.1**, nível AA.

**RNF-25**
O sistema deve permitir navegação assistida para usuários com baixa familiaridade tecnológica.

---

## 7. RNF — Manutenibilidade e Evolução

**RNF-26**
O sistema deve possuir arquitetura modular, facilitando manutenção e evolução.

**RNF-27**
O sistema deve permitir parametrização de critérios, prazos e períodos sem alteração de código-fonte.

**RNF-28**
O sistema deve possuir documentação técnica e funcional atualizada.

---

## 8. RNF — Auditoria, Transparência e Conformidade Pública

**RNF-29**
O sistema deve manter **logs imutáveis** de acessos, alterações e decisões administrativas.

**RNF-30**
O sistema deve permitir extração de relatórios de auditoria para órgãos de controle.

**RNF-31**
O sistema deve manter histórico completo das movimentações da criança durante todo o ciclo.

---

## 9. RNF — Interoperabilidade e Integração

**RNF-32**
O sistema deve permitir integração futura com sistemas governamentais por meio de **APIs REST**.

**RNF-33**
O sistema deve utilizar formatos de dados padronizados (JSON, UTF-8).

---

## 10. RNF — Implantação e Ambiente

**RNF-34**
O sistema deve ser compatível com ambientes baseados em **Linux**.

**RNF-35**
O sistema deve permitir implantação em infraestrutura local ou em nuvem.
