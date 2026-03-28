valor_hora = float(input('Valor da hora trabalhada:R$'))
hora_mes = float(input('Horas trabalhas no referente mês:'))
salario_bruto = valor_hora * hora_mes
print(f'R${salario_bruto:.2f}')
calculo_fgts = salario_bruto * (11 / 100)
calculo_inss = salario_bruto * (10 / 100)

if salario_bruto <= 900:
    status_desconto = 0
    desconto = 0
    desconto_geral = salario_bruto - calculo_inss
    soma_desconto = calculo_inss
    print('Isento do imposto de renda!')
elif salario_bruto <= 1500:
    status_desconto = 5
    desconto = salario_bruto * (5 / 100)
    desconto_geral = salario_bruto - calculo_inss - desconto
    soma_desconto = calculo_inss + desconto
elif salario_bruto <= 2500:
    status_desconto = 10
    desconto = salario_bruto * (10 / 100)
    desconto_geral = salario_bruto - calculo_inss - desconto
    soma_desconto = calculo_inss + desconto
else:
    status_desconto = 20
    desconto = salario_bruto * (20 / 100)
    desconto_geral = salario_bruto - calculo_inss -desconto
    soma_desconto = calculo_inss + desconto

print(f'''
salário Bruto: ({valor_hora:.0f} * {hora_mes:.0f}{')':.<25}:R${salario_bruto:.2f}
(-) IR ({status_desconto}%){'':.<37}:R${desconto:.2f}
(-) INSS (10%){'':.<34}:R${calculo_inss:.2f}
FGTS (11%){'':.<38}:R${calculo_fgts:.2f}
Total de descontos {'':.<29}:R${soma_desconto:.2f}
Salário Líquido{'':.<33}:R${desconto_geral:.2f}
''')