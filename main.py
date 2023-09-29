'''
Flask: Modulo para criar aplicacoes web
'''
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session


app = Flask(__name__, static_url_path='/static')

app.secret_key = 'luismelhor'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pagina_inicial')
def pagina_inicial():
    return render_template('pagina_inicial/index.html')

@app.route('/sem_acesso')
def sem_acesso():
    return render_template('sem_acesso/index.html')

def is_valid_login(username, password):
    if username == "luisgomes" and password == "luis":
        return True
    elif username == "colorad" and password == "colorad":
        return True
    else:
        return False

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if is_valid_login(username, password):
            session['username'] = username
            return redirect(url_for('area_de_utilizador'))
        return 'Invalid username or password'

    return render_template('login/index.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/area_de_utilizador')
def area_de_utilizador():
    return render_template('area_de_utilizador/index.html')

@app.route('/aviso_escola')
def aviso_escola():
    return render_template('aviso_escola/index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
