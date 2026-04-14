#Exercício 20
#Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc). Carregue uma outra lista com o consumo desses carros,
#isto é, quantos quilômetros cada um desses carros faz com um litro de combustível. Calcule e mostre:
#O modelo do carro mais econômico;
#Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros e quanto isto custará,
#considerando um que a gasolina custe R$ 2,25 o litro.

modelo_carro = []
consumo_carro = []
menor_consumo = 0
nome_carro = ''
for carros in range(0, 5):
    nome = str(input('Nome do carro: '))
    consumo = float(input('Km por litro: '))
    modelo_carro.append(nome)
    consumo_carro.append(consumo)

print('Relatório Final:')
print('=' * 30)
for carro, consumo in zip(modelo_carro, consumo_carro):
    litros = 1000 / consumo
    if menor_consumo == 0:
        menor_consumo = litros
        nome_carro = carro
    elif menor_consumo > litros:
        menor_consumo = litros
        nome_carro = carro
    print(f'Carro: {carro} - Consumo: {consumo} - {litros:.1f} Litros - R${litros * 2.25:.2f}')
print(f'O menor consumo é do {nome_carro}')