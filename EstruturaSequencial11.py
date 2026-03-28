#Exercício 11
#Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre:

#O produto do dobro do primeiro com metade do segundo .
#A soma do triplo do primeiro com o terceiro.
#O terceiro elevado ao cubo.

num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
num3 = float(input('Terceiro número: '))
print(f'O produto do dobro do primeiro com metade do segundo: {(num1 * 2) * (num2 / 2)}')
print(f'A soma do triplo do primeiro com o terceiro: {(num1 * 3) + num3}')
print(f'O terceiro elevado ao cubo: {num3**3:.2f}')