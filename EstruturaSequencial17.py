#Exercício 17
#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
#Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math
from math import ceil

area = float(input('Tamanho a ser pintado em metros(m): '))
cobertura = area / 6 * 1.1
lata_grande = math.ceil(cobertura / 18)
lata_pequena = math.ceil(cobertura / 3.6)

print(f'Se optar por levar apenas latas grandes(R$80,00): {lata_grande} latas R${lata_grande * 80:.2f}')
print(f'Se optar por levar apenas latas pequenas(R$25,00): {lata_pequena} galões R${lata_pequena * 25:.2f}')
mistura_latas = int(cobertura / 18)
resto = cobertura % 18
mistura = math.ceil(resto / 3.6)
preco_mistura = (mistura_latas * 80) + (mistura * 25)
print(f'Quantidade: {mistura_latas} lata(s) e {mistura} galão(ões)')
print(f'Preço mistura R${preco_mistura:.2f}')