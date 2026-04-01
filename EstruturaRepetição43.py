#Exercício 43
#O cardápio de uma lanchonete é o seguinte:
#Especificação   Código  Preço
#Cachorro Quente 100     R$ 1,20
#Bauru Simples   101     R$ 1,30
#Bauru com ovo   102     R$ 1,50
#Hambúrguer      103     R$ 1,20
#Cheeseburguer   104     R$ 1,30
#Refrigerante    105     R$ 1,00
#Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido.
#Considere que o cliente deve informar quando o pedido deve ser encerrado.

total = 0
while True:
    codigo = int(input('Informe o código do lanche desejado: '))
    quantidade = int(input('Informe a quantidade: '))
    if codigo == 100:
        parcial = 1.20 * quantidade
        total += parcial
    if codigo == 101:
        parcial = 1.30 * quantidade
        total += parcial
    if codigo == 102:
        parcial = 1.50 * quantidade
        total += parcial
    if codigo == 103:
        parcial = 1.20 * quantidade
        total += parcial
    if codigo == 104:
        parcial = 1.30 * quantidade
        total += parcial
    if codigo == 105:
        parcial = 1.00 * quantidade
        total += parcial
    sair = input('Deseja algo mais [S/N]: ').strip().upper()[0]
    if sair == 'N':
        break
print(f'Total: R${total:.2f}')