#Exercício 3: Processamento de Vendas por Unidade (setor Comercial) Você tem uma lista de tuplas onde cada tupla representa uma venda:
#vendas_dia = [(“Monitor”, 900, 2), (“Teclado”, 150, 5), (“Mouse”, 80, 10)].
#Cada tupla contém (produto, preco_unitario, quantidade). Crie um loop for que use unpacking diretamente na estrutura do loop para extrair
#os três valores e, para cada item, imprima: “Produto: [nome] | Total: R$[preco * quantidade]”.

vendas_dia = [("Monitor", 900, 2), ("Teclado", 150, 5), ("Mouse", 80, 10)]

for produto, valor, quantidade in vendas_dia:
    print(f'Produto: {produto} - Total: R${valor * quantidade:.2f}')