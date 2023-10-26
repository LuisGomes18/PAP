import psutil


cpu_percent = psutil.cpu_percent(interval=1)
print(f'Uso de cpu: {cpu_percent}%')

try:
    if cpu_percent > 80:
        print('Impossivel rodar server')
    else:
        print('Rodar server')
except Exception as e:
    exit(f'Erro ao rodar o servidor: {e}', 1)
