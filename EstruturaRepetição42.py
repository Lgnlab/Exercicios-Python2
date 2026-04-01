#Exercício 42
#Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos:
#[0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.

cont_25 = cont_50 = cont_75 = cont_100 = 0
while True:
    numero = int(input('Informe um número: '))
    if numero < 0:
        break
    if numero < 25:
        cont_25 += 1
    if numero < 50:
        cont_50 += 1
    if numero < 75:
        cont_75 += 1
    if numero < 100:
        cont_100 += 1
print(f'No intervalo entre [0-25]: {cont_25} vez(es)\nNo intervalo entre [26-50]: {cont_50} vez(es)\nNo intervalo entre [51-75]: {cont_75} vez(es)\nNo intervalo entre [76-100]: {cont_100} vez(es)')
