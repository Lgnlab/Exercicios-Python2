pessoa_fisica = str(input('Informe O CPF(xxx.xxx.xxx-xx): ')).strip()
if len(pessoa_fisica) == 14:
    print(f'CPF {pessoa_fisica} válido')
else:
    print(f'CPF {pessoa_fisica} Inválido')