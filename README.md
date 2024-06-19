# Cadastro de Creches

![Python](https://img.shields.io/badge/Python-3.0-blue)
![Flask](https://img.shields.io/badge/Flask-3.0.3-blue)
![SQLite](https://img.shields.io/badge/SQLite-3.0-blue)
![HTML](https://img.shields.io/badge/HTML-5-blue)
![CSS](https://img.shields.io/badge/CSS-3-blue)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-blue)

## Descrição

O sistema de Cadastro de Creches é uma aplicação web desenvolvida para a Secretaria Municipal de Educação de Nanuque, com o objetivo de facilitar o registro online de inscrições em creches. Este projeto foi desenvolvido utilizando Python com Flask para o backend e SQLite para o banco de dados. O frontend foi construído utilizando HTML, CSS e JavaScript.

## Funcionalidades

- Cadastro de Usuários: Permite o registro de usuários com CPF e senha segura (hashing).
- Login de Usuários: Autenticação de usuários utilizando CPF e senha.
- Cadastro de Crianças: Formulário para cadastro de crianças para vagas em creches.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para o desenvolvimento do backend.
- **Flask**: Micro framework web utilizado para criar a aplicação web.
- **SQLite**: Banco de dados utilizado para armazenar informações de usuários e inscrições.
- **HTML/CSS/JavaScript**: Tecnologias utilizadas para construir o frontend da aplicação.

## Estrutura do Projeto

```plaintext
cadastro-creches/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   └── templates/
│       ├── index.html
│       ├── register.html
│       └── login.html
│
├── static/
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── script.js
│
├── venv/
│   └── ... (arquivos do ambiente virtual)
│
├── run.py
├── init_db.py
└── schema.sql```

## Configuração e Execução

### Pré-requisitos

- Python 3.x
- pip (Python package installer)
- virtualenv

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/maxwelldeveloper7/cadastro-creches.git
   cd cadastro-creches
   ```

2. **Crie e ative um ambiente virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Inicialize o banco de dados:**
   ```bash
   python init_db.py
   ```

5. **Execute a aplicação:**
   ```bash
   python run.py
   ```

6. **Acesse a aplicação:**
   - Abra o navegador e acesse `http://127.0.0.1:5000`.

## Segurança de Senhas

As senhas dos usuários são armazenadas de forma segura utilizando a função de hashing do `werkzeug.security`. Isso garante que as senhas sejam protegidas contra acessos não autorizados.

## Contribuição

Sinta-se à vontade para contribuir com este projeto. Faça um fork do repositório, crie uma branch para suas alterações, e envie um pull request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).