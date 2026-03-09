# Estrutura Profissional do Projeto

```
vagas-creche/
│
├── app/
│   ├── __init__.py
│   ├── config.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── usuario.py
│   │   ├── unidade.py
│   │   ├── responsavel.py
│   │   ├── crianca.py
│   │   └── inscricao.py
│   │
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth_routes.py
│   │   ├── inscricao_routes.py
│   │   ├── consulta_routes.py
│   │   └── relatorio_routes.py
│   │
│   ├── services/
│   │   ├── auth_service.py
│   │   ├── inscricao_service.py
│   │   └── relatorio_service.py
│   │
│   ├── templates/
│   │   ├── base.html
│   │   ├── login.html
│   │   ├── dashboard.html
│   │   │
│   │   ├── inscricoes/
│   │   │   ├── nova_inscricao.html
│   │   │   ├── cadastro_responsavel.html
│   │   │   ├── cadastro_crianca.html
│   │   │   ├── conferencia.html
│   │   │   └── comprovante.html
│   │   │
│   │   ├── consultas/
│   │   │   └── consulta_inscricoes.html
│   │   │
│   │   └── relatorios/
│   │       └── relatorios.html
│   │
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   │
│   │   ├── js/
│   │   │   └── main.js
│   │   │
│   │   └── img/
│   │
│   ├── utils/
│   │   ├── pdf_generator.py
│   │   ├── security.py
│   │   └── validators.py
│   │
│   └── database.py
│
├── migrations/
│
├── run.py
│
├── requirements.txt
│
└── README.md
```

---

# Arquivo Principal da Aplicação

## run.py

```python
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
```

---

# Inicialização da Aplicação

## app/**init**.py

```python
from flask import Flask
from .config import Config
from .database import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from .routes.auth_routes import auth_bp
    from .routes.inscricao_routes import inscricao_bp
    from .routes.consulta_routes import consulta_bp
    from .routes.relatorio_routes import relatorio_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(inscricao_bp)
    app.register_blueprint(consulta_bp)
    app.register_blueprint(relatorio_bp)

    return app
```

---

# Configuração do Sistema

## config.py

```python
import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY","chave_secreta")

    SQLALCHEMY_DATABASE_URI = "postgresql://usuario:senha@localhost/creche_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```

---

# Conexão com o Banco

## database.py

```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
```

---

# Exemplo de Modelo

## models/crianca.py

```python
from app.database import db

class Crianca(db.Model):

    __tablename__ = "criancas"

    id = db.Column(db.Integer, primary_key=True)

    nome = db.Column(db.String(150), nullable=False)

    data_nascimento = db.Column(db.Date, nullable=False)

    cpf = db.Column(db.String(14), unique=True, nullable=False)

    nome_pai = db.Column(db.String(150))

    nome_mae = db.Column(db.String(150))
```

---

# Exemplo de Rota

## routes/auth_routes.py

```python
from flask import Blueprint, render_template, request, redirect

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/")
def login():
    return render_template("login.html")
```

---

# Serviço de Inscrição

## services/inscricao_service.py

Responsável pela lógica de negócio.

```python
def verificar_cpf_existente(cpf, db):
    from app.models.crianca import Crianca
    return db.session.query(Crianca).filter_by(cpf=cpf).first()
```

---

# Geração de Comprovante

## utils/pdf_generator.py

Pode utilizar biblioteca **reportlab**.

```python
from reportlab.pdfgen import canvas

def gerar_pdf(nome_crianca, numero_inscricao):

    arquivo = f"comprovante_{numero_inscricao}.pdf"

    pdf = canvas.Canvas(arquivo)

    pdf.drawString(100,750,"Comprovante de Inscrição")

    pdf.drawString(100,720,f"Criança: {nome_crianca}")

    pdf.drawString(100,700,f"Número: {numero_inscricao}")

    pdf.save()

    return arquivo
```

---

# Arquivo de Dependências

## requirements.txt

```
Flask
Flask-SQLAlchemy
psycopg2-binary
reportlab
python-dotenv
bcrypt
```

---

# Fluxo Geral do Sistema

```
Usuário acessa sistema
        │
        ▼
Login
        │
        ▼
Painel
        │
        ▼
Nova inscrição
        │
        ├── cadastro responsável
        ├── cadastro criança
        │
        ▼
Conferência
        │
        ▼
Registro da inscrição
        │
        ▼
Geração do comprovante PDF
```

---

# Benefícios dessa Estrutura

Essa arquitetura:

* mantém **separação entre rotas, modelos e lógica**
* facilita manutenção
* facilita testes
* permite expansão futura

Também segue padrões comuns em projetos Flask de médio porte.
