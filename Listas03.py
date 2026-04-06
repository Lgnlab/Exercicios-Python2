#Exercício 03
#Faça um programa que leia 4 notas, mostre as notas e a média na tela.

soma_notas = 0
lista_notas = []
for notas in range(1, 5):
    nota = float(input(f'{notas} Nota: '))
    lista_notas.append(nota)
for m in lista_notas:
    soma_notas += m
media = soma_notas / len(lista_notas)
print('=' * 30)
print(f'Notas: {lista_notas}')
print(f'Média das notas: {media:.1f}')
print('=' * 30)