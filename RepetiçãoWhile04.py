numero = int(input('Informe um número: '))
i = numero
multi = 1
print(f'{numero}!=', end=' ')
while i > 0:
    multi *= i
    if i > 1:
        print(i, end=' x ')
    else:
        print(i, end=' = ')
    i -= 1
print(f'{multi}')