nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
nota3 = float(input('Nota 3: '))
media = (nota1 + nota2 + nota3) / 3
print(f'Média Geral: {media:.1f}')

if media >= 7:
    print('APROVADO', end=' ')
else:
    print('REPROVADO')
if media == 10:
    print('COM DISTINÇÃO')