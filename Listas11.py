#Exercício 11
#Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
lista3 = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
intercalado = []

for i in range(10):
    intercalado.append(lista1[i])
    intercalado.append(lista2[i])
    intercalado.append(lista3[i])

print('Vetor Intercalado:')
print(intercalado)

