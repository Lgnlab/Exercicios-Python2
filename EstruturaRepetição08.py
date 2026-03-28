soma = 0
for n in range(1, 6):
    numero = int(input(f'Número {n}: '))
    soma += numero
media = soma / 5
print(f'Total: {soma}\nMédia: {media:.1f}')