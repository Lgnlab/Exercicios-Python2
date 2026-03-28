#Exercício 09
#Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx
#e indique se é um número válido ou inválido através da validação dos dígitos verificadores edos caracteres de formatação.

pessoa_fisica = str(input('Informe O CPF(xxx.xxx.xxx-xx): ')).strip()
if len(pessoa_fisica) == 14:
    print(f'CPF {pessoa_fisica} válido')
else:
    print(f'CPF {pessoa_fisica} Inválido')