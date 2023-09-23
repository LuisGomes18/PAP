'''
Module for the main page of the website.
'''
from flask import Flask # pylint: disable=import-error
from flask import render_template # pylint: disable=import-error


app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    '''Renders the index page'''
    return render_template('index.html')

@app.route('/sem_acesso')
def sem_acesso():
    '''Renders the sem_acesso page'''
    return render_template('sem_acesso/index.html')

if __name__ == '__main__':
    app.run(debug=True)
