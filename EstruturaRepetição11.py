#Exercício 11
#Altere o programa anterior para mostrar no final a soma dos números.

inicio = int(input('Início: '))
fim = int(input('Fim: '))
soma = 0
for i in range(inicio, fim + 1):
    soma += i
print(f'Soma do intervalo de {inicio} e {fim}: {soma}')