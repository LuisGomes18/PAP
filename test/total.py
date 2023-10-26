import psutil


ram_info = psutil.virtual_memory()

PERCENTAGEM_CPU = psutil.cpu_percent(interval=1)
RAM_USADA = ram_info.used / (1024 ** 3)  # Convert RAM used to GB
RAM_TOTAL = ram_info.total / (1024 ** 3)  # Convert total RAM to GB
RAM_NECESSARIA = 0.4 # 400 MB to GB

if RAM_TOTAL - RAM_USADA > RAM_NECESSARIA and PERCENTAGEM_CPU < 80:
    print('Rodando o server')
elif RAM_TOTAL - RAM_USADA >= RAM_NECESSARIA:
    print('RAM necessária indisponível. Por favor, feche aplicativos desnecessários.')
elif PERCENTAGEM_CPU >= 80:
    print('Porcentagem de CPU mais alta do que o necessário.')
else:
    exit('Erro ao rodar o server', 1) # type: ignore
