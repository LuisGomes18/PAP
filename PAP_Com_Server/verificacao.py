"""
Este módulo realiza verificações de recursos do sistema e valida pastas e arquivos.
"""
import sys
from os import system, path
from psutil import virtual_memory, cpu_percent
import platform

sistema_operacional = platform.system()

if sistema_operacional == "Windows":
    exit(0)
elif sistema_operacional == "Linux":
    pass

system('clear')

def verificacao():
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
        sys.exit(1)  # Exit com código de erro

    caminho_base = path.expanduser("~")
    pastas = ["Desktop", "Documentos", "Música", "Imagens", "Vídeos", "Transferências"]
    PASTA_ALVO = "PAP"
    CAMINHO_PASTA_ALVO = ""  # Inicialize com uma string vazia
    pastas_verificar = [
        path.join(CAMINHO_PASTA_ALVO, "PAP_Com_Server/static"),
        path.join(CAMINHO_PASTA_ALVO, "PAP_Com_Server/templates"),
        path.join(CAMINHO_PASTA_ALVO, "PAP_Com_Server/templates/index.html")
    ]

    for pasta in pastas:
        caminho = path.join(caminho_base, pasta, PASTA_ALVO)
        if path.exists(caminho) and path.isdir(caminho):
            CAMINHO_PASTA_ALVO = caminho
            break

    for item in pastas_verificar:
        if not path.exists(item):
            print(f'{item} não existe. Por favor, crie a pasta ou arquivo.\n\n')
            sys.exit(1)
    print('Teste  de ficheiros passado\n\n')

verificacao()
