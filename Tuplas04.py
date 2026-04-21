#Exercício 4: Performance de Vendas Regionais (setor de Dashboard): crie uma função chamada analisar_vendas que receba uma lista de números (vendas).
#A função deve retornar o total vendido e a média das vendas. Dado o dicionário:
#dados_filiais = {“Matriz”: [10000, 15000, 20000], “Filial Sul”: [5000, 7000]}:
#1. Percorra o dicionário.
#2. Para cada filial, use a função e faça o unpacking do resultado.
#3. Exiba: “Filial [Nome] -> Total: R$[valor],Média: R$[valor]”.


def analisar_vendas(lista_vendas):
    soma_vendas = sum(lista_vendas)
    media_vendas = soma_vendas / len(lista_vendas)
    return soma_vendas, media_vendas

dados_filiais = {"Matriz": [10000, 15000, 20000], "Filial Sul": [5000, 7000]}
for filial in dados_filiais:
    vendas_filial = dados_filiais[filial]
total_vendas_filial, media_vendas_filial = analisar_vendas(vendas_filial)

print(
    f"Filial {filial} -> "
    f"Total: R${total_vendas_filial}, "
    f"Média: R${media_vendas_filial}"
)