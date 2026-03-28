numero = str(input('Informe um número entre 1 e 1000: ')).strip()
if len(numero) == 1:
    print(f'{numero} = 1 Unidade')
elif len(numero) == 2:
    print(f'{numero} = {numero[0]} dezena e {numero[1]} unidade(s)')
elif len(numero) == 3:
    print(f'{numero} = {numero[0]} centena(s), {numero[1]} dezena(s) e {numero[2]} unidade(s)')
else:
    print(f'{numero} = {numero[0]} unidade de milhar, {numero[1]} centena(s), {numero[2]} dezena(s) e {numero[3]} unidade(s)')