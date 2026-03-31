#Exercício 33
#O Departamento Estadual de Meteorologia contratou você para desenvolver um programa que leia um conjunto indeterminado de temperaturas,
#e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.

lista_tempe = []
maior = menor = 0
while True:
    temperaturas = int(input('Temperatura em ªC: '))
    lista_tempe.append(temperaturas)
    sair = input('Quer adicionar mais temperaturas[S/N]: ').strip().upper()[0]
    if sair == 'N':
        break
for t in lista_tempe:
    if t > maior:
        maior = t
        menor = t
    if t < menor:
        menor = t
print(f'Maior temperatura registrada: {maior}ºC\nMenor temperatura registrada: {menor}ºC')