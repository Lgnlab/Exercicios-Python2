#Exercício 08
#Faça um programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respetivo vetor.
#Imprima a idade e a altura na ordem inversa a ordem lida.

dados = []
for d in range(1, 3):
    idade = int(input('Idade: '))
    altura = float(input('Altura (m): '))
    dados.append([idade, altura])
dados_invertidos = dados[::-1]
print(f'Dados inversos  a ordem lida: {dados_invertidos}')
