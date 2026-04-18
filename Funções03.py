#Exercício 03
#Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def soma_numeros(n1, n2, n3):
    soma = n1 + n2 + n3
    return soma

#Programa Principal
try:
    n1 = int(input('Primeiro número: '))
    n2 = int(input('Segundo número: '))
    n3 = int(input('Terceiro número: '))
except ValueError:
    print('Digite um número inteiro')
except KeyboardInterrupt:
    print('Programa interrompido pelo o usuário')
else:
    print(f'Soma de todos os números: {soma_numeros(n1,n2,n3)}')