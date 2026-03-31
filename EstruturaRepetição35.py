#Exercício 35
#Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.

numero = int(input('Intervalo: '))
lista_numeros = []
for p in range(2, numero + 1):
    e_primo = True
    for v in range(2, p):
        if p % v == 0:
            e_primo = False
            break
    if e_primo:
        lista_numeros.append(p)
print(f'Os números encontrados foram: {lista_numeros}')