#Exercício 23
#Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
#O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
#Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

numero = int(input('Informe um número: '))
cont = 0
print('=' * 20)
for p in range(1, numero + 1):
    if numero % p == 0:
        print(f'\033[32m{p}\033[m', end=' ')
        cont += 1
    else:
        print(f'\033[31m{p}\033[m',end=' ')
print()
print('=' * 20)
print(f'O número {numero} tem {cont} divisores!')
if cont == 2:
    print(f'O número {numero} \033[32mÉ PRIMO!\033[m')
else:
    print(f'O número {numero} \033[31mNÃO É PRIMO!\033[m')