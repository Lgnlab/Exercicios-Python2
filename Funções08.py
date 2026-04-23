#Exercício 08
#Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

def contador_digitos(numero):
    tamanho = len(numero)
    return tamanho

# Programa Principal
numeros = str(input('Informe um número inteiro: '))
print(contador_digitos(numeros))