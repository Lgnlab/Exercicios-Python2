total_gasto = cont = menor_valor = 0
nome_menor = ''
while True:
    nome = str(input('Nome do produto: '))
    valor = float(input('Preço: R$'))
    total_gasto += valor
    if valor > 1_000:
        cont += 1
    if valor > 0:
        menor_valor = valor
        nome_menor = nome
    elif valor < menor_valor:
        nome_menor = nome
    escolha = str(input('Quer continuar[S/N]? ')).strip().upper()[0]
    if escolha == 'N':
        break
print()
print(f'Total: R${total_gasto:.2f}\n{cont} Produtos custam mais de R$1000\nProduto mais barato: {nome_menor}')
