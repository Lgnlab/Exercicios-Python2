maior = 0
for n in range(1, 5 + 1):
    numero = int(input(f'Informe o {n} número: '))
    if numero > maior:
        maior = numero
print(f'Maior número digitado: {maior}')