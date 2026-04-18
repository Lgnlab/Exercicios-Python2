#Exercício 02
#Faça um programa para imprimir:
#1
#1   2
#1   2   3
#.....
#1   2   3   ...  n
#Para um n informado pelo usuário. Use uma função que receba um valor n inteiro, imprima até a n-ésima linha.

def cascata(n):
    for linha in range(1, n + 1):
        for coluna in range(linha):
            print(linha, end=' ')
        print()


try:
    numero = int(input('Informe um número: '))
    if numero > 0:
        cascata(numero)
    else:
        print('Digite um número maior que zero.')
except ValueError:
    print('Digite um número inteiro.')