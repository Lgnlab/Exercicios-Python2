#Exercício 27
#Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma.
#As turmas não podem ter mais de 40 alunos.

while True:
    quant_alunos = int(input('Alunos: '))
    turma = int(input('Turmas: '))
    calculo = quant_alunos / turma
    if calculo > 40:
        continue
    else:
        break
print(f'Média: {calculo:.0f} alunos por turma')