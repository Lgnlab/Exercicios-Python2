#O programa deverá permitir a digitação do salário de um número indefinido (desconhecido) de salários. Um valor de salário igual a 0 (zero) encerra a digitação.
#Após a entrada de todos os dados o programa deverá calcular o valor do abono concedido a cada colaborador, de acordo com a regra definida acima.

#Ao final, o programa deverá apresentar:
#O salário de cada funcionário, com o valor do abono;
#O número total de funcionário processados;
#O valor total a ser gasto com o pagamento do abono;
#O número de funcionário que receberá o valor mínimo de 100 reais;
#O maior valor pago como abono;
#Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro;
#O piso do abono será de 100 reais, isto é, aqueles funcionários cujo salário for muito baixo, recebem este valor mínimo;

lista_salarios = []
lista_abono = []
colaboradores = valor_minimo = total_abono = maior_abono = 0
while True:
    salario = float(input('Salário: R$'))
    if salario == 0:
        break
    else:
        lista_salarios.append(salario)
        colaboradores += 1
print('Salário     - Abono')
for cont in lista_salarios:
    if cont >= 1000:
        calculo = cont * (20 / 100)
        lista_abono.append(calculo)
        total_abono += calculo
        print(f'R${cont:.2f} - R${calculo:.2f}')
    else:
        print(f'R${cont:.2f} - R$100.00')
        lista_abono.append(100)
        total_abono += 100
        valor_minimo += 1

print(f'Foram processados {colaboradores} colaboradores')
print(f'Total gasto com abonos: R${total_abono:.2f}')
print(f'Valor mínimo pago a {valor_minimo} colaboradores')

for maior in lista_abono:
    if maior > maior_abono:
        maior_abono = maior
print(f'Maior valor de abono pago: R${maior_abono:.2f}')