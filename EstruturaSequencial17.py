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