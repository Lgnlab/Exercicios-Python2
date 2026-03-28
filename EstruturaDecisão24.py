numero1 = float(input('Primeiro Número: '))
numero2 = float(input('Segundo Número: '))
operando = str(input('Operador (+, -, *, /): ')).strip()[0]

if operando == '+':
    soma = numero1 + numero2
    print(f'{numero1} + {numero2} = {soma}')
    if soma % 2 == 0:
        print(f'O número {soma} é PAR!')
    else:
        print(f'O número {soma} é IMPAR!')
    if soma > 0:
        print('POSITIVO')
    else:
        print('NEGATIVO')
    if soma % 1 == 0:
        print('INTEIRO')
    else:
        print('DECIMAL')
elif operando == '-':
    subtra = numero1 - numero2
    print(f'{numero1} - {numero2} = {subtra}')
    if subtra % 2 == 0:
        print(f'O número {subtra} é PAR!')
    else:
        print(f'O número {subtra} é IMPAR')
    if subtra > 0:
        print('POSITIVO')
    else:
        print('NEGATIVO')
    if subtra % 1 == 0:
        print('INTEIRO')
    else:
        print('DECIMAL')
elif operando == '*':
    multi = numero1 * numero2
    print(f'{numero1} * {numero2} = {multi}')
    if multi % 2 == 0:
        print(f'O número {multi} é PAR!')
    else:
        print(f'O número {multi} é IMPAR!')
    if multi > 0:
        print('POSITIVO')
    else:
        print('NEGATIVO')
    if multi % 1 == 0:
        print('INTEIRO')
    else:
        print('DECIMAL')
elif operando == '/':
    divis = numero1 / numero2
    print(f'{numero1} / {numero2} = {divis}')
    if divis % 2 == 0:
        print(f'O número {divis} é PAR!')
    else:
        print(f'O número {divis} é IMPAR!')
    if divis > 0:
        print('POSITIVO')
    else:
        print('NEGATIVO')
    if divis % 1 == 0:
        print('INTEIRO')
    else:
        print('DECIMAL')