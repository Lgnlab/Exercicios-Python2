#Exercício 21
#Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um número indeterminado de entradas, cada uma contendo:
#um número de identificação do mouse o tipo de defeito:
#necessita da esfera;
#necessita de limpeza; a.necessita troca do cabo ou conector; a.quebrado ou inutilizado Uma identificação igual a zero encerra o programa.

quantidade_mouses = []
lista_defeitos = []
d1 = d2 = d3 = d4 = 0
while True:
    identi = int(input('Número de identificação: '))
    if identi == 0:
        break
    defeito = int(input('Defeito: '))
    lista_defeitos.append(defeito)
    quantidade_mouses.append(identi)
for d in lista_defeitos:
    if d == 1:
        d1 += 1
    if d == 2:
        d2 += 1
    if d == 3:
        d3 += 1
    if d == 4:
        d4 += 1
print(f'1.Necessita de esfera: {d1} mouses - cerca de {(d1/ len(quantidade_mouses)) * 100:.0f}%')
print(f'2.Necessita de limpeza: {d2} mouses - cerca de {(d2 / len(quantidade_mouses)) * 100:.0f}%')
print(f'3.Necessita troca do cabo ou conector: {d3} mouses - cerca de {(d3 / len(quantidade_mouses)) * 100:.0f}%')
print(f'4.Quebrado ou inutilizado: {d4} mouses - cerca de {(d4 / len(quantidade_mouses)) * 100:.0f}%')