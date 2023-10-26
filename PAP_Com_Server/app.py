import sys
import os
from os import path
from psutil import virtual_memory
from psutil import cpu_percent
import platform

from os import urandom
from flask import Flask
from flask import render_template

def verificacao():
    os.system('clear')
    sistema_operacional = platform.system()
    if sistema_operacional == "Windows":
        pass
    elif sistema_operacional == "Linux":
        verificacao_linux()

def verificacao_linux():
    ram_info = virtual_memory()

    PERCENTAGEM_CPU = cpu_percent(interval=1)
    RAM_USADA = ram_info.used / (1024 ** 3)
    RAM_TOTAL = ram_info.total / (1024 ** 3)
    RAM_NECESSARIA = 0.3

    if RAM_TOTAL - RAM_USADA > RAM_NECESSARIA and PERCENTAGEM_CPU < 80:
        print('\n\nTeste de CPU e RAM passado')
    elif RAM_TOTAL - RAM_USADA >= RAM_NECESSARIA:
        print('\n\nRAM necessária indisponível. Por favor, feche aplicativos desnecessários.')
        sys.exit(1)
    elif PERCENTAGEM_CPU >= 80:
        print('\n\nPorcentagem de CPU mais alta do que o necessário.')
        sys.exit(1)
    else:
        sys.exit(1)

    caminho = os.getcwd()
    pastas_verificar = [
        path.join(caminho, "PAP_Com_Server/static"),
        path.join(caminho, "PAP_Com_Server/templates"),
        path.join(caminho, "PAP_Com_Server/templates/index.html")
    ]

    for item in pastas_verificar:
        if path.exists(item):
            pass
        else:
            print(f'{item} não existe. Por favor, crie a pasta/ficheiro\n\n')
            exit(1)

    print('Teste de ficheiros passado\n\n')


if __name__ == '__main__':
    verificacao() 

    app = Flask(__name__, static_url_path='/static')
    app.secret_key = urandom(24)

    @app.route('/')
    def index():
        '''Renderiza a pagina index'''
        return render_template('index.html')

    app.run(host='0.0.0.0', port=5000)  # Inicie o servidor Flask após a verificação
