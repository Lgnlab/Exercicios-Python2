#Exercício 13
#Faça um programa que receba a temperatura média de cada mês do ano e armazene-as numa lista. Após isto, calcule a média anual das temperaturas e mostre todas
#as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – janeiro, 2 – fevereiro, ...).

dados = []
soma = media = 0
for m in range(1, 13):
    mes = str(input(f'Mês {m}: '))
    temperatura = int(input('Média de temperatura do mês: '))
    dados.append([mes,temperatura])

for mt in dados:
    soma += mt[1]
    media = soma / len(dados)
print(f'Média anual de temperaturas: {media}')

for a in dados:
    if a[1] > media:
        print(f'{a[0]} = {a[1]}')
