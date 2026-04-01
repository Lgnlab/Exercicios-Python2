#Exercício 39
#Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros.
#Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.

cod_maior = cod_menor = 0
maior_altura = menor_altura = 0
for c in range(1, 6):
    cod = int(input('Número do aluno: '))
    altura = float(input('Altura do aluno: '))
    if altura > maior_altura:
        cod_maior = cod
        maior_altura = altura
        menor_altura = altura
    if altura < menor_altura:
        cod_menor = cod
        menor_altura = altura
print(f'Maior altura é do aluno de número {cod_maior}: {maior_altura:.2f}')
print(f'Menor altura é do aluno de número {cod_menor}: {menor_altura:.2f}')
