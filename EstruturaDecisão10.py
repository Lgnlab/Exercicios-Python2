turno = str(input('Informe o turno que você estuda (Matutino/Vespertino/Noturno): ')).strip().upper()[0]
if turno == 'M':
    print('Bom dia!')
elif turno == 'V':
    print('Boa Tarde!')
elif turno == 'N':
    print('Boa noite!')
else:
    print('\033[31mValor Inválido!\033[m')