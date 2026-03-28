#Exercício 13
#Tendo como dados de entrada um arquivo em Gigabytes, construa um algoritmo que faça a conversão para Megabytes e Kilobytes, usando as seguintes fórmulas:

#Para Megabytes: Gigabytes * 1024
#Para Kilobytes: Gigabytes * 1024 * 1024
#Responda o tamanho do arquivo em Megabytes e o tamanho em Kilobytes

gigaby = float(input('Arquivo em Gigabytes: GB'))
print(f'Tamanho do arquivo em Megabytes: {gigaby * 1024}MG')
print(f'Tamanho do arquivo em Kilobytes: {gigaby * 1024 * 1024}')