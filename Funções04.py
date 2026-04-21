#Exercício 04
#Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere P, se o seu argumento for positivo, e N, se o seu argumento for zero ou negativo.

def caractere(estado=False):
    if estado:
        print('P')
    elif estado == 0:
        print('N')

#Programa Principal
caractere()