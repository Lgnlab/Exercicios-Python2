data = str(input('Data De Nascimento (dd/mm/aaaa): ')).strip()

if data[3:5] == '01':
    print(f'Você nasceu em {data[0:2]} de Janeiro de {data[6:]}')
elif data[3:5] == '02':
    print(f'Você nasceu em {data[0:2]} de Fevereiro de {data[6:]}')
elif data[3:5] == '03':
    print(f'Você nasceu em {data[0:2]} de Março de {data[6:]}')
elif data[3:5] == '04':
    print(f'Você nasceu em {data[0:2]} de Abril de {data[6:]}')
elif data[3:5] == '05':
    print(f'Você nasceu em {data[0:2]} de Maio de {data[6:]}')
elif data[3:5] == '06':
    print(f'Você nasceu em {data[0:2]} de Junho de {data[6:]}')
elif data[3:5] == '07':
    print(f'Você nasceu em {data[0:2]} de Julho de {data[6:]}')
elif data[3:5] == '08':
    print(f'Você nasceu em {data[0:2]} de Agosto de {data[6:]}')
elif data[3:5] == '09':
    print(f'Você nasceu em {data[0:2]} de Setembro de {data[6:]}')
elif data[3:5] == '10':
    print(f'Você nasceu em {data[0:2]} de Outubro de {data[6:]}')
elif data[3:5] == '11':
    print(f'Você nasceu em {data[0:2]} de Novembro de {data[6:]}')
elif data[3:5] == '12':
    print(f'Você nasceu em {data[0:2]} de Dezembro de {data[6:]}')