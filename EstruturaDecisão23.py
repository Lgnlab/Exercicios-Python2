#Exercício 23
#Faça um programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.

numero = float(input('Informe Um Número: '))
if numero % 1 == 0:
    print(f'O número {numero:.0f} é INTEIRO!')
else:
    print(f'O número {numero} é DECIMAL!')
