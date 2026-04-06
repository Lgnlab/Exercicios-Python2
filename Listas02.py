#Exercício 02
#Faça um programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

lista_numeros = []
for leitura in range(1, 11):
    numeros = str(input(f'Informe o {leitura}ª número: '))
    lista_numeros.append(numeros)
print('=' * 30)
print(lista_numeros[::-1])

