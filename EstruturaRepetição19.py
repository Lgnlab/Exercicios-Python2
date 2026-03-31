#Exercício 19
#Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

maior = menor = 0
while True:
    numero = int(input('Informe um número: '))
    if numero < 0 or numero > 1000:
        continue
    else:
        break
print('Sequência: ', end='')
for c in range(0, numero + 1):
    print(c, end=' ')
    if c > maior:
        maior = c
    if c < menor:
        menor = c
print()
print(f'Maior: {maior}\nMenor: {menor}')