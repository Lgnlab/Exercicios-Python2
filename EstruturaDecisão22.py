#Exercício 22
#Faça um programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).

numero = int(input('Informe Um Número: '))
if numero % 2 == 0:
    print(f'O número {numero} é PAR!')
else:
    print(f'O número {numero} é IMPAR!')