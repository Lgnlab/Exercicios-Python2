numero = int(input('Informe um número para ver o dia da semana (1-7): '))

if numero == 1:
    print('Domingo')
elif numero == 2:
    print('Segunda-Feira')
elif numero == 3:
    print('Terça-Feira')
elif numero == 4:
    print('Quarta-Feira')
elif numero == 5:
    print('Quinta-Feira')
elif numero == 6:
    print('Sexta-Feira')
elif numero == 7:
    print('Sábado')
else:
    print('\033[31mVALOR INVÁLIDO\033[m')