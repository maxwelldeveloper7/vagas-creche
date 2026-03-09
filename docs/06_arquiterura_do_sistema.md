Considerando o cenário informado — **até 12 acessos simultâneos**, uso interno administrativo e infraestrutura simples — a escolha por uma **arquitetura monolítica baseada em Flask** é tecnicamente adequada.

Essa abordagem segue o princípio de **simplicidade arquitetural** recomendado em projetos de pequeno porte por **Karl Wiegers**, evitando complexidade desnecessária como microsserviços ou APIs desacopladas.

A seguir está a **definição arquitetural formal do sistema**.

---

# Arquitetura do Sistema

## Tipo de Arquitetura

Arquitetura **Monolítica Web MVC**.

Características:

* aplicação única
* backend responsável por lógica e renderização
* comunicação direta com banco de dados
* sem camada de API externa

---

# Visão Geral da Arquitetura

```
Usuário
   │
Navegador Web
(HTML + CSS + JavaScript)
   │
Servidor Web
Flask Application
   │
Camada de Negócio
   │
Camada de Persistência
(PostgreSQL)
```

---

# Stack Tecnológica

| Camada         | Tecnologia        |
| -------------- | ----------------- |
| Frontend       | HTML5             |
| Estilo         | CSS3              |
| Interatividade | JavaScript        |
| Backend        | Flask             |
| ORM            | SQLAlchemy        |
| Banco de Dados | PostgreSQL        |
| Servidor       | Gunicorn ou uWSGI |
| Proxy reverso  | Nginx             |

---

# Estrutura de Diretórios Recomendada

Uma organização simples e adequada para Flask.

```
sistema-creche/

app/
│
├── __init__.py
├── config.py
├── extensions.py
│
├── models/
│   ├── usuario.py
│   ├── unidade_escolar.py
│   ├── responsavel.py
│   ├── crianca.py
│   └── inscricao.py
│
├── routes/
│   ├── auth_routes.py
│   ├── inscricao_routes.py
│   ├── consulta_routes.py
│   └── relatorio_routes.py
│
├── services/
│   ├── inscricao_service.py
│   ├── pdf_service.py
│   └── relatorio_service.py
│
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── dashboard.html
│   ├── inscricao/
│   │   ├── iniciar.html
│   │   ├── responsavel.html
│   │   ├── crianca.html
│   │   └── conferencia.html
│   │
│   └── consulta/
│
├── static/
│   ├── css/
│   ├── js/
│   └── img/
│
└── utils/
    ├── auth.py
    ├── validators.py
    └── helpers.py


migrations/

run.py
requirements.txt
```

---

# Padrão Arquitetural Interno

Aplicação seguirá **MVC adaptado ao Flask**.

| Camada    | Responsabilidade            |
| --------- | --------------------------- |
| Routes    | Controladores HTTP          |
| Services  | Lógica de negócio           |
| Models    | Entidades e acesso ao banco |
| Templates | Interface HTML              |

---

# Fluxo de Requisição

Exemplo: **registro de inscrição**

```
Navegador
   │
HTTP Request
   │
Flask Route
   │
Service Layer
   │
Model (SQLAlchemy)
   │
PostgreSQL
   │
Response
   │
Template HTML renderizado
```

---

# Módulos do Sistema

## 1. Autenticação

Responsável por:

* login
* logout
* controle de sessão
* verificação de perfil

---

## 2. Gestão de Estrutura Escolar

Permite:

* cadastro de unidades escolares
* cadastro de diretores
* cadastro de secretários

---

## 3. Módulo de Inscrição

Fluxo:

1. iniciar inscrição
2. verificar CPF da criança
3. cadastrar responsável
4. cadastrar criança
5. conferir dados
6. salvar inscrição
7. gerar comprovante

---

## 4. Consulta de Inscrições

Permite:

* buscar por CPF
* buscar por nome
* visualizar inscrição
* reemitir comprovante

---

## 5. Relatórios

Relatórios disponíveis:

* lista geral de inscritos
* inscritos por unidade
* inscritos por faixa etária
* inscritos por critérios sociais

Exportação:

* CSV

---

# Segurança

### Senhas

Armazenamento usando:

```
bcrypt
```

---

### Sessão

Controle de sessão via:

```
Flask-Login
```

---

### Controle de Acesso

Implementação de **RBAC simples**.

Perfis:

```
administrador
diretor
secretario
```

---

# Estratégia de Deploy

Arquitetura recomendada:

```
Nginx
   │
Gunicorn
   │
Flask App
   │
PostgreSQL
```

---

# Capacidade de Escala

O sistema suporta facilmente:

* 10 a 20 usuários simultâneos
* consultas administrativas
* geração de relatórios

Caso a demanda aumente futuramente:

* separar frontend
* criar API
* migrar para arquitetura de serviços

---

# Dependências Python

Exemplo de `requirements.txt`:

```
Flask
Flask-Login
Flask-Migrate
Flask-SQLAlchemy
psycopg2-binary
bcrypt
reportlab
python-dotenv
```

---

# Geração do Comprovante PDF

Biblioteca recomendada:

```
ReportLab
```

Características:

* geração dinâmica
* criptografia por senha
* senha = CPF da criança

---

# Logs e Auditoria

Registros importantes:

* login de usuários
* criação de inscrições
* reemissão de comprovantes

---

# Conclusão Arquitetural

A arquitetura definida apresenta:

* **baixa complexidade**
* **alta manutenibilidade**
* **adequação ao volume de uso**
* **facilidade de implantação**

É uma solução apropriada para um **sistema administrativo municipal de pequeno porte**.
