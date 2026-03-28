ano = int(input('Verifique se o ano é BISSEXTO: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano} É BISSEXTO!')
else:
    print(f'O ano de {ano} NÃO É BISSEXTO.')