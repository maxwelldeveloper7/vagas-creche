""" Definição de rotas"""
from flask import render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from app import app, get_db_connection

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        cpf = request.form['cpf']
        senha = request.form['senha']
        senha_hash = generate_password_hash(senha) # Implementação de Hashing de senhas
        nome = request.form['nome']
        telefone = request.form['telefone']
        email = request.form['email']
        endereco = request.form['endereco']
        bairro = request.form['bairro']
        ponto_referencia = request.form['ponto_referencia']
        endereco_trabalho = request.form['endereco_trabalho']
        bairro_trabalho = request.form['bairro_trabalho']

        conn = get_db_connection()
        conn.execute('INSERT INTO usuarios (cpf, senha, nome, telefone, email, endereco, bairro, ponto_referencia, endereco_trabalho, bairro_trabalho) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                    (cpf, senha_hash, nome, telefone, email, endereco, bairro, ponto_referencia, endereco_trabalho, bairro_trabalho))
        conn.commit()
        conn.close()
        flash('Usuário registrado com sucesso!')
        return redirect(url_for('index'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        cpf = request.form['cpf']
        senha = request.form['senha']

        conn = get_db_connection()
        user = conn.execute('SELECT * FROM usuarios WHERE cpf = ?', (cpf,)).fetchone()
        conn.close()

        if user and check_password_hash(user['senha'], senha): # Decripta o rash da senha e verifica se está correta
            print('login realizado')
            flash('Login realizado com sucesso!')
            return redirect(url_for('index'))
        else:
            flash('CPF ou senha incorretos.')

    return render_template('login.html')