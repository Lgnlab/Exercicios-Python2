#Exercício 17
#Numa competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado pela média dos cinco valores restantes.
#Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta nos seus saltos e depois informe o nome, os saltos e a média dos saltos.
#O programa deve ser encerrado quando não for informado o nome do atleta.

saltos = []
soma = 0
while True:
    nome = str(input('Nome do Atleta: '))
    if nome == '':
        break
    else:
        for s in range(1, 6):
            salto = float(input(f'{s}ª Salto: '))
            soma += salto
            saltos.append(salto)
        print('=' * 35)
        print('Resultado Final:')
        print(f'Atleta: {nome}')
        print(f'Saltos: {saltos}')
        print(f'Média dos saltos: {soma / len(saltos):.1f}')
        saltos.clear()
        print('=' * 35)