""" Definição de rotas"""
import logging
import sqlite3
from flask import render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from app import app, get_db_connection

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # filtra e remove os caracteres da máscara
        nome = request.form['nome']
        cpf = ''.join(filter(str.isdigit, request.form['cpf']))
        # filtra e remove os caracteres da máscara
        telefone = ''.join(filter(str.isdigit, request.form['telefone']))
        # senha = request.form['senha']
        # # Implementação de Hashing de senhas
        # senha_hash = generate_password_hash(senha)
        email = request.form['email']
        # endereco = request.form['endereco']
        # bairro = request.form['bairro']
        # ponto_referencia = request.form['ponto_referencia']
        # endereco_trabalho = request.form['endereco_trabalho']
        # bairro_trabalho = request.form['bairro_trabalho']

        conn = get_db_connection()
        try:
            conn.execute('INSERT INTO usuarios (nome, cpf, telefone, email) VALUES (?, ?, ?, ?)',
                        (nome, cpf, telefone, email))
            conn.commit()
            return redirect(url_for('index'))
        except sqlite3.IntegrityError:
            flash('CPF já cadastrado. Tente novamente.')
        except Exception as e:
            logging.error(f'Error occurred: {e}')
            flash('Ocorreu um erro no servidor. Tente novamente mais tarde.')
        finally:
            # Fecha a conexão com o banco de dados
            conn.close()        

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        cpf = ''.join(filter(str.isdigit, request.form['cpf'])) # filtra e remove os pontos e traço da máscara
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
