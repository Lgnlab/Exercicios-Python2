letra = str(input('Informe uma letra: ')).strip().upper()[0]
if letra == 'AEIOU':
    print(f'A letra {letra} é uma VOGAL!')
else:
    print(f'A letra {letra} é uma CONSOANTE!')