#Exercício 16
#Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por cento das suas
# vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470.
# Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:


faixas = [['R$200 - R$299'], ['R$300 - R$399'], ['R$400 - R$499'], ['R$500 - R$599'], ['R$600 - R$699'], ['R$700 - R$799'], ['R$800 - R$899'], ['R$900 - R$999'], ['R$1000']]
while True:
    vendas = float(input('Vendas da semana R$'))
    if vendas == 0:
        break
    else:
        bonus = vendas * (9 / 100)
        salario_final = 200 + bonus
        print(f'Salário: R$200.00 + R${bonus:.2f} = R${salario_final:.2f}')
        if salario_final >= 200 <= 299:
            print(f'O funcionário está na faixa 0: {faixas[0]}')
        elif salario_final <= 399:
            print(f'O funcionário está na faixa 1: {faixas[1]}')
        elif salario_final <= 499:
            print(f'O funcionário está na faixa 2: {faixas[2]}')
        elif salario_final <= 599:
            print(f'O funcionário está na faixa 3: {faixas[3]}')
        elif salario_final <= 699:
            print(f'O funcionário está na faixa 4: {faixas[4]}')
        elif salario_final <= 799:
            print(f'O funcionário está na faixa 5: {faixas[5]}')
        elif salario_final <= 899:
            print(f'O funcionário está na faixa 6: {faixas[6]}')
        elif salario_final <= 999:
            print(f'O funcionário está na faixa 7: {faixas[7]}')
        else:
            print(f'O funcionário está na faixa 8: {faixas[8]}')

