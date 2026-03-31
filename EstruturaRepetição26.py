#Exercício 26
#Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

pedro = vera = lucia = 0
total_eleitores = int(input('Números de eleitores para votação: '))
print('=' * 20)
print('Opções de voto: \nPedro vote 1\nVera vote 2\nLucia vote 3')
print('=' * 20)
for v in range(1, total_eleitores + 1):
    voto = int(input('Faça sua escolha: '))
    if voto == 1:
        pedro += 1
    elif voto == 2:
        vera += 1
    elif voto == 3:
        lucia += 1
print('=' * 20)
print(f'Quantidade de votos: \nPedro: {pedro}\nVera: {vera}\nLucia: {lucia}')
print('=' * 20)
if pedro > vera and pedro > lucia:
    print('Pedro foi eleito')
elif vera > pedro and vera > lucia:
    print('Vera foi eleita')
else:
    print('Lucia foi eleita')
