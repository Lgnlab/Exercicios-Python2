#Exercício 20
#Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.

while True:
    numero = int(input('Informe um número: '))
    fatorial = 1
    print(f'{numero}! = ', end='')
    for c in range(numero, 0, -1):
        fatorial *= c
        if c == 1:
            print(f'{c} = ', end='')
        else:
            print(f'{c}.', end='')
    print(fatorial)
    sair = input('Quer calcular outro fatorial [S/N]?: ').upper().strip()[0]
    if sair == 'N':
        break