import os


diretorio_base_usuario = os.path.expanduser("~")

diretorios = ["Desktop", "Documentos", "Música", "Imagens", "Vídeos", "Transferências"]
pasta_alvo = "PAP"
caminho_pasta_alvo = None

for diretorio in diretorios:
    caminho = os.path.join(diretorio_base_usuario, diretorio, pasta_alvo)
    if os.path.exists(caminho) and os.path.isdir(caminho):
        caminho_pasta_alvo = caminho
        break

caminho_ficheiros = [ 
    # Add novos caminhos caso necessarios
    f"{caminho_pasta_alvo}/PAP_Com_Server/static",
    f"{caminho_pasta_alvo}/PAP_Com_Server/templates",
    f"{caminho_pasta_alvo}/PAP_Com_Server/templates/index.html"
]

for item in caminho_ficheiros:
    if os.path.exists(item):
        print(f'O diretório {item} existe.')
    else:
        print(f'O diretório {item} não existe.')
