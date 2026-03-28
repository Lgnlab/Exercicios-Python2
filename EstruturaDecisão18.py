data = str(input('Data (dd/mm/aaaa): ')).strip()
if len(data) == 10:
    print('DATA VÁLIDA!')
else:
    print('DATA INVÁLIDA.')