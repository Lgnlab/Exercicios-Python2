#Exercício 21
#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

while True:
    numero = int(input('Informe um número: '))
    if numero % 2 == 0:
        print(f'O número {numero} É PRIMO')
    else:
        print(f'O número {numero} NÃO É PRIMO!')
    sair = input('Quer verificar outro número [S/N]: ').strip().upper()[0]
    if sair == 'N':
        break
