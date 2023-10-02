'''
Flask: Modulo para criar aplicacoes web
'''
from os import urandom
import tkinter as tk
import json

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session

app = Flask(__name__, static_url_path='/static')

IPS_PERMITIDOS = ["192.168.1.36", "192.168.1.21"] # Portatil e MSI
MANUTENCAO = False

app.secret_key = urandom(24)

users = {
    'luisgomes': 'luis',
    'colorad': 'colorad'
}

@app.errorhandler(404)
def not_found_error(error):
    return render_template('nao_encontrado/index.html'), 404

@app.before_request
def verificar_modo_manutencao():
    ip_cliente = request.remote_addr
    if MANUTENCAO:
        if ip_cliente not in IPS_PERMITIDOS:
            return "O servidor está em manutenção. Tente novamente mais tarde.", 503

@app.route('/ativar_manutencao')
def ativar_manutencao():
    global MANUTENCAO
    MANUTENCAO = True
    return "Modo de manutenção ativado."

@app.route('/desativar_manutencao')
def desativar_manutencao():
    global MANUTENCAO
    MANUTENCAO = False
    return "Modo de manutenção desativado"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pagina_inicial')
def pagina_inicial():
    return render_template('pagina_inicial/index.html')

@app.route('/sem_acesso')
def sem_acesso():
    return render_template('sem_acesso/index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('area_de_utilizador'))
        else:
            return 'Credenciais Invalidas. <a href="/login">Tente Novamente</a>'
    return render_template('login/index.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/area_de_utilizador')
def area_de_utilizador():
    if 'username' in session:
        return render_template('area_de_utilizador/index.html')
    return 'Voçe não esta logado. <a href="/login">Faça Login </a>'

@app.route('/aviso_escola')
def aviso_escola():
    return render_template('aviso_escola/index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
