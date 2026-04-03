# SICREM
## Sistema de Inscrição em Creche da Rede Municipal

**Documento:** Apresentação Institucional  
**Destinatário:** Secretaria Municipal de Educação  
**Versão:** 1.0  
**Data:** 2026  

---

## O que é o SICREM

O SICREM é um sistema digital desenvolvido para organizar e registrar as inscrições de crianças nas creches da rede municipal de educação.

Nos últimos três anos, o processo de inscrição foi realizado de forma presencial na Secretaria Municipal de Educação, utilizando formulários digitais sem integração entre as unidades. O SICREM representa uma evolução significativa: **o atendimento passa a ser feito diretamente nas 14 unidades escolares da rede**, com todas as informações centralizadas em tempo real e acessíveis pela Secretaria Municipal a qualquer momento.

---

## Problema que resolve

O processo atual apresenta limitações que impactam a qualidade do atendimento e a gestão da rede:

- atendimento concentrado em um único ponto, gerando deslocamento desnecessário das famílias
- registros dispersos e sem padronização entre unidades
- dificuldade de rastrear e auditar informações
- ausência de visibilidade consolidada para planejamento de vagas
- risco de inscrições duplicadas para a mesma criança

O SICREM resolve cada um desses pontos com uma solução digital centralizada, padronizada e auditável.

---

## Como funciona

O atendimento continua sendo **presencial nas unidades escolares**, com distribuição de senha física e organização da fila feita pela própria unidade — exatamente como hoje. A diferença é que o registro da inscrição passa a ser feito diretamente no sistema, pelo Diretor ou Secretário Escolar da unidade, no momento do atendimento.

O fluxo de atendimento segue estas etapas:

**1. Identificação da criança**  
O operador informa o CPF da criança. O sistema verifica automaticamente se já existe uma inscrição para aquela criança no ano letivo vigente, evitando duplicidades.

**2. Cadastro do responsável**  
Dados de identificação, endereço, vínculo empregatício e situação socioeconômica são registrados. Essas informações subsidiam o planejamento de políticas públicas pela Secretaria.

**3. Cadastro da criança**  
Dados pessoais, unidade e turma pretendidas, encaminhamentos institucionais (Conselho Tutelar, CRAS, CREAS, Vara da Família) e informações de saúde relevantes (laudos de deficiência, neurodivergência, intolerância alimentar).

**4. Inscrição de irmãos**  
O sistema permite registrar múltiplas crianças do mesmo responsável em sequência, reutilizando os dados já cadastrados e agilizando o atendimento.

**5. Comprovante de inscrição**  
Ao final, o sistema gera automaticamente um comprovante em PDF, entregue ao responsável no momento do atendimento.

---

## O que a Secretaria Municipal pode fazer no sistema

A Secretaria Municipal de Educação tem acesso completo a todas as informações de todas as unidades, podendo:

- **visualizar em tempo real** todas as inscrições realizadas na rede
- **consultar** inscrições por nome, CPF, unidade ou ano letivo
- **acompanhar** a demanda por unidade e por turma ao longo do período de inscrição
- **gerar relatórios** com dados consolidados por critérios sociais, encaminhamentos institucionais e faixas etárias
- **exportar o arquivo CSV oficial** ao encerramento do período, para uso no planejamento de vagas

> A Secretaria Municipal **não registra nem edita inscrições** — essa responsabilidade é dos operadores das unidades. O papel da Secretaria no sistema é exclusivamente de supervisão, consulta e planejamento.

---

## Critérios de elegibilidade e priorização de vagas

O SICREM registra as pré-matrículas e coleta dados que podem subsidiar a definição de critérios de priorização. **A definição dos critérios de priorização e a condução da chamada de vagas são responsabilidade exclusiva da Secretaria Municipal de Educação**, fora do escopo do sistema.

Essa separação é intencional e garante que o sistema seja um instrumento neutro de registro, sem interferir nas decisões administrativas da Secretaria.

---

## Quem usa o sistema e o que cada perfil pode fazer

| Perfil | Quem é | O que pode fazer |
|--------|--------|-----------------|
| **Administrador** | Responsável técnico pelo sistema | Configurar o sistema, definir o período de inscrição, cadastrar o Secretário de Educação |
| **Secretário de Educação** | Gestor da rede municipal | Cadastrar unidades e operadores, visualizar todas as inscrições, gerar relatórios e exportar CSV |
| **Diretor** | Diretor da unidade escolar | Registrar e consultar inscrições da própria unidade, emitir comprovantes |
| **Secretário Escolar** | Secretário administrativo da unidade | Mesmas permissões do Diretor na própria unidade |

---

## Período de inscrição

O período de inscrição é definido pelo Administrador do sistema com data de início e data de encerramento. Durante o período aberto:

- novas inscrições podem ser registradas
- inscrições já registradas podem ser corrigidas pelos operadores das unidades

Após o encerramento do período:

- nenhuma inscrição pode ser criada ou alterada
- todos os registros ficam disponíveis para consulta e relatórios
- o arquivo CSV oficial fica disponível para exportação pela Secretaria

---

## Turmas e faixas etárias

A elegibilidade da criança é calculada automaticamente pelo sistema com base na **data de corte de 31 de março** do ano letivo — padrão nacional para creches e pré-escolas.

As turmas disponíveis na rede municipal são:

| Turma | Faixa etária (em 31/03) |
|-------|------------------------|
| Berçário I | 0 a 11 meses |
| Berçário II | 1 ano a 1 ano e 11 meses |
| Berçário III | 2 anos a 2 anos e 11 meses |
| 1º Período | 3 anos a 3 anos e 11 meses |
| 2º Período | 4 anos a 4 anos e 11 meses |

> As faixas etárias acima podem ser ajustadas pela Secretaria Municipal antes da implantação do sistema, caso as definições locais sejam diferentes.

O sistema sugere automaticamente a turma compatível com a idade da criança e **bloqueia a seleção de turmas incompatíveis**, evitando erros de registro.

---

## Segurança e privacidade dos dados

O sistema foi desenvolvido em conformidade com a **Lei Geral de Proteção de Dados Pessoais (LGPD — Lei 13.709/2018)** e com a **Lei FELCA (Lei 15.211/2025)**, que trata da proteção digital de crianças.

As principais medidas adotadas:

- **acesso por perfil:** cada usuário acessa apenas as informações pertinentes ao seu papel — operadores de uma unidade não têm acesso a dados de outras unidades
- **rastreabilidade completa:** todas as operações realizadas no sistema são registradas com identificação do usuário, data, horário e endereço de acesso — o histórico é imutável e não pode ser alterado nem pelo administrador
- **comprovantes protegidos:** os PDFs gerados são protegidos por senha baseada no CPF da criança
- **transmissão segura:** toda comunicação entre o sistema e os usuários ocorre por conexão criptografada (HTTPS)
- **senha segura:** as senhas dos operadores são armazenadas com criptografia — nenhum dado de acesso fica em texto legível no sistema

---

## Dados coletados

O sistema coleta apenas as informações necessárias para o processo de inscrição e para o planejamento educacional da rede. Nenhum dado é compartilhado com terceiros.

**Dados da criança:** nome, CPF, data de nascimento, filiação, unidade e turma pretendidas, encaminhamentos institucionais, informações de saúde relevantes (laudos), NIS e cartão SUS.

**Dados do responsável:** identificação (nome, CPF, RG), contato, endereço residencial, endereço do trabalho (opcional) e situação socioeconômica (vínculo empregatício, benefícios sociais, renda per capita).

> Informações de saúde e situação de vulnerabilidade social são coletadas exclusivamente para subsidiar o planejamento de políticas públicas pela Secretaria Municipal. O sistema não utiliza esses dados para definir prioridades de vaga.

---

## Licença e código-fonte

O SICREM é distribuído sob **GNU General Public License (GPL)**, o que significa que:

- o código-fonte é **aberto e auditável** por qualquer interessado
- o município tem total liberdade para usar, adaptar e redistribuir o sistema
- melhorias realizadas sobre o sistema devem ser disponibilizadas sob a mesma licença

Essa escolha garante que o sistema seja um **bem público**, sem dependência de fornecedores privados para sua continuidade.

---

## Próximas etapas previstas

| Etapa | Descrição |
|-------|-----------|
| Revisão das faixas etárias | Confirmação com a Secretaria Municipal das faixas etárias por turma antes da implantação |
| Homologação | Período de testes com operadores em ambiente separado, antes da entrada em produção |
| Capacitação | Treinamento dos Diretores e Secretários Escolares para uso do sistema |
| Implantação | Entrada em produção antes do período de inscrição |
| Suporte | Acompanhamento técnico durante o primeiro período de inscrição |

---

*Documento elaborado pela equipe técnica responsável pelo desenvolvimento do SICREM.*  
*Para informações técnicas detalhadas, consultar o SRS IEEE 830 v1.0 e a documentação de arquitetura Arc42 v1.0.*
