ganho_hora = float(input('Ganho por hora: R$'))
horas_mes = float(input('Horas trabalhadas no mês: '))
salario_total = ganho_hora * horas_mes
print(f'Salário Bruto: R${salario_total:.2f}')
imposto_renda = salario_total * (11 / 100)
print(f'IR (11%) - Desconto de R${imposto_renda:.2f}')
desconto_inss = salario_total * (8 / 100)
print(f'INSS (8%) - Desconto de R${desconto_inss}')
desconto_sindicato = salario_total * (5 / 100)
print(f'Sindicato (5%) - Desconto de R${desconto_sindicato}')
salario_liquido = salario_total - imposto_renda - desconto_inss - desconto_sindicato
print(f'Salário Líquido: R${salario_liquido:.2f}')
