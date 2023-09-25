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
    '''Rederiza a pagina index'''
    return render_template('index.html')

@app.route('/sem_acesso')
def sem_acesso():
    '''Rederiza a pagina sem_acesso'''
    return render_template('sem_acesso/index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    '''Renders the login page and handles login logic.'''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if is_valid_login(username, password):
            session['username'] = username
            return redirect(url_for('home')) 
        return 'Invalid username or password'

    return render_template('login/index.html')

def is_valid_login(username, password):
    '''Valida o login'''
    return username == "luisgomes" and password == "luis"

@app.route('/home')
def home():
    '''Rederiza a pagina home'''
    return render_template('home/index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
