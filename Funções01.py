#Exercício 01
#Faça um programa para imprimir:
#1
#2   2
#3   3   3
#.....
#n   n   n   n   n   n  ... n
#para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.

def imprimir_cascata(numero):
    """
    -> Imprime uma cascata numérica de 1 até n
    :param numero: até onde vai ser a cascata
    :return: a cascata
    """
    for linha in range(1, n + 1):
        for coluna in range(linha):
            print(linha, end=' ')
        print()
#Programa Principal
try:
    n = int(input('Informe um número: '))
    if n > 0:
        imprimir_cascata(n)
    else:
        print('Por favor, digite um número inteiro positivo.')
except ValueError:
    print('Entrada inválida. Digite um número inteiro.')