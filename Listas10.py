#Exercício 10
#Faça um programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

lista1 = []
lista2 = []
lista3 = []
print('Primeira Lista:')
for l1 in range(1, 11):
    num = int(input(f'{l1}ª número: '))
    lista1.append(num)
print('Segunda lista:')
for l2 in range(1, 11):
    num = int(input(f'{l2}ª número: '))
    lista2.append(num)

lista3.append(lista1)
lista3.append(lista2)
print(lista3)