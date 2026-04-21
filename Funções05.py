#Exercício 05
#Faça um programa com uma função chamada soma_imposto. A função possui dois parâmetros formais:
#taxa_imposto, que é a quantia de imposto sobre vendas expressas em porcentagem, e custo, que é o
#custo de um item antes do imposto. A função "altera" o valor de custo para incluir o imposto sobre vendas.
from dbm.sqlite3 import error


def soma_imposto(taxa_imposto, custo):
    calculo = custo + (custo * (taxa_imposto / 100))
    return calculo

#Programa Principal
try:
    taxa = int(input('Informe a percentagem do imposto: '))
    custo = float(input('Valor da venda: R$'))
except ValueError, TypeError:
    print(f'Digite um valor válido!')
else:
    print(f'Imposto: {taxa}%\nValor da venda sem imposto: R${custo:.2f}\nValor final com imposto: R${soma_imposto(taxa, custo):.2f}')
