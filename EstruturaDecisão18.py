#Exercício 18
#Faça um programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

data = str(input('Data (dd/mm/aaaa): ')).strip()
if len(data) == 10:
    print('DATA VÁLIDA!')
else:
    print('DATA INVÁLIDA.')