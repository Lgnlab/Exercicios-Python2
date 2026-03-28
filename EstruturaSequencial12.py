#Exercício 12
#Tendo como dados de entrada um arquivo em Gigabytes, construa um algoritmo que faça a conversão para Megabytes, usando a seguinte fórmula:

gigabytes = float(input('Informe o tamanho do arquivo: GB'))
print(f'Convertendo o arquivo {gigabytes}GB para megabytes: {gigabytes * 1024}MB')