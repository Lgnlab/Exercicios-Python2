nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
media = (nota1 + nota2) / 2

if media == 7:
    print('APROVADO')
elif media < 7:
    print('REPROVADO')
elif media == 10:
    print('APROVADO COM DISTIÇÃO')
