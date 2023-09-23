'''
Flask: Modulo para criar aplicacoes web
'''
from flask import Flask # pylint: disable=import-error
from flask import render_template # pylint: disable=import-error


app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    '''Rederiza a pagina index'''
    return render_template('index.html')

@app.route('/sem_acesso')
def sem_acesso():
    '''Rederiza a pagina sem_acesso'''
    return render_template('sem_acesso/index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
