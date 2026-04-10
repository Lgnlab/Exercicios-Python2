#Exercício 10
#Faça um programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

lista1 = []
lista2 = []
intercalado = []

print('Primeira Lista:')
for l1 in range(1, 5 + 1):
    num = int(input(f'{l1}ª número: '))
    lista1.append(num)
print('Segunda lista:')
for l2 in range(1, 5 + 1):
    num = int(input(f'{l2}ª número: '))
    lista2.append(num)
for i in range(5):
    intercalado.append(lista1[i])
    intercalado.append(lista2[i])

print('Vetor Intercalado:')
print(intercalado)
