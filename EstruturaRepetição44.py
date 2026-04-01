#Exercício 44
#Numa eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
#Faça um programa que calcule e mostre:
#O total de votos para cada candidato;
#O total de votos nulos;
#O total de votos em branco;
#A percentagem de votos nulos sobre o total de votos;
#A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.

print('1- Jose\n2- Pedro\n3- Lucia\n4- Ana\n5- Voto Nulo\n6- Voto em Branco')

jose = pedro = lucia = ana = nulo = branco = total_votos = 0
while True:
    voto = int(input('Informe seu voto: '))
    if voto == 0:
        break
    if voto == 1:
        jose += 1
    if voto == 2:
        pedro += 1
    if voto == 3:
        lucia += 1
    if voto == 4:
        ana += 1
    if voto == 5:
        nulo += 1
    if voto == 6:
        branco += 1
total_votos = jose + pedro + lucia + ana + nulo + branco
print(f'Total de votos: {total_votos}')
print(f'Jose: {jose} voto(s)\nPedro: {pedro} voto(s)\nLucia: {lucia} voto(s)\nAna: {ana} voto(s)')
print(f'Votos Nulos: {nulo} voto(s)\nVotos Em Branco: {branco} voto(s)')
print(f'Percentagem de votos nulos: {(nulo / total_votos) * 100:.0f}%')
print(f'Percentagem de votos branco: {(branco / total_votos) * 100:.0f}%')

