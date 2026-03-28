#Exercício 08
#Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

ganho_hora = float(input('Ganho por hora R$'))
hora_trabalhada = float(input('Horas trabalhadas no mês: '))
calculo = ganho_hora * hora_trabalhada
print(f'Seu salário do mês será: R${calculo:.2f}')