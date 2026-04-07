#Exercício 06
#Faça um programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

lista_media = []
media_maior = 0
for notas in range(1, 11):
    nota1 = float(input('1ª nota: '))
    nota2 = float(input('2ª Nota: '))
    nota3 = float(input('3ª Nota: '))
    nota4 = float(input('4ª Nota: '))
    media = (nota1 + nota2 + nota3 + nota4) / 4
    lista_media.append(media)
    print('=' * 15)
for med in lista_media:
    if med >= 7:
        media_maior += 1
print(f'Média de todos alunos: {lista_media}')
print(f'O número de alunos com média maior ou igual a 7.0: {media_maior} aluno(s)')