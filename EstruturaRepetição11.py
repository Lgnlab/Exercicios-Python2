inicio = int(input('Início: '))
fim = int(input('Fim: '))
soma = 0
for i in range(inicio, fim + 1):
    soma += i
print(f'Soma do intervalo de {inicio} e {fim}: {soma}')