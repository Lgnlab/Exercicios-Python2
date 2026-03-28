#Exercício 27
#Uma fruteira está vendendo frutas com a seguinte tabela de preços:

#                Até 5 Kg                Acima de 5 Kg
#Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.
#Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

morango = float(input('Peso Morango kg: '))
apple = float(input('Peso Maçã kg: '))
tot_kg = morango + apple
tot_compra = 0

if morango <= 5:
    calculo_morango = morango * 2.50
    print(f'Você comprou {morango}kg de morango\nValor do kg: R$2,50\nTotal: R${calculo_morango:.2f}')
else:
    calculo_morango = morango * 2.20
    print(f'Você comprou {morango}kg de morango\nValor do kg: R$2,20\nTotal: R${calculo_morango:.2f}')
print('=' * 30)
if apple <= 5:
    calculo_apple = apple * 1.80
    print(f'Você comprou {apple}kg de maçã\nValor do kg: R$1,80\nTotal: R${calculo_apple:.2f}')
else:
    calculo_apple = apple * 1.50
    print(f'Você comprou {apple}kg de maçã\nValor do kg: R$1,50\nTotal: R${calculo_apple:.2f}')
print('=' * 30)
tot_compra = calculo_morango + calculo_apple

if tot_kg > 8 or tot_compra > 25:
    desconto = tot_compra * (10 / 100)
    print(f'Total da compra com desconto de 10%: R${tot_compra - desconto:.2f}')
else:
    print(f'Sem Desconto Adicional!\nTotal Da Compra: R${tot_compra:.2f}')