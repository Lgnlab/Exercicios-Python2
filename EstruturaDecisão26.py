#Exercício 26
#Um posto está vendendo combustíveis com a seguinte tabela de descontos:

#Álcool:

#até 20 litros: desconto de 3% por litro
#acima de 20 litros: desconto de 5% por litro
#Gasolina: - até 20 litros: desconto de 4% por litro - acima de 20 litros: desconto de 6% por litro

#Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma:
#A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

litros = float(input('Litros: '))
combustivel = str(input('Tipo Do Combustível[A/G]: ')).strip().upper()[0]
if combustivel == 'A':
    if litros <= 20:
        print('Preço Do Litro Do Álcool: R$1,90')
        calculo = litros * 1.90
        desconto = calculo * (3 / 100)
        total = calculo - desconto
        print(f'Valor Do Desconto (3%): R${desconto:.2f}\nTotal Com Desconto: R${total:.2f}')
    else:
        print('Preço Do Litro Do Álcool: R$1,90')
        calculo = litros * 1.90
        desconto = calculo * (5 / 100)
        total = calculo - desconto
        print(f'Valor Do Desconto (5%): R${desconto:.2f}\nTotal Com Desconto: R${total:.2f}')
if combustivel == 'G':
    if litros <= 20:
        print('Preço Do Litro Da Gasolina: R$2,50')
        calculo = litros * 2.50
        desconto = calculo * (4 / 100)
        total = calculo - desconto
        print(f'Valor Do Desconto (4%): R${desconto:.2f}\nTotal Com Desconto: R${total:.2f}')
    else:
        print('Preço Do Litro Da Gasolina: R$2,50')
        calculo = litros * 2.50
        desconto = calculo * (6 / 100)
        total = calculo - desconto
        print(f'Valor Do Desconto (6%): R${desconto:.2f}\nTotal Com Desconto: R${total:.2f}')