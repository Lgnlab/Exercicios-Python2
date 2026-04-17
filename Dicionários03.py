#Exercício 3: Análise de Faturamento por Região (Setor Financeiro): dada a lista de faturamento por região:
#vendas_regiao = {“norte”: 15000, “sul”: 22000, “leste”: 18000, “oeste”: 25000}.
#O programa deve:
#Extrair todos os valores (faturamentos) para uma lista.
#Calcular e exibir o faturamento total da empresa (soma de todas as regiões). 3. Calcular e exibir o faturamento médio das regiões.

vendas_regiao = {"norte": 15000, "sul": 22000, "leste": 18000, "oeste": 25000}
lista_faturamento = []
soma_faturamento = 0
for fat in vendas_regiao.values():
    soma_faturamento += fat
    lista_faturamento.append(fat)
print(f'Faturamento: {lista_faturamento}')
print(f'Faturamento total das regiões: R${soma_faturamento:.2f}')
print(f'Faturamento médio das regiões: R${soma_faturamento / len(lista_faturamento):.2f}')
