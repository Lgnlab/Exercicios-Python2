#Exercício 16
#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
#Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
#Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

import math
from math import ceil

area = float(input('Informe o tamanho em metros(m): '))
cobertura = area / 3
latas = cobertura / 18
cima = math.ceil(latas)
total = cima * 80
print(f'Para pintar uma área de {area}m vai ser preciso {cobertura:.0f} litros')
print(f'Total de latas: {cima}')
print(f'Total: R${total:.2f}')