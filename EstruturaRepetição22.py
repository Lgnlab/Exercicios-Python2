#Exercício 22
#Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais números ele é divisível.

cont = 0
numero = int(input('Informe um número: '))
print(f'Divisores de {numero}:')
for p in range(1, numero + 1):
    if numero % p == 0:
        print(f'\033[31m{p}\033[m', end=' ')
        cont += 1
print()
if cont == 2:
    print(f'O número {numero} É PRIMO!')
else:
    print(f'O número {numero} NÃO É PRIMO!')