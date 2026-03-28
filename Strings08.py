frase = str(input('Verifique se a frase é uma palíndromo: ')).split()
junto = ''.join(frase).upper()
inverso = junto[::-1].upper()
if junto == inverso:
    print(f'{junto} e {inverso} SÃO PALÍNDROMO!')
else:
    print(f'{junto} e {inverso} NÃO PALÍNDROMO!')