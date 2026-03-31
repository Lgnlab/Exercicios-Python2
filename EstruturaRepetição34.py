#Exercício 34
#Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é aquele que é divisível apenas por um e por ele mesmo.
#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

numero = int(input('Informe um número: '))
cont_divisor = 0
for p in range(1, numero + 1):
    if numero % p == 0:
        print(f'\033[31m{p}\033[m', end=' ')
        cont_divisor += 1
    else:
        print(f'\033[32m{p}\033[m', end=' ')
print()
if cont_divisor == 2:
    print(f'O número {numero} É PRIMO!')
else:
    print(f'O número {numero} NÃO É PRIMO!')
print(f'Divisores: {cont_divisor}')
