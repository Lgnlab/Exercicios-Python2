#Exercício 09
#Faça um programa que leia três números e mostre-os em ordem decrescente:

num1 = int(input('Número 1: '))
num2 = int(input('Número 2: '))
num3 = int(input('Número 3: '))
if num1 > num2 > num3:
    print(f'{num1}, {num2}, {num3}')
elif num2 > num1 > num3:
    print(f'{num2}, {num1}, {num3}')
elif num3 > num2 > num1:
    print(f'{num3}, {num2}, {num1}')

