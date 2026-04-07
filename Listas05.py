#Exercício 05
#Faça um programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números ÍMPARES no vetor impar. Imprima os três vetores.

lista_impar = []
lista_par = []
for n in range(1, 21):
    numero = int(input(f'{n}ª Número: '))
    if numero % 2 == 0:
        lista_par.append(numero)
    else:
        lista_impar.append(numero)
print('=>' * 40)
print(f'Lista de PARES: \033[34m{lista_par}\033[m\nLista ÍMPARES: \033[35m{lista_impar}\033[m')