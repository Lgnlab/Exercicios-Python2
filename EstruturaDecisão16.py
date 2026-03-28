#Exercício 16
#Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
#O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

#Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
#Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

valor1 = int(input('Valor A: '))
valor2 = int(input('Valor B: '))
valor3 = int(input('Valor C: '))
delta = (valor2 ** 2) - (4 * valor1 * valor3)
print(f'Delta:{delta}')

if valor1 == 0:
    print('A equação não é do segundo grau.')
elif delta < 0:
    print('A equação não possui raizes reais.')
elif delta == 0:
    x = -valor2 / (2 * valor1)
    print(f'Delta ZERO. A equação possui apenas uma raiz real. {x}')
else:
    print('A equação possui duas raizes reais.')