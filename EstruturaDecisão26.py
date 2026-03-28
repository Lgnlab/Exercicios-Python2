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