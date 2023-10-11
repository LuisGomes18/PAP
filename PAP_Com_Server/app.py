'''
Flask: Modulo para criar aplicacoes web
'''
from os import urandom

from flask import Flask
from flask import render_template


app = Flask(__name__, static_url_path='/static')
app.secret_key = urandom(24)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
