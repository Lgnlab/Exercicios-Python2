
sair =  ''
soma = multi = maior = 0

valor1 = int(input('Primeiro Número: '))
valor2 = int(input('Segundo valor: '))

while sair != '5':
    print('Opções:')
    print("""
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
    """)
    escolha = str(input('Sua opção: ')).strip()
    if escolha == '1':
        soma = valor1 + valor2
        print(f'{valor1} + {valor2} = {soma}')
    elif escolha == '2':
        multi = valor1 * valor2
        print(f'{valor1} * {valor2} = {multi}')
    elif escolha == '3':
        if valor1 > valor2:
            maior = valor1
        else:
            maior = valor2
        print(f'Maior valor entre {valor1} e {valor2} é {maior}')
    elif escolha == '4':
        valor1 = int(input('Primeiro Número: '))
        valor2 = int(input('Segundo valor: '))
    elif escolha == '5':
        sair = '5'