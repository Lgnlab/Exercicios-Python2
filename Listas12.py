#Exercício 12
#Foram anotadas as idades e alturas de 10 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.

dados = []
soma = media = cont_altura = 0

for cont in range(1, 11):
    nome = str(input('Nome Do Aluno: '))
    idade = int(input('Idade: '))
    altura = float(input('Altura: '))
    dados.append([nome, idade, altura])
for m in dados:
    soma += m[2]
    media = soma / len(dados)
print(f'Média de altura da turma: {media:.2f}')
for c in dados:
    if c[1] == 13 and c[2] < media:
        cont_altura += 1
print(f'{cont_altura} alunos possuem altura inferior a média da turma')