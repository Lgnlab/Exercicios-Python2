#Exercício 18
#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
#calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

arquivo = float(input('Tamanho Arquivo(MB): '))
velocidade = float(input('Velocidade Da Internet(Mbps): '))
calculo = arquivo * 8           #Converter para mb
tempo = calculo / velocidade        #Tempo em segundos
print(f'O tempo vai ser de {tempo / 60:.0f} minuto')