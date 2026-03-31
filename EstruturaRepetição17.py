#Exercício 17
#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

numero = int(input('Informe um número: '))
fatorial = 1
print(f'{numero}! = ', end='')
for f in range(numero, 0, - 1):
    fatorial *= f
    if f == 1:
        print(f'{f} = ', end='')
    else:
        print(f'{f}.', end='')
print(fatorial)