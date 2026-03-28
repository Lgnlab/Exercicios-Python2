#Exercício 21
#Faça um programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas.
#As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais.
#O programa não deve se preocupar com a quantidade de notas existentes na máquina.

#Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
#Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

print(f'{"CAIXA ELETRÔNICO":=^38}')
print('Notas Disponíveis: R$ 1,5,10,50 e 100\nValor mínimo: R$10,00\nValor máximo: R$600,00')
saque = int(input('Valor Do Saque: R$'))
total = saque
cedula_atual = 100
total_cedulas = 0
while True:
    if total >= cedula_atual:
        total -= cedula_atual
        total_cedulas += 1
    else:
        if total_cedulas > 0:
            print(f'Total de cédulas {total_cedulas} de R${cedula_atual}')
        if cedula_atual == 100:
            cedula_atual = 50
        elif cedula_atual == 50:
            cedula_atual = 10
        elif cedula_atual == 10:
            cedula_atual = 5
        elif cedula_atual == 5:
            cedula_atual = 1
        total_cedulas = 0
        if total == 0:
            break