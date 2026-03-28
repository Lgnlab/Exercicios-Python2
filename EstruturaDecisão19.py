#Exercício 19
#Faça um programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.

#Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:

#326 = 3 centenas, 2 dezenas e 6 unidades

#12 = 1 dezena e 2 unidades

#Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

numero = str(input('Informe um número entre 1 e 1000: ')).strip()
if len(numero) == 1:
    print(f'{numero} = 1 Unidade')
elif len(numero) == 2:
    print(f'{numero} = {numero[0]} dezena e {numero[1]} unidade(s)')
elif len(numero) == 3:
    print(f'{numero} = {numero[0]} centena(s), {numero[1]} dezena(s) e {numero[2]} unidade(s)')
else:
    print(f'{numero} = {numero[0]} unidade de milhar, {numero[1]} centena(s), {numero[2]} dezena(s) e {numero[3]} unidade(s)')