#Exercício 02
#Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

num = int(input('Digite um número (Positivo / Negativo): '))
if num > 0:
    print(f'O número {num} é POSITIVO!')
else:
    print(f'O número {num} é NEGATIVO!')