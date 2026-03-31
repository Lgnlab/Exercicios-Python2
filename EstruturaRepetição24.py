#Exercício 24
#Faça um programa que calcule o mostre a média aritmética de N notas.

soma = 0
lista_notas = []
while True:
    nota = float(input(f'Nota: '))
    lista_notas.append(nota)
    escolha = input('Quer adicionar mais notas[S/N]? ').strip().upper()[0]
    if escolha == 'N':
        break
print('Notas: ')
for n in lista_notas:
    if lista_notas:
        print(f'{n:.1f}', end=' ')
    soma += n
media = soma / len(lista_notas)
print()
print(f'Média final: {media:.1f}')
