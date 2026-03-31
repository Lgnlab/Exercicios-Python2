#Exercício 18
#Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

lista = [1, 2, 3, 4, 5]
maior = menor = 1
for c in lista:
    if c > maior:
        maior = c
    if c < menor:
        menor = c
print(f'Maior: {maior}\nMenor: {menor}')
