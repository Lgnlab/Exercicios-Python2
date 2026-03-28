ganho_hora = float(input('Ganho por hora R$'))
hora_trabalhada = float(input('Horas trabalhadas no mês: '))
calculo = ganho_hora * hora_trabalhada
print(f'Seu salário do mês será: R${calculo:.2f}')