#Exercício 14
#Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?" "Esteve no local do crime?" "Mora perto da vítima?" "Devia para a vítima?" "Já trabalhou com a vítima?"
#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada
#como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

perguntas = ['Telefonou para a vítima?', 'Esteve no local do crime?', 'Mora perto da vítima?', 'Devia para a vítima?', 'Já trabalhou com a vítima?']
positivos = 0

for perg in perguntas:
    respostas = str(input(f'{perg}[S/N]')).strip().upper()[0]
    if respostas == 'S':
        positivos += 1
print('=' * 32)
if positivos == 2:
    print('Classificação: Suspeita')
elif positivos <= 4:
    print('Classificação: Cúmplice')
elif positivos == 5:
    print('Classificação: Assassino')
else:
    print('Classificação: Inocente')