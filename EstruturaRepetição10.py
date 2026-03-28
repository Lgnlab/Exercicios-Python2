#Exercício 10
#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

inicio = int(input('Início: '))
fim = int(input('Fim: '))
for p in range(inicio, fim + 1):
    print(p, end=' ')
