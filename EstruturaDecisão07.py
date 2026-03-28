#Exercício 07
#Faça um programa que leia três números e mostre o maior e o menor deles:

num1 = int(input('Número 1: '))
num2 = int(input('Número 2: '))
num3 = int(input('Número 3: '))
if num1 > num2 and num1 > num3:
    print(f'O primeiro número é o maior: {num1}')
elif num2 > num1 and num2 > num3:
    print(f'O segundo número é o maior: {num2}')
else:
    print(f'O terceiro número é o maior: {num3}')
if num1 < num2 and num1 < num3:
    print(f'O primeiro número é o menor: {num1}')
elif num2 < num1 and num2 < num3:
    print(f'O segundo número é o menor: {num2}')
else:
    print(f'O terceiro número é o menor: {num3}')