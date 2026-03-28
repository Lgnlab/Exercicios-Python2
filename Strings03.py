#Exercício 03
#Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.

nome = str(input('Digite seu nome: ')).strip().upper()
for vertical in nome:
    print(vertical)
    