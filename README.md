# SICREM — Sistema de Inscrição em Creche da Rede Municipal

Projeto open-source (GNU GPL) para gestão digital de inscrições em creches e pré-escolas do município.

## Visão Geral

O SICREM centraliza e padroniza o processo de pré-matrícula em rede municipal, com foco em:

- registros unificados em banco de dados relacional (PostgreSQL)
- rastreabilidade e auditoria de todas as operações (registro imutável)
- controle de acesso por perfis (RBAC) conforme cargos da estrutura escolar
- saneamento de dados para consultas, relatórios e exportação CSV
- geração de comprovantes em PDF

> Escopo 1.0: pré-matrículas e controle de inscrições. Convocação de vagas, matrícula definitiva e seleção final são realizados fora do sistema.

## Perfis de Usuário

- **Administrador**: configurações globais, cadastros de Secretários de Educação, criação de períodos de inscrição e acesso total a relatórios.
- **Secretário de Educação**: cadastro de unidades, diretores, secretários escolares e visibilidade de todas as inscrições.
- **Diretor**: cadastro de turmas, inscrição de crianças, edição durante período aberto e relatório da própria unidade.
- **Secretário Escolar**: mesmo nível operativo do Diretor na unidade vinculada.

## Módulos Principais

1. Autenticação segura (CPF/e-mail + senha; recuperação via e-mail institucional; bloqueio por tentativas).
2. Gestão de estrutura escolar (unidades, turmas, períodos de inscrição, vagas por turma).
3. Cadastro de responsáveis e crianças (incluindo vínculo e parentesco).
4. Registro de inscrições com critérios socioeconômicos e validações de unicidade por período.
5. Consulta, edição (somente com período aberto) e impressão de comprovantes.
6. Relatórios e exportação CSV oficial de encerramento.
7. Auditoria completa (`audit_log` com usuário, operação, entidade, diff, IP, dispositivo, timestamp).

## Modelo de Dados (Resumo)

Entidades chave:

- `periodos_inscricao`: janela de inscrições por ano letivo (`aberto` / `encerrado`).
- `unidades_escolares`: cadastro de escolas com status `ativa` / `inativa`.
- `turmas` + `definicoes_turma` + `unidade_turma`: estrutura de oferta (tipo, faixa etária, vagas) por unidade e período.
- `responsaveis`, `criancas`, `responsaveis_criancas`: cadastro de família e vínculo legal.
- `inscricoes`: registro de candidaturas com critérios socioeconômicos e integridade de dados.
- `usuarios`: perfis de acesso e autenticação.
- `audit_log`: trilha de auditoria para todos os eventos de criação/edição/leitura crítica.

## Requisitos Não Funcionais

- compatibilidade com PostgreSQL 14+;
- backend em Python (Flask, SQLAlchemy); front-end responsivo para navegadores modernos;
- comunicação via HTTPS obrigatório;
- LGPD em dados sensíveis, com criptografia de senha (`bcrypt`/`argon2`) e gestão de token de recuperação;
- logs centralizados e imutáveis; políticas de backup e restore.

## Instalação e Execução

1. clone o repositório
2. configure ambiente virtual Python 3.11+
3. instale dependências em `requirements.txt`
4. configure variáveis de ambiente (`DATABASE_URL`, `SECRET_KEY`, SMTP)
5. execute migrações do banco (SQLAlchemy/Flask-Migrate ou scripts DDL em `docs`)
6. crie usuário `administrador` inicial e períodos de inscrição
7. acesse via navegador no host/porta configurados

## Documentação

Toda a documentação é mantida em `docs/`:

- `01_PRD.md`: requisito de produto (escopo, perfis, fluxo e regras de negócio)
- `02_modelagem_de_dados.md`: DER, DBML e DDL PostgreSQL
- `03_srs_ieee830_creche.md`: especificação de requisitos de software (IEEE 830)
- `04_arc42_sicrem.md`: arquitetura de software (estrutural e de implantação)
- `05_sicrem_institucional.md`: manual operacional e uso institucional

## Contribuição

- abra issues para bugs e melhorias
- faça fork + PR com código e testes
- siga estilo de código PEP8 e práticas de segurança
- mantenha consistência com a modelagem de dados e regra de negócio do PRD

## Licença

GNU General Public License (GPL) — consulte o arquivo `LICENSE` para detalhes.

