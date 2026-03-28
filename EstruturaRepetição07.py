#Exercício 7
#Faça um programa que leia 5 números e informe o maior número.

maior = 0
for n in range(1, 5 + 1):
    numero = int(input(f'Informe o {n} número: '))
    if numero > maior:
        maior = numero
print(f'Maior número digitado: {maior}')