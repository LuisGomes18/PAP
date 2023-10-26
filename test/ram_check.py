import psutil
import os
import subprocess

ram_info = psutil.virtual_memory()
RAM_BYTES_USADA = ram_info.used
RAM_BYTES_TOTAL = ram_info.total
RAM_NECESSARIA = 0.512  # 512 MB
resto = (RAM_BYTES_TOTAL - RAM_BYTES_USADA) / (1024 ** 3)

venv_path = "../PAP/.venv"

try:
    if resto < RAM_NECESSARIA:
        print('Server não pode ser rodado')
    else:
        print('Rodando o server')
        """"
        if os.name == 'posix':  # Verifica se está em um sistema Unix (Linux, macOS)
            activar_script = os.path.join(venv_path, "bin", "activate")
            subprocess.run(f"source {activar_script} && python /home/luis/Desktop/PAP/PAP_Com_Server/app.py", shell=True, text=True, check=True, executable="/bin/bash")
        elif os.name == 'nt':  # Verifica se está no Windows
            activate_script = os.path.join(venv_path, "Scripts", "activate")
            subprocess.run(f"{activate_script} && python C:\\Users\\luis\\Desktop\\PAP\\PAP_Com_Server\\app.py", shell=True, text=True, check=True, executable="cmd")
        """
except Exception as e:
    exit(f'Erro ao rodar o servidor: {e}', 1)
