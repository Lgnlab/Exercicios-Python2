lado1 = int(input('Lado 1: '))
lado2 = int(input('Lado 2: '))
lado3 = int(input('Lado 3: '))
if lado1 + lado2 > lado3 or lado2 + lado3 > lado1 or lado1 + lado3 > lado2:
    print('Podemos formar um TRIÂNGULO!')
if lado1 == lado2 == lado3:
    print('TRIÂNGULO EQUILÁTERO')
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print('TRIÂNGULO ISÓSCELES')
else:
    print('TRIÂNGULO ESCALENO')