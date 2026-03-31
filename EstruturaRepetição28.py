#Exercício 28
#Faça um programa que calcule o valor total investido por um colecionador na sua coleção de CDs e o valor médio gasto em cada um deles.
#O usuário deverá informar a quantidade de CDs e o valor para em cada um.

soma = 0
cont_cds = int(input('Informe a quantidade de CDs da sua coleção: '))
for c in range(1, cont_cds + 1):
    valor = float(input('Valor estimado em cada um: R$'))
    soma += valor
media = soma / cont_cds
print(f'Valor médio gasto: R${media:.2f}\nTotal gasto: R${soma:.2f}')