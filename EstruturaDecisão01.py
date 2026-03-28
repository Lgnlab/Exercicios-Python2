#Exercício 01
#Faça um programa que peça dois números e imprima o maior deles.

num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
if num1 > num2:
    print(f'O número {num1} é o maior!')
else:
    print(f'O número {num2} é o maior!')