#Exercício 07
#Faça um programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

lista_numeros = []
soma = 0
multi = 1
for n in range(1, 6):
    numero = int(input(f'{n}ª Número: '))
    lista_numeros.append(numero)
for op in lista_numeros:
    soma += op
    multi *= op
print(f'Valores lidos: {lista_numeros}')
print(f'Soma dos valores lidos: {soma}\nMultiplicação dos valores lidos: {multi}')