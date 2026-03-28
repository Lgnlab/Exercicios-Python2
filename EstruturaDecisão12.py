#Exercício 12
#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
# O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

#Desconto do IR: - Salário Bruto até 900 (inclusive) - isento - Salário Bruto até 1500 (inclusive) - desconto de 5% - Salário Bruto até 2500 (inclusive) - desconto de 10% - Salário Bruto acima de 2500 - desconto de 20%

#Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

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