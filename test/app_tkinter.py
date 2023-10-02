from json import loads, dumps
from json import JSONDecodeError
from tkinter import *
from tkinter import ttk

def ativar_manutencao():
    dados['manutencao'] = True
    salvar_dados()
    label_estado.config(text="Manutenção Ativada")
    button_manutencao.config(text="Desativar Manutenção", command=desativar_manutencao)

def desativar_manutencao():
    dados['manutencao'] = False
    salvar_dados()
    label_estado.config(text="Manutenção Desativada")
    button_manutencao.config(text="Ativar Manutenção", command=ativar_manutencao)

def salvar_dados():
    with open('Dados/dados.json', 'w', encoding='utf-8') as dd:
        dd.write(dumps(dados))

try:
    with open('Dados/dados.json', 'r', encoding='utf-8') as dd:
        conteudo_json = dd.read()
        dados = loads(conteudo_json)
except JSONDecodeError:
    print('Erro na formatação do .json')
    exit(1)
except FileNotFoundError:
    print('Arquivo não encontrado!')
    exit(1)
except Exception as erro:
    print(f"Ocorreu um erro: {str(erro)}")
    exit(1)


root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Label(frm, text="Ativar/Desativar Manutenção").grid(row=0, column=0, columnspan=2)
label_estado = ttk.Label(frm, text="")
if dados['manutencao'] == False:
    label_estado.config(text="Manutenção Desativada")
button_manutencao = ttk.Button(frm, text="", command=ativar_manutencao if not dados['manutencao'] else desativar_manutencao)
button_manutencao.grid(row=1, column=0, columnspan=2)

ttk.Button(frm, text="Quit", command=root.destroy).grid(row=2, column=0, columnspan=2)

root.mainloop()
