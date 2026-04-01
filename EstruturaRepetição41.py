#Exercício 41
#Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.


while True:
    divi = float(input('Valor da dívida R$'))

    tres = divi * (10 / 100)
    seis = divi * (15 / 100)
    nove = divi * (20 / 100)
    doze = divi * (25 / 100)
    print('Quantidade de parcelas e juros sobre as parcelas:', end='')
    print(f'''
    Valor da Dívida:        Valor dos juros:    Quantidade de parcelas:        Valor da parcela:
    R${divi:.2f}\t            R${divi:.2f}          \t1                              R${divi:.2f}
    R${divi:.2f}\t            R${tres:.2f}          \t3                              R${(divi + tres) / 3:.2f}
    R${divi:.2f}\t            R${seis:.2f}          \t6                              R${(divi + seis) / 6:.2f} 
    R${divi:.2f}\t            R${nove:.2f}          \t9                              R${(divi + nove) / 9:.2f}
    R${divi:.2f}\t            R${doze:.2f}          \t12                             R${(divi + doze) / 12:.2f}
    ''')
    sair = input('Quer simular outro valor[S/N]: ').strip().upper()[0]
    if sair == 'N':
        break

