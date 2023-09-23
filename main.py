'''
flask: Modulo de que permite criar um servidor web
'''
from flask import Flask # pylint: disable=import-error
from flask import render_template # pylint: disable=import-error

app = Flask(__name__)

@app.route('/')
def index():
    '''Função que retorna a pagina index.html'''
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
