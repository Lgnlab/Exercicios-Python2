#Exercício 40
#Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
#Código da cidade;
#Número de veículos de passeio (em 1999);
#Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
#Qual o maior e menor índice de acidentes de trânsito e a que cidade pertence;
#Qual a média de veículos nas cinco cidades juntas;
#Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.


maior_acidentes = menor_acidentes = 0
cod_maior = cod_menor = int
soma_veiculos = 0
for c in range(1, 6):
    codigo_cidade = int(input('Código da cidade: '))
    acidentes = int(input('Número de acidentes de trânsito com vítimas: '))
    veiculos = int(input('Números de veículos: '))
    soma_veiculos += veiculos
    if acidentes > maior_acidentes:
        cod_maior = codigo_cidade
        maior_acidentes = acidentes
        menor_acidentes = acidentes
    if acidentes < menor_acidentes:
        cod_menor = codigo_cidade
        menor_acidentes = acidentes
print(f'O maior índice de acidentes é na cidade de código {cod_maior}: {maior_acidentes}')
print(f'O menor índice de acidentes é na cidade de código {cod_menor}: {menor_acidentes}')
print(f'A média de veículos das cinco cidades: {soma_veiculos / 5:.0f}')