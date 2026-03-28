#Exercício 25
#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?"
#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
#Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
#Caso contrário, ele será classificado como "Inocente".

positivo = 0
print('Responda com [S/N]:')
p1 = str(input('Telefonou para a vítima? ')).strip().upper()[0]
if p1 == 'S':
    positivo += 1
p2 = str(input('Esteve no local do crime? ')).strip().upper()[0]
if p2 == 'S':
    positivo += 1
p3 = str(input('Mora perto da vítima? ')).strip().upper()[0]
if p3 == 'S':
    positivo += 1
p4 = str(input('Devia para a vítima? ')).strip().upper()[0]
if p4 == 'S':
    positivo += 1
p5 = str(input('Já trabalhou com a vítima? ')).strip().upper()[0]
if p5 == 'S':
    positivo += 1
if positivo == 2:
    print('SUSPEITA')
elif positivo < 4:
    print('CÚMPLICE')
elif positivo == 5:
    print('ASSASSINO')
else:
    print('INOCENTE')
