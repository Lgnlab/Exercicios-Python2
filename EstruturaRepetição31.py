#Exercício 31
#O Sr. Manoel Joaquim expandiu os negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. Faça um programa que implemente uma caixa registradora rudimentar.
#O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra.
#O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco.
#Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra.

print(f'{"LOJAS TABAJARA":=^30}')
print()
cont = 1
total = 0
while True:
    produto = float(input(f'Produto {cont}: R$'))
    cont += 1
    total += produto
    if produto != 0:
        continue
    else:
        print(f'Total: R${total:.2f}')
        pagamento = float(input('Dinheiro do cliente: R$'))
        print(f'Dinheiro: R${pagamento:.2f}')
        troco = pagamento - total
        print(f'Troco: R${troco:.2f}')
        sair = input('Quer registrar outra compra [S/N]: ').upper().strip()[0]
        if sair == 'N':
            break