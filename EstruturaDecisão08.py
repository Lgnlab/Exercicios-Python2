prod1 = float(input('Produto 1:R$'))
prod2 = float(input('Produto 2:R$'))
prod3 = float(input('Produto 3:R$'))
if prod1 < prod2 and prod1 < prod3:
    print(f'O produto 1 é mais barato R${prod1:.2f}')
elif prod2 < prod1 and prod2 < prod3:
    print(f'O produto 2 é mais barato R${prod2:.2f}')
else:
    print(f'O produto 3 é mais barato R${prod3:.2f}')