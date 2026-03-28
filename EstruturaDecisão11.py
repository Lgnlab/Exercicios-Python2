salario = float(input('Informe o salário:R$'))
if salario <= 280:
    aumento = salario * (20 / 100)
    print(f'O salário de R${salario:.2f} terá um aumento de 20%: R${aumento:.2f}\nValor com aumento: R${aumento + salario:.2f}')
elif salario <= 700:
    aumento = salario * (15 / 100)
    print(f'O salário de R${salario:.2f} terá um aumento de 15%: R${aumento:.2f}\nValor com aumento: R${aumento + salario:.2f}')
elif salario <= 1500:
    aumento = salario * (10 / 100)
    print(f'O salário de R${salario:.2f} terá um aumento de 10%: R${aumento:.2f}\nValor com aumento: R${aumento + salario:.2f}')
else:
    aumento = salario * (5 / 100)
    print(f'O salário de R${salario:.2f} terá um aumento de 5%: R${aumento:.2f}\nValor com aumento: R${aumento + salario:.2f}')
