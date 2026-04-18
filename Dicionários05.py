#Exercício 5: Limpeza de Banco de Dados (setor de TI): o sistema de e-commerce descontinuou alguns produtos. Você tem o dicionário:
#produtos = {“celular”: 1500, “camera”: 800, “radio”: 200, “fone”: 100}.
#O item “radio” deve ser removido por estar obsoleto. Crie um código que:
#1. Remova o item “radio” do dicionário usando o método .pop().
#2. Imprima o valor do produto que foi removido para fins de log.
#3. Verifique se o produto “celular” ainda existe no dicionário e imprima True ou False.

produtos = {"celular": 1500, "camera": 800, "radio": 200, "fone": 100}
produto_removido = "radio"
print(f'Item removido: {produtos.pop(produto_removido)}')
print(produtos)
celular_produtos = "celular" in produtos
print('Celular em estoque?', celular_produtos)

