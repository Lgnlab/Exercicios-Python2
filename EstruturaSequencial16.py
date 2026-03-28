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