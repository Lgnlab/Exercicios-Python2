#Exercício 21
#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

cont = 0
numero = int(input('Informe um número: '))
for p in range(1, numero + 1):
    if numero % p == 0:
        cont += 1
if cont == 2:
    print(f'O número {numero} É PRIMO')
else:
    print(f'O número {numero} NÃO É PRIMO!')

