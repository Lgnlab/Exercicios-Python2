arquivo = float(input('Tamanho Arquivo(MB): '))
velocidade = float(input('Velocidade Da Internet(Mbps): '))
calculo = arquivo * 8           #Converter para mb
tempo = calculo / velocidade        #Tempo em segundos
print(f'O tempo vai ser de {tempo / 60:.0f} minuto')