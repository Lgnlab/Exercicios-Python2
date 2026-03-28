print(f'{"CAIXA ELETRÔNICO":=^38}')
print('Notas Disponíveis: R$ 1,5,10,50 e 100\nValor mínimo: R$10,00\nValor máximo: R$600,00')
saque = int(input('Valor Do Saque: R$'))
total = saque
cedula_atual = 100
total_cedulas = 0
while True:
    if total >= cedula_atual:
        total -= cedula_atual
        total_cedulas += 1
    else:
        if total_cedulas > 0:
            print(f'Total de cédulas {total_cedulas} de R${cedula_atual}')
        if cedula_atual == 100:
            cedula_atual = 50
        elif cedula_atual == 50:
            cedula_atual = 10
        elif cedula_atual == 10:
            cedula_atual = 5
        elif cedula_atual == 5:
            cedula_atual = 1
        total_cedulas = 0
        if total == 0:
            break