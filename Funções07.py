#Exercício 07
#Faça um programa que use a função valor_pagamento para determinar o valor a ser pago por uma prestação de uma conta.
#O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a
#função valor_pagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá
#então exibir o valor a ser pago na tela. Após a execução, o programa deverá voltar a pedir outro valor de prestação e assim
#continuar até que seja informado um valor igual a zero para a prestação. Neste momento, o programa deverá ser encerrado, exibindo
#o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma.
#Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.

def valor_pagamento(parcela, dias_atraso=0):
    if dias_atraso > 0:
        calculo_multa = parcela + (parcela * (3 / 100))
        calculo_juros = (calculo_multa * 0.1) * dias_atraso
        return calculo_multa, calculo_juros
    else:
        return parcela, dias_atraso

# Programa Principal
relatorio_dia = []
while True:
    try:
        parcelas = float(input('Valor da prestação: R$'))
        if parcelas == 0:
            break
        atraso = int(input('Informe os dias de atraso: '))
    except ValueError, TypeError:
        print('\033[31mERRO! Digite um valor conforme as regras.\033[m')
    except KeyboardInterrupt:
        print('Usuário interrompeu o programa.')
    else:
        retorno = valor_pagamento(parcelas, atraso)
        relatorio_dia.append(retorno)
print('=' * 25)
print('Relatório Do Dia:')
for p, a in relatorio_dia:
    print(f'Prestação: R${p:.2f} - Valor do Atraso: R${a:.2f}')
