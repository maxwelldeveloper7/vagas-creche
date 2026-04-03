# Documentação de Arquitetura — SICREM
## Sistema de Inscrição em Creche da Rede Municipal

**Padrão:** Arc42 v8  
**Versão:** 1.0  
**Stack:** Flask 3.x + PostgreSQL 14+  
**Licença:** GNU General Public License (GPL)  
**Data:** 2026  
**Status:** Em elaboração  

---

## Histórico de Revisões

| Versão | Data | Descrição |
|--------|------|-----------|
| 1.0 | 2026 | Versão inicial derivada do SRS IEEE 830 v1.0 e DDL PostgreSQL v1.0 |

---

## Sumário

1. [Introdução e Objetivos](#1-introdução-e-objetivos)
2. [Restrições de Arquitetura](#2-restrições-de-arquitetura)
3. [Escopo e Contexto do Sistema](#3-escopo-e-contexto-do-sistema)
4. [Estratégia de Solução](#4-estratégia-de-solução)
5. [Visão de Blocos — Decomposição do Sistema](#5-visão-de-blocos--decomposição-do-sistema)
6. [Visão de Runtime — Fluxos Principais](#6-visão-de-runtime--fluxos-principais)
7. [Visão de Deployment](#7-visão-de-deployment)
8. [Conceitos Transversais](#8-conceitos-transversais)
9. [Decisões de Arquitetura](#9-decisões-de-arquitetura)
10. [Requisitos de Qualidade](#10-requisitos-de-qualidade)
11. [Riscos Técnicos](#11-riscos-técnicos)
12. [Glossário Técnico](#12-glossário-técnico)

---

## 1. Introdução e Objetivos

### 1.1 Contexto

O SICREM substitui um processo manual de pré-matrícula conduzido via Google Forms na Secretaria Municipal de Educação. A inovação central é a **descentralização do atendimento** para 14 unidades escolares, mantendo visibilidade centralizada em tempo real pela Secretaria.

### 1.2 Objetivos de Qualidade

Os objetivos de qualidade que guiam as decisões arquiteturais deste documento, em ordem de prioridade:

| Prioridade | Atributo | Motivação |
|:---:|---------|-----------|
| 1 | **Integridade de dados** | Inscrições são registros públicos — inconsistência tem impacto jurídico e administrativo |
| 2 | **Rastreabilidade** | Conformidade com LGPD e suporte a processos administrativos exigem auditoria completa |
| 3 | **Segurança** | Dados sensíveis de crianças (laudos, situação social, NIS) exigem controle rigoroso |
| 4 | **Usabilidade** | Operadores sem perfil técnico avançado — a interface deve ser simples e orientada à tarefa |
| 5 | **Manutenibilidade** | Sistema público com ciclo de vida longo — código deve ser legível e sustentável |

### 1.3 Stakeholders

| Stakeholder | Interesse arquitetural |
|-------------|----------------------|
| Secretaria Municipal de Educação | Visibilidade global, relatórios, exportação CSV oficial |
| Diretores e Secretários Escolares | Sistema estável e simples durante o período de inscrição |
| Administrador do sistema | Facilidade de configuração, deploy e manutenção |
| Responsáveis pelos alunos | Receber comprovante correto — interesse indireto |
| Equipe de desenvolvimento | Código organizado, decisões documentadas, stack familiar |

---

## 2. Restrições de Arquitetura

### 2.1 Restrições Técnicas

| Restrição | Descrição |
|-----------|-----------|
| RC-T01 | Stack obrigatório: Python 3.11+ / Flask 3.x / PostgreSQL 14+ |
| RC-T02 | Sistema exclusivamente online — sem suporte a modo offline |
| RC-T03 | Deploy em servidor Linux (Ubuntu 22.04 LTS ou superior recomendado) |
| RC-T04 | Toda comunicação via HTTPS — TLS 1.2 mínimo |
| RC-T05 | Banco de dados exclusivamente PostgreSQL — sem suporte a outros SGBD na v1.0 |

### 2.2 Restrições Organizacionais

| Restrição | Descrição |
|-----------|-----------|
| RC-O01 | Código-fonte sob GNU GPL |
| RC-O02 | Conformidade com LGPD (Lei 13.709/2018) e Lei FELCA (Lei 15.211/2025) |
| RC-O03 | Volume controlado: 14 unidades, menos de 400 inscrições por ano, período de 5 a 6 semanas |
| RC-O04 | Operadores sem perfil técnico — interface deve minimizar erros operacionais |

### 2.3 Convenções

- idioma do código-fonte: português para nomes de domínio (entidades, campos), inglês para estruturas técnicas (funções utilitárias, configuração)
- nomes de rotas: português, kebab-case (ex: `/inscricoes/nova`)
- nomes de tabelas e colunas: português, snake_case — conforme DDL
- variáveis de ambiente: maiúsculas com prefixo `SICREM_` (ex: `SICREM_DATABASE_URL`)

---

## 3. Escopo e Contexto do Sistema

### 3.1 Contexto de Negócio

```
                         ┌─────────────────────────────┐
                         │           SICREM             │
  Operadores ────────────►  (Diretores / Sec. Escolares) │
  (14 unidades)          │                             │
                         │  Registro de inscrições     │
  Secretaria Mun. ───────►  Relatórios globais         │
  de Educação            │  Exportação CSV             │
                         │                             │
  Administrador ─────────►  Configuração do sistema    │
                         └──────────┬──────────────────┘
                                    │
                         ┌──────────▼──────────────────┐
                         │       PostgreSQL             │
                         │  (dados + audit_log)        │
                         └─────────────────────────────┘
```

### 3.2 Contexto Técnico

```
┌─────────────────────────────────────────────────────────────┐
│                        Infraestrutura                        │
│                                                             │
│  Navegador ──HTTPS──► Nginx (proxy reverso + TLS)           │
│                              │                              │
│                       Gunicorn (WSGI)                        │
│                              │                              │
│                        Flask App                            │
│                              │                              │
│                       SQLAlchemy ORM                        │
│                              │                              │
│                        PostgreSQL 14                        │
│                              │                              │
│                    Servidor SMTP (e-mail)                    │
└─────────────────────────────────────────────────────────────┘
```

**Interfaces externas:**

| Interface | Protocolo | Direção | Descrição |
|-----------|-----------|---------|-----------|
| Navegador | HTTPS | Entrada | Acesso dos operadores via browser |
| PostgreSQL | TCP (psycopg2) | Saída | Persistência de dados |
| Servidor SMTP | SMTP/TLS | Saída | Envio de tokens de recuperação de senha e senha inicial |

---

## 4. Estratégia de Solução

### 4.1 Decisões Fundamentais

**Arquitetura em camadas (Layered Architecture)**

Dada a simplicidade do domínio, o volume controlado e a necessidade de manutenibilidade por equipe enxuta, a arquitetura em camadas é a escolha mais adequada. Evita a complexidade desnecessária de arquiteturas orientadas a eventos ou microsserviços para um sistema com escopo bem delimitado.

```
┌──────────────────────────────────┐
│         Camada de Apresentação   │  Rotas Flask + Templates Jinja2
├──────────────────────────────────┤
│         Camada de Serviço        │  Lógica de negócio + orquestração
├──────────────────────────────────┤
│         Camada de Repositório    │  Acesso a dados via SQLAlchemy
├──────────────────────────────────┤
│         Camada de Dados          │  PostgreSQL 14
└──────────────────────────────────┘
```

**Server-side rendering com Jinja2**

Dado o perfil dos operadores (sem expertise técnica, uso em máquinas das unidades escolares sem garantia de performance para SPAs), o rendering server-side com Jinja2 é mais adequado que um frontend JavaScript desacoplado. Reduz complexidade de deploy e elimina uma camada de API REST desnecessária para o contexto.

**ORM com SQLAlchemy 2.x**

SQLAlchemy fornece abstração do banco mantendo acesso direto a SQL quando necessário. A versão 2.x introduz a API assíncrona e typing melhorado, aumentando a manutenibilidade.

### 4.2 Decomposição em Módulos Flask

O sistema é organizado como uma aplicação Flask com **Blueprints** por módulo funcional, seguindo a estrutura de Application Factory.

---

## 5. Visão de Blocos — Decomposição do Sistema

### 5.1 Estrutura de Diretórios

```
sicrem/
│
├── app/                          # Pacote principal da aplicação
│   ├── __init__.py               # Application Factory (create_app)
│   ├── extensions.py             # Instâncias de extensões (db, login_manager, mail)
│   ├── config.py                 # Configurações por ambiente
│   │
│   ├── models/                   # Modelos SQLAlchemy (mapeamento ORM)
│   │   ├── __init__.py
│   │   ├── periodo.py            # PeriodoInscricao
│   │   ├── unidade.py            # UnidadeEscolar
│   │   ├── usuario.py            # Usuario
│   │   ├── turma.py              # Turma, DefiniçãoTurma, UnidadeTurma
│   │   ├── responsavel.py        # Responsavel
│   │   ├── crianca.py            # Crianca
│   │   ├── vinculo.py            # ResponsavelCrianca
│   │   ├── inscricao.py          # Inscricao
│   │   └── audit.py              # AuditLog
│   │
│   ├── repositories/             # Camada de acesso a dados
│   │   ├── __init__.py
│   │   ├── base.py               # BaseRepository com operações comuns
│   │   ├── inscricao_repo.py
│   │   ├── responsavel_repo.py
│   │   ├── crianca_repo.py
│   │   ├── usuario_repo.py
│   │   └── unidade_repo.py
│   │
│   ├── services/                 # Camada de lógica de negócio
│   │   ├── __init__.py
│   │   ├── auth_service.py       # Autenticação, recuperação de senha
│   │   ├── inscricao_service.py  # Orquestração do fluxo de inscrição
│   │   ├── corte_etario.py       # Cálculo de faixa etária (31/03)
│   │   ├── comprovante_service.py # Geração de PDF
│   │   ├── relatorio_service.py  # Geração de relatórios e CSV
│   │   └── audit_service.py      # Registro de operações no audit_log
│   │
│   ├── blueprints/               # Rotas organizadas por módulo
│   │   ├── auth/                 # Login, logout, recuperação de senha
│   │   ├── admin/                # Períodos, configuração do sistema
│   │   ├── secretaria/           # Unidades, usuários, relatórios globais
│   │   ├── inscricoes/           # Fluxo completo de inscrição
│   │   ├── consulta/             # Busca e visualização de inscrições
│   │   └── relatorios/           # Relatórios e exportação CSV
│   │
│   ├── templates/                # Templates Jinja2
│   │   ├── base.html             # Layout base com navbar por perfil
│   │   ├── auth/
│   │   ├── admin/
│   │   ├── secretaria/
│   │   ├── inscricoes/
│   │   ├── consulta/
│   │   └── relatorios/
│   │
│   ├── static/                   # CSS, JS, imagens
│   │   ├── css/
│   │   └── js/
│   │
│   └── utils/                    # Utilitários transversais
│       ├── cpf.py                # Validação de CPF (dígitos verificadores)
│       ├── decorators.py         # @requer_perfil, @periodo_aberto
│       ├── paginacao.py
│       └── formatadores.py
│
├── migrations/                   # Alembic — migrações de banco de dados
│
├── tests/                        # Testes automatizados
│   ├── unit/
│   ├── integration/
│   └── conftest.py
│
├── scripts/                      # Scripts utilitários
│   ├── seed.py                   # Popula definicoes_turma e dados iniciais
│   └── criar_admin.py            # Cria o primeiro usuário Administrador
│
├── .env.example                  # Template de variáveis de ambiente
├── requirements.txt
├── requirements-dev.txt
├── wsgi.py                       # Entry point para Gunicorn
└── README.md
```

### 5.2 Módulos e Responsabilidades

#### 5.2.1 Application Factory (`app/__init__.py`)

```python
def create_app(config_name: str = "production") -> Flask:
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Inicializa extensões
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)

    # Registra blueprints
    from .blueprints.auth       import bp as auth_bp
    from .blueprints.admin      import bp as admin_bp
    from .blueprints.secretaria import bp as secretaria_bp
    from .blueprints.inscricoes import bp as inscricoes_bp
    from .blueprints.consulta   import bp as consulta_bp
    from .blueprints.relatorios import bp as relatorios_bp

    app.register_blueprint(auth_bp,       url_prefix="/auth")
    app.register_blueprint(admin_bp,      url_prefix="/admin")
    app.register_blueprint(secretaria_bp, url_prefix="/secretaria")
    app.register_blueprint(inscricoes_bp, url_prefix="/inscricoes")
    app.register_blueprint(consulta_bp,   url_prefix="/consulta")
    app.register_blueprint(relatorios_bp, url_prefix="/relatorios")

    return app
```

#### 5.2.2 Camada de Modelos

Mapeamento ORM fiel ao DDL. Exemplo representativo:

```python
# app/models/inscricao.py
from app.extensions import db

class Inscricao(db.Model):
    __tablename__ = "inscricoes"

    id                    = db.Column(db.Integer, primary_key=True)
    numero_inscricao      = db.Column(db.String(20), unique=True, nullable=False)
    responsavel_id        = db.Column(db.String(11), nullable=False)
    crianca_id            = db.Column(db.String(11), nullable=False)
    unidade_id            = db.Column(db.Integer,    nullable=False)
    turma_id              = db.Column(db.Integer,    nullable=False)
    periodo_id            = db.Column(db.Integer,    nullable=False)
    operador_id           = db.Column(db.String(11),
                               db.ForeignKey("usuarios.cpf"), nullable=False)
    criado_em             = db.Column(db.DateTime(timezone=True),
                               server_default=db.func.now(), nullable=False)

    # situação socioeconômica
    mae_empregada         = db.Column(db.Boolean, default=False, nullable=False)
    mae_autonoma          = db.Column(db.Boolean, default=False, nullable=False)
    loas_bpc              = db.Column(db.Boolean, default=False, nullable=False)
    seguro_desemprego     = db.Column(db.Boolean, default=False, nullable=False)
    mae_estudante         = db.Column(db.Boolean, default=False, nullable=False)
    vulnerabilidade_social= db.Column(db.Boolean, default=False, nullable=False)
    renda_per_capita      = db.Column(db.Numeric(10, 2))

    # encaminhamentos / saúde
    vara_familia          = db.Column(db.Boolean, default=False, nullable=False)
    conselho_tutelar      = db.Column(db.Boolean, default=False, nullable=False)
    cras_creas            = db.Column(db.Boolean, default=False, nullable=False)
    laudo_deficiencia     = db.Column(db.Boolean, default=False, nullable=False)
    laudo_intolerancia    = db.Column(db.Boolean, default=False, nullable=False)
    laudo_neurodivergencia= db.Column(db.Boolean, default=False, nullable=False)
    nis                   = db.Column(db.String(13))
    cartao_sus            = db.Column(db.String(15))
    irmao_matriculado     = db.Column(db.Boolean, default=False, nullable=False)

    # FK composta → responsaveis_criancas
    __table_args__ = (
        db.ForeignKeyConstraint(
            ["responsavel_id", "crianca_id"],
            ["responsaveis_criancas.responsavel_id",
             "responsaveis_criancas.crianca_id"]
        ),
        db.ForeignKeyConstraint(
            ["unidade_id", "turma_id", "periodo_id"],
            ["unidade_turma.unidade_id",
             "unidade_turma.turma_id",
             "unidade_turma.periodo_id"]
        ),
        db.UniqueConstraint("crianca_id", "periodo_id",
                            name="uk_inscricao_unica_por_periodo"),
    )
```

#### 5.2.3 Camada de Serviço

A camada de serviço contém toda a lógica de negócio. As rotas (blueprints) não contêm lógica — apenas recebem a requisição, delegam ao serviço e renderizam a resposta.

**`corte_etario.py` — serviço crítico:**

```python
from datetime import date

def calcular_idade_meses_no_corte(data_nascimento: date, ano_letivo: int) -> int:
    """
    Calcula a idade em meses completos na data de corte (31/03 do ano letivo).
    Regra central de negócio — RF-011.
    """
    data_corte = date(ano_letivo, 3, 31)
    delta_anos  = data_corte.year  - data_nascimento.year
    delta_meses = data_corte.month - data_nascimento.month
    total_meses = delta_anos * 12 + delta_meses
    if data_corte.day < data_nascimento.day:
        total_meses -= 1
    return max(total_meses, 0)


def sugerir_turma(idade_meses: int,
                  turmas_disponiveis: list) -> tuple:
    """
    Retorna (turma_sugerida, turmas_invalidas).
    turmas_invalidas são bloqueadas na interface.
    """
    sugerida  = None
    invalidas = []
    for turma in turmas_disponiveis:
        definicao = turma.definicao
        if definicao.min_meses <= idade_meses <= definicao.max_meses:
            sugerida = turma
        else:
            invalidas.append(turma.id)
    return sugerida, invalidas
```

**`inscricao_service.py` — orquestrador do fluxo principal:**

```python
def registrar_inscricao(dados: dict, operador: Usuario) -> Inscricao:
    """
    Orquestra o fluxo completo de registro de inscrição.
    RF-014.
    """
    # 1. Verificar período aberto
    periodo = periodo_repo.buscar_periodo_aberto()
    if not periodo:
        raise PeriodoFechadoError("Não há período de inscrição aberto.")

    # 2. Verificar duplicidade
    if inscricao_repo.existe_inscricao(dados["crianca_cpf"], periodo.id):
        raise InscricaoDuplicadaError("Já existe inscrição para esta criança neste período.")

    # 3. Garantir cadastro do responsável
    responsavel = responsavel_repo.buscar_ou_criar(dados["responsavel"])

    # 4. Garantir cadastro da criança
    crianca = crianca_repo.buscar_ou_criar(dados["crianca"])

    # 5. Garantir vínculo responsavel_crianca
    vinculo_repo.garantir_vinculo(responsavel.cpf, crianca.cpf, dados["parentesco"])

    # 6. Gerar número de inscrição
    numero = gerar_numero_inscricao(periodo.ano_letivo)

    # 7. Persistir inscrição
    inscricao = inscricao_repo.criar(dados, numero, operador.cpf)

    # 8. Registrar no audit_log
    audit_service.registrar(
        usuario=operador,
        operacao="C",
        entidade="inscricoes",
        registro_id=str(inscricao.id),
        request=current_request
    )

    return inscricao
```

#### 5.2.4 Decorators de Controle de Acesso

```python
# app/utils/decorators.py
from functools import wraps
from flask import abort
from flask_login import current_user

def requer_perfil(*perfis):
    """Restringe acesso a perfis específicos. RF-004."""
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if current_user.perfil not in perfis:
                abort(403)
            return f(*args, **kwargs)
        return wrapper
    return decorator

def periodo_aberto(f):
    """Bloqueia operação se não houver período aberto. RF-009."""
    @wraps(f)
    def wrapper(*args, **kwargs):
        from app.repositories.periodo_repo import buscar_periodo_aberto
        if not buscar_periodo_aberto():
            abort(403, description="Não há período de inscrição aberto.")
        return f(*args, **kwargs)
    return wrapper
```

**Uso nas rotas:**

```python
@bp.route("/nova", methods=["GET", "POST"])
@login_required
@requer_perfil("diretor", "secretario_escolar")
@periodo_aberto
def nova_inscricao():
    ...
```

---

## 6. Visão de Runtime — Fluxos Principais

### 6.1 Fluxo de Login

```
Navegador          Flask/auth          auth_service        PostgreSQL
    │                   │                    │                  │
    │── POST /login ────►│                   │                  │
    │                   │── validar_cpf() ──►│                  │
    │                   │                   │── SELECT usuario ►│
    │                   │                   │◄── usuario ───────│
    │                   │                   │── check_hash() ──►│(bcrypt)
    │                   │                   │── conta_ativa? ───│
    │                   │◄── ok / erro ──────│                  │
    │                   │                   │── INSERT audit ──►│
    │◄── redirect/erro ─│                   │                  │
```

### 6.2 Fluxo de Registro de Inscrição

```
Navegador       Blueprint        InscricaoService      Repositories      PostgreSQL
    │               │                   │                   │                │
    │─ POST /nova ──►│                  │                   │                │
    │               │── registrar() ───►│                   │                │
    │               │                  │── periodo_aberto? ►│                │
    │               │                  │                   │── SELECT ──────►│
    │               │                  │◄── periodo ────────│                │
    │               │                  │── existe_inscricao?►│               │
    │               │                  │                   │── SELECT ──────►│
    │               │                  │◄── não existe ─────│                │
    │               │                  │── buscar_ou_criar_responsavel()      │
    │               │                  │                   │── UPSERT ──────►│
    │               │                  │── buscar_ou_criar_crianca()          │
    │               │                  │                   │── UPSERT ──────►│
    │               │                  │── garantir_vinculo()                 │
    │               │                  │                   │── INSERT ──────►│
    │               │                  │── criar_inscricao()                  │
    │               │                  │                   │── INSERT ──────►│
    │               │                  │── registrar_audit()                  │
    │               │                  │                   │── INSERT ──────►│
    │               │◄── inscricao ─────│                   │                │
    │─◄ comprovante ─│                  │                   │                │
```

### 6.3 Fluxo de Recuperação de Senha

```
Navegador        Flask/auth        auth_service       SMTP         PostgreSQL
    │                │                  │               │               │
    │─ POST /recuperar►│                │               │               │
    │                │── solicitar() ──►│               │               │
    │                │                 │── SELECT user ►│──────────────►│
    │                │                 │── gerar_token()│               │
    │                │                 │── INSERT token►│──────────────►│
    │                │                 │── send_email() ►│              │
    │                │                 │               │── SMTP TLS ───►│(servidor)
    │◄── "e-mail enviado"               │               │               │
    │                                  │               │               │
    │─ GET /redefinir?token=XXX ───────►│               │               │
    │                │── validar_token()►│              │               │
    │                │                 │── SELECT token►│──────────────►│
    │                │                 │── expirado? ──►│               │
    │─ POST /redefinir ────────────────►│               │               │
    │                │── redefinir() ──►│               │               │
    │                │                 │── UPDATE hash ►│──────────────►│
    │                │                 │── invalidar_token              │
    │                │                 │── encerrar_sessoes             │
    │                │                 │── INSERT audit►│──────────────►│
    │◄── redirect login                 │               │               │
```

---

## 7. Visão de Deployment

### 7.1 Topologia de Produção

```
┌─────────────────────────────────────────────────────────┐
│                    Servidor de Produção                  │
│                    (Linux Ubuntu 22.04)                  │
│                                                         │
│  ┌──────────────────────────────────────────────────┐   │
│  │  Nginx (porta 443 / TLS)                         │   │
│  │  • Proxy reverso para Gunicorn                   │   │
│  │  • Serve arquivos estáticos diretamente          │   │
│  │  • Certificado TLS (Let's Encrypt ou municipal)  │   │
│  └────────────────────┬─────────────────────────────┘   │
│                       │ socket unix / porta 8000         │
│  ┌────────────────────▼─────────────────────────────┐   │
│  │  Gunicorn (WSGI)                                 │   │
│  │  • Workers: 2–4 (proporcional ao volume)         │   │
│  │  • Timeout: 60s                                  │   │
│  │  • Entry point: wsgi:app                         │   │
│  └────────────────────┬─────────────────────────────┘   │
│                       │ SQLAlchemy / psycopg2            │
│  ┌────────────────────▼─────────────────────────────┐   │
│  │  PostgreSQL 14                                   │   │
│  │  • Banco: sicrem_prod                            │   │
│  │  • Usuário de aplicação com permissões restritas │   │
│  │  • Backup diário automatizado                    │   │
│  └──────────────────────────────────────────────────┘   │
│                                                         │
│  ┌──────────────────────────────────────────────────┐   │
│  │  Systemd service: sicrem                         │   │
│  │  • Reinício automático em falha                  │   │
│  │  • Logs via journald                             │   │
│  └──────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
         │
         ▼ SMTP TLS
┌─────────────────┐
│ Servidor de     │
│ E-mail          │
│ (externo)       │
└─────────────────┘
```

### 7.2 Variáveis de Ambiente

```bash
# .env.example
SICREM_SECRET_KEY=<chave-aleatória-256-bits>
SICREM_DATABASE_URL=postgresql+psycopg2://usuario:senha@localhost/sicrem_prod
SICREM_MAIL_SERVER=smtp.exemplo.gov.br
SICREM_MAIL_PORT=587
SICREM_MAIL_USERNAME=sicrem@educacao.municipio.gov.br
SICREM_MAIL_PASSWORD=<senha-smtp>
SICREM_MAIL_USE_TLS=true
SICREM_MAX_LOGIN_ATTEMPTS=5
SICREM_TOKEN_EXPIRATION_HOURS=1
SICREM_ENV=production
```

### 7.3 Configuração por Ambiente

```python
# app/config.py
class Config:
    SECRET_KEY              = os.environ["SICREM_SECRET_KEY"]
    SQLALCHEMY_DATABASE_URI = os.environ["SICREM_DATABASE_URL"]
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER             = os.environ["SICREM_MAIL_SERVER"]
    MAIL_PORT               = int(os.environ.get("SICREM_MAIL_PORT", 587))
    MAIL_USE_TLS            = os.environ.get("SICREM_MAIL_USE_TLS", "true") == "true"
    MAIL_USERNAME           = os.environ["SICREM_MAIL_USERNAME"]
    MAIL_PASSWORD           = os.environ["SICREM_MAIL_PASSWORD"]
    MAX_LOGIN_ATTEMPTS      = int(os.environ.get("SICREM_MAX_LOGIN_ATTEMPTS", 5))
    TOKEN_EXPIRATION_HOURS  = int(os.environ.get("SICREM_TOKEN_EXPIRATION_HOURS", 1))

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://sicrem:sicrem@localhost/sicrem_dev"

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://sicrem:sicrem@localhost/sicrem_test"

class ProductionConfig(Config):
    DEBUG   = False
    TESTING = False

config = {
    "development": DevelopmentConfig,
    "testing":     TestingConfig,
    "production":  ProductionConfig,
}
```

### 7.4 Inicialização e Deploy

```bash
# Instalação de dependências
pip install -r requirements.txt

# Criação do banco e execução das migrations
flask db upgrade

# Seed inicial (definicoes_turma + primeiro Administrador)
flask seed run

# Execução em produção
gunicorn --workers 4 --bind unix:/run/sicrem.sock wsgi:app
```

---

## 8. Conceitos Transversais

### 8.1 Autenticação e Sessão

**Flask-Login** gerencia a sessão do usuário autenticado via cookie de sessão server-side assinado com `SECRET_KEY`. Não é utilizado JWT — sessão server-side é mais adequada para aplicações com server-side rendering e perfis com necessidade de invalidação imediata (bloqueio de conta).

```python
# app/models/usuario.py
from flask_login import UserMixin

class Usuario(db.Model, UserMixin):
    __tablename__ = "usuarios"
    cpf           = db.Column(db.String(11), primary_key=True)
    # ...

    def get_id(self):
        return self.cpf  # Flask-Login usa get_id() como identificador de sessão
```

### 8.2 Validação de CPF

```python
# app/utils/cpf.py
def validar_cpf(cpf: str) -> bool:
    """
    Valida CPF pelos dígitos verificadores.
    Utilizado em RF-009 (CPF da criança) e RF-010 (CPF do responsável).
    """
    cpf = "".join(filter(str.isdigit, cpf))
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False
    for i in range(2):
        soma  = sum(int(cpf[j]) * (10 + i - j) for j in range(9 + i))
        digito = (soma * 10 % 11) % 10
        if digito != int(cpf[9 + i]):
            return False
    return True
```

### 8.3 Geração do Número de Inscrição

```python
# app/services/inscricao_service.py
def gerar_numero_inscricao(ano_letivo: int) -> str:
    """
    Gera número sequencial no formato ANO + 5 dígitos (ex: 202600001).
    Utiliza SELECT FOR UPDATE para evitar race condition em acessos simultâneos.
    """
    from app.models.inscricao import Inscricao
    ultimo = (
        db.session.query(Inscricao)
        .filter(Inscricao.numero_inscricao.like(f"{ano_letivo}%"))
        .with_for_update()
        .order_by(Inscricao.numero_inscricao.desc())
        .first()
    )
    sequencia = int(ultimo.numero_inscricao[4:]) + 1 if ultimo else 1
    return f"{ano_letivo}{sequencia:05d}"
```

### 8.4 Geração de Comprovante PDF

```python
# app/services/comprovante_service.py
def gerar_comprovante(inscricao: Inscricao) -> bytes:
    """
    Gera PDF do comprovante protegido por senha = CPF da criança (só dígitos).
    RF-016.
    """
    # Renderiza HTML do comprovante via Jinja2
    html = render_template("comprovante/comprovante.html", inscricao=inscricao)

    # Converte HTML → PDF (WeasyPrint)
    pdf_bytes = HTML(string=html).write_pdf()

    # Protege com senha = CPF da criança (apenas dígitos)
    senha = "".join(filter(str.isdigit, inscricao.crianca_id))
    pdf_protegido = proteger_pdf(pdf_bytes, senha)

    return pdf_protegido
```

### 8.5 Auditoria Automática

O serviço de auditoria é chamado explicitamente nas camadas de serviço — não via signals ou middleware — para garantir rastreabilidade precisa por operação.

```python
# app/services/audit_service.py
from flask import request as current_request

def registrar(usuario, operacao: str, entidade: str,
              registro_id: str, payload_diff: dict = None) -> None:
    """
    Registra operação no audit_log. RF-021.
    Chamado explicitamente nas camadas de serviço.
    """
    log = AuditLog(
        usuario_id    = usuario.cpf,
        perfil_usuario= usuario.perfil,
        operacao      = operacao,
        entidade      = entidade,
        registro_id   = registro_id,
        payload_diff  = payload_diff,
        ip_origem     = current_request.remote_addr,
        dispositivo   = current_request.user_agent.string[:500],
    )
    db.session.add(log)
    # Não fazemos commit aqui — o commit é responsabilidade do serviço chamador
    # garantindo atomicidade entre a operação principal e o log
```

### 8.6 Tratamento de Erros

```python
# app/__init__.py
@app.errorhandler(403)
def acesso_negado(e):
    return render_template("erros/403.html", descricao=str(e)), 403

@app.errorhandler(404)
def nao_encontrado(e):
    return render_template("erros/404.html"), 404

@app.errorhandler(500)
def erro_interno(e):
    db.session.rollback()
    return render_template("erros/500.html"), 500
```

### 8.7 Migrações de Banco de Dados

**Flask-Migrate (Alembic)** gerencia as migrações. O DDL inicial é aplicado via migration, não diretamente — garantindo rastreabilidade de mudanças de schema ao longo do ciclo de vida do sistema.

```bash
flask db init       # apenas na inicialização do projeto
flask db migrate -m "schema inicial"
flask db upgrade    # aplica em produção
```

---

## 9. Decisões de Arquitetura

### DA-001 — Server-side rendering com Jinja2 em vez de SPA

**Contexto:** operadores sem perfil técnico, máquinas das unidades escolares sem garantia de performance, equipe de desenvolvimento enxuta.

**Decisão:** rendering server-side com Flask + Jinja2.

**Consequências positivas:** deploy simples, sem necessidade de build front-end, sem API REST separada, sem gerenciamento de estado client-side.

**Consequências negativas:** menor interatividade em comparação a SPAs — mitigado pela natureza sequencial e formulário-orientada do fluxo de inscrição.

---

### DA-002 — Sessão server-side em vez de JWT

**Contexto:** necessidade de invalidação imediata de sessão (bloqueio de conta, redefinição de senha).

**Decisão:** Flask-Login com sessão server-side assinada.

**Consequências positivas:** invalidação de sessão imediata e determinística. Sem necessidade de blacklist de tokens.

**Consequências negativas:** estado de sessão no servidor — sem impacto prático dado o volume (máx. 14 sessões simultâneas).

---

### DA-003 — Auditoria explícita na camada de serviço

**Contexto:** necessidade de rastreabilidade precisa por operação, com `payload_diff` específico por tipo de alteração.

**Decisão:** `audit_service.registrar()` é chamado explicitamente em cada serviço, não via middleware ou signals.

**Consequências positivas:** controle preciso sobre o que é auditado e como. Payload de diff estruturado por contexto.

**Consequências negativas:** risco de esquecer a chamada em novos serviços — mitigado por testes de integração que verificam presença de log para cada operação coberta pelo SRS.

---

### DA-004 — `SELECT FOR UPDATE` na geração de número de inscrição

**Contexto:** múltiplos operadores simultâneos podem gerar inscrições no mesmo instante, criando race condition na geração de `numero_inscricao`.

**Decisão:** `SELECT FOR UPDATE` na query que busca o último número do período.

**Consequências positivas:** garante unicidade do número de inscrição sem necessidade de sequence separada.

**Consequências negativas:** lock de linha durante a transação — impacto desprezível dado o volume máximo de 14 operadores simultâneos.

---

### DA-005 — Commit atômico entre operação principal e audit_log

**Contexto:** se a operação principal (INSERT em `inscricoes`) for commitada mas o audit_log falhar, o sistema fica com dado sem rastreabilidade.

**Decisão:** operação principal e inserção no `audit_log` ocorrem na mesma transação. O commit é único, na camada de serviço chamadora.

**Consequências positivas:** atomicidade garantida — ou ambos são commitados ou nenhum é.

**Consequências negativas:** `audit_service.registrar()` não faz commit próprio — requer disciplina na camada de serviço. Documentado como convenção obrigatória.

---

## 10. Requisitos de Qualidade

### 10.1 Cenários de Qualidade

| ID | Atributo | Cenário | Resposta esperada |
|----|---------|---------|-------------------|
| Q-001 | Integridade | Operador tenta registrar segunda inscrição para o mesmo CPF no mesmo período | Sistema rejeita com mensagem clara, sem criar registro |
| Q-002 | Segurança | Usuário tenta acessar inscrições de outra unidade via URL direta | Sistema retorna 403 e registra tentativa no audit_log |
| Q-003 | Rastreabilidade | Auditor solicita histórico de alterações de uma inscrição específica | Sistema retorna todos os eventos U com payload_diff para aquela inscrição |
| Q-004 | Usabilidade | Operador seleciona turma incompatível com a faixa etária da criança | Sistema bloqueia a seleção e exibe mensagem explicativa com a faixa correta |
| Q-005 | Disponibilidade | Conexão com banco cai durante preenchimento do formulário | Sistema exibe mensagem clara ao operador antes de qualquer perda de dados |
| Q-006 | Manutenibilidade | Desenvolvedor precisa adicionar novo campo ao formulário de inscrição | Alteração limitada a: migration Alembic + modelo SQLAlchemy + template Jinja2 |

---

## 11. Riscos Técnicos

| ID | Risco | Probabilidade | Impacto | Mitigação |
|----|-------|:---:|:---:|-----------|
| RT-001 | Queda de internet na unidade durante atendimento | Média | Alto | Mensagem clara ao operador; formulário não perde dados preenchidos |
| RT-002 | Race condition na geração de número de inscrição | Baixa | Médio | `SELECT FOR UPDATE` + constraint `UNIQUE` no banco |
| RT-003 | Falha no servidor SMTP impede recuperação de senha | Baixa | Médio | Fluxo de suporte hierárquico documentado como fallback |
| RT-004 | Vazamento de dados sensíveis por erro de controle de acesso | Baixa | Alto | RBAC em todas as rotas via decorator; testes de integração cobrindo 403 |
| RT-005 | Corrupção do audit_log por falha de transação | Muito baixa | Alto | Commit atômico entre operação e log; `RULE` de proteção no banco |
| RT-006 | Seed de `definicoes_turma` incorreto gera sugestão de turma errada | Baixa | Médio | Revisão do seed com Secretaria Municipal antes da implantação |

---

## 12. Glossário Técnico

| Termo | Definição |
|-------|-----------|
| Application Factory | Padrão Flask onde a instância da aplicação é criada por uma função `create_app()`, facilitando testes e múltiplos ambientes |
| Blueprint | Módulo Flask que agrupa rotas, templates e recursos relacionados |
| Gunicorn | Servidor WSGI Python para execução em produção |
| Nginx | Servidor web/proxy reverso — responsável por TLS e servir arquivos estáticos |
| SQLAlchemy | ORM Python que mapeia classes Python a tabelas do banco de dados |
| Alembic / Flask-Migrate | Ferramenta de migração de schema de banco de dados para SQLAlchemy |
| Flask-Login | Extensão Flask para gerenciamento de sessão de usuário autenticado |
| WSGI | Web Server Gateway Interface — protocolo de comunicação entre servidor web e aplicação Python |
| Jinja2 | Engine de templates Python integrada ao Flask |
| psycopg2 | Driver Python para PostgreSQL |
| WeasyPrint | Biblioteca Python para geração de PDF a partir de HTML/CSS |
| bcrypt | Algoritmo de hash de senha com fator de custo configurável |
| SELECT FOR UPDATE | Instrução SQL que aplica lock de linha durante uma transação |
| TIMESTAMPTZ | Tipo PostgreSQL que armazena timestamp com fuso horário (UTC internamente) |
| RULE | Mecanismo PostgreSQL que intercepta e substitui operações DML em uma tabela |

---

*Documento gerado a partir do SRS IEEE 830 v1.0, PRD v2.0, modelagem DBML v3 e DDL PostgreSQL v1.0.*  
*Próximos artefatos previstos: Manual de Implantação, documento de infraestrutura e SLA, formato livre para comunicação institucional.*
