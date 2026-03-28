#Exercício 8
#Faça um programa que leia 5 números e informe a soma e a média dos números.

soma = 0
for n in range(1, 6):
    numero = int(input(f'Número {n}: '))
    soma += numero
media = soma / 5
print(f'Total: {soma}\nMédia: {media:.1f}')