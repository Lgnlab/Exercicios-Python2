#Exercício 09
#Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soma = 0
for c in numeros:
    quadrados = c ** 2
    soma += quadrados
    print(quadrados, end=' ')
print()
print(f'Soma dos quadrados dos números: {soma}')