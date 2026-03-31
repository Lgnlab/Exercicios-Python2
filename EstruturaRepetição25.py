#Exercício 25
#Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60;
#e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

soma = 0
lista_idade = list()
while True:
    idade = int(input('Idade: '))
    lista_idade.append(idade)
    sair = input('Quer adicionar mais idade a lista [S/N]? ').strip().upper()[0]
    if sair == 'N':
        break
for i in lista_idade:
    soma += i
media = soma / len(lista_idade)
if media < 25:
    print(f'Média: {media:.0f} -> Jovem')
elif media <= 60:
    print(f'Média: {media:.0f} -> Adulto')
else:
    print(f'Média: {media:.0f} -> Idosa')
