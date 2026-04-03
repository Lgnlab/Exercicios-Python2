#Exercício 46
#Numa competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados.
#O seu resultado fica sendo a média dos três valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta nos saltos e depois
#informe a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média). Faça uso de uma lista para armazenar os saltos.
#Os saltos são informados na ordem da execução, portanto não são ordenados. O programa deve ser encerrado quando não for informado o nome do atleta.

lista_saltos = []
maior_salto = menor_salto = soma_saltos = 0
while True:
    nome = str(input('Nome do atleta: ')).strip()
    if nome == '':
        break
    for s in range(1, 6):
        salto = float(input(f'{s} Salto: '))
        soma_saltos += salto
        lista_saltos.append(salto)
        for l in lista_saltos:
            if l > maior_salto:
                maior_salto = l
                menor_salto = l
            if l < menor_salto:
                menor_salto = l
    print(f'Atleta {nome}:')
    print(f'Melhor salto: {maior_salto:.1f} m')
    print(f'Pior salto: {menor_salto:.1f} m')
    print(f'Média dos saltos: {soma_saltos / 5:.1f} m')