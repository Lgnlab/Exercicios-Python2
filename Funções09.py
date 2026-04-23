#Exercício 09
#Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

def reverso_numero(numero):
    """
    • Recebe um número em forma de string e inverte o número
    :param numero: Número a ser revertido
    :return: O número de trás para frente
    """
    reverso = numero[::-1]
    return reverso

try:
    numeros = int(input('Informe um número: '))
    mudando = str(numeros)
except ValueError, TypeError:
    print('Informe um número inteiro')
else:
    print(reverso_numero(mudando))