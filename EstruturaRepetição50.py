#Exercício 50
#Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.

h = 1
soma = 0
termos = int(input('Quantos termos você gostaria de ver: '))
for c in range(h, termos + 1):
    calculo = h / c
    soma += calculo
print(f'Valor de H: {soma:.1f}')