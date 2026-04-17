#Exercício 1: Atualização de Cadastro de Clientes (Setor de CRM): você tem um dicionário com o faturamento acumulado de alguns clientes:
#clientes = {“Lira”: 5000, “Alon”: 3000, “Julia”: 4500}.
#O cliente “Alon” fez uma nova compra de R$ 1.500,00. Crie um código que:
#1. Atualize o valor do cliente “Alon” somando o novo valor ao faturamento antigo. 2. Adicione um novo cliente chamado “Marcos” com um faturamento inicial de R$ 2.000,00.
#3. Exiba o dicionário atualizado.

clientes = {"Lira": 5000, "Alon": 3000, "Julia": 4500}
soma_compra = 0
for k, v in clientes.items():
    if k == 'Alon':
        soma_compra = v + 1500
print(f'Alon fez uma nova compra de R$1.500,00\nAcumulado Alon: R${soma_compra:.2f}')
clientes["Marcos"] = 2000
print(f'Dicionário atualizado: {clientes}')
