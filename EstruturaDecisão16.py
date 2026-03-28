valor1 = int(input('Valor A: '))
valor2 = int(input('Valor B: '))
valor3 = int(input('Valor C: '))
delta = (valor2 ** 2) - (4 * valor1 * valor3)
print(f'Delta:{delta}')

if valor1 == 0:
    print('A equação não é do segundo grau.')
elif delta < 0:
    print('A equação não possui raizes reais.')
elif delta == 0:
    x = -valor2 / (2 * valor1)
    print(f'Delta ZERO. A equação possui apenas uma raiz real. {x}')
else:
    print('A equação possui duas raizes reais.')