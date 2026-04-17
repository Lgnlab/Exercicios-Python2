#Exercício 2: Consulta de Estoque Interativa (Setor de Logística): a empresa possui o seguinte estoque:
#estoque = {“teclado”: 50, “mouse”: 120, “monitor”: 30}.
#Crie um programa que peça para o usuário digitar o nome de um produto.
#1. Se o produto existir no estoque, exiba a quantidade disponível.
#2. Se o produto não existir, exiba a mensagem: “Produto não encontrado no sistema”. Dica: Lembre-se de tratar o input para evitar erros de letras maiúsculas ou espaços.

estoque = {"teclado": 50, "mouse": 120, "monitor": 30}
nome_produto = str(input('Nome do produto: ')).strip().lower()
status = False
for k, v in estoque.items():
    if nome_produto == k:
        print(f'O {nome_produto} já está cadastrado\nEstoque disponível: {v}')
        status = True
        break
if not status:
    print('Produto não encontrado no sistema')