#Exercício 45
#Desenvolver um programa para verificar a nota do aluno numa prova com 10 questões, o programa deve perguntar ao aluno a resposta de cada questão e ao final
#comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa).
#Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:


lista_a = []
lista_b = ['a', 'b', 'c', 'd', 'e', 'e', 'd', 'c', 'b', 'a']
acerto = 0
while True:
    for c in range(1, 11):
        resposta = str(input(f'Resposta da questão {c}ª: '))
        lista_a.append(resposta)
    sair = input('Quer verifcar mais alguma prova?[S/N]: ').strip().upper()[0]
    if sair == 'N':
        break
for a, b in zip(lista_a, lista_b):
    if a == b:
        acerto += 1
print(f'Respostas certas: {acerto}')
