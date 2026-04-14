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