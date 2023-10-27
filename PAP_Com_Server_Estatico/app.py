'''
Platform: Recolher o sistema do usuario
OS: Para uso do terminal e dos caminhos e gerar token do server
PSUTIL: Recolher dados da CPU e RAM do pc
SYS: Para fazer saidas do terminal
FLASK: Para fazer o server HTML 
'''
import platform
from os import system
from psutil import virtual_memory
from psutil import cpu_percent
import sys
from os import getcwd
from os import path

from os import urandom
from flask import Flask
from flask import render_template

def apagar_terminal():
    sistema_operacional = platform.system()
    if sistema_operacional == "Windows":
        system('cls')
    elif sistema_operacional == "Linux":
        system('clear')

def verificacao():
    apagar_terminal()
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

    caminho = getcwd()
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

    app = Flask(__name__)
    app.secret_key = urandom(24)

    @app.route('/')
    def index():
        '''Renderiza a pagina index'''
        return render_template('index.html')

    app.run(host='0.0.0.0', port=5000)