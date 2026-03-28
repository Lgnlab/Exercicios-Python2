#Exercício 14
#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média.
#A atribuição de conceitos obedece à tabela abaixo:

#Média de Aproveitamento  Conceito
#Entre 9.0 e 10.0         A
#Entre 7.5 e 9.0          B
#Entre 6.0 e 7.5          C
#Entre 4.0 e 6.0          D
#Entre 4.0 e zero         E
#O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

nota1 = float(input('Primeira Nota: '))
nota2 = float(input('Segunda Nota: '))
media = (nota1 + nota2) / 2

if media >= 9:
    print(f'Média:{media:.1f}\n\033[34mConceito A\033[m\n\033[32mAPROVADO\033[m')
elif media >= 7.5:
    print(f'Média:{media:.1f}\n\033[34mConceito B\n\033[32mAPROVADO\033[m')
elif media >= 6:
    print(f'Média:{media:.1f}\n\033[34mConceito C\n\033[mAPROVADO\033[m')
elif media >= 4:
    print(f'Média:{media:.1f}\n\033[34mConceito D\n\033[mREPROVADO\033[m')
elif media >= 0:
    print(f'Média:{media:.1f}\n\033[34mConceito E\n\033[mREPROVADO\033[m')