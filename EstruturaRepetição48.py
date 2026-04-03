#Exercício 48
#Faça um programa que peça um número inteiro positivo e em seguida mostre este numero invertido.

while True:
    numero = str(input('Digite um número inteiro: '))
    print(numero[::-1], end=' ')
    sair = str(input('Quer ver outro número [S/N]? ')).strip().upper()[0]
    if sair == 'N':
        break