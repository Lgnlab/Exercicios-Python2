#Exercício 47
#Numa competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes.
#Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas pelo atleta na sua apresentação e depois informe a sua média, conforme
#a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). As notas não são informados ordenadas

lista_notas = []
maior_nota = menor_nota = soma_nota = 0
nome = str(input('Nome do atleta: ')).strip()
for n in range(1, 8):
    nota = float(input('Nota: '))
    soma_nota += nota
    lista_notas.append(nota)
print('Resultado final:')
for c in lista_notas:
    if c > maior_nota:
        maior_nota = c
        menor_nota = c
    if c < menor_nota:
        menor_nota = c
print(f'Atleta: {nome}')
print(f'Melhor nota: {maior_nota:.1f}\nPior nota: {menor_nota:.1f}\nMédia: {soma_nota / 7:.1f}')