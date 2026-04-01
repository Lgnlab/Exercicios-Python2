#Exercício 38
#Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
#Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
#Em 1996 recebeu aumento de 1,5% sobre o seu salário inicial;
#A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
#Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.

salario_inicial = float(input('Informe seu salário atual: R$'))   #1995
aumento_percentual = 0
for c in range(1, 30):     #1997 29 anos para 2026
    aumento_percentual = c * 3

aumento = salario_inicial * (aumento_percentual / 100)
print(f'De 1997 até 2026: aumento percentual sobre o salário de {aumento_percentual}%')
print(f'Salário em 2026: R${aumento_percentual + salario_inicial:.2f}')