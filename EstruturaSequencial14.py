peso = float(input('Peso do peixe: kg'))
peso_maior = peso - 50
multa = peso_maior * 4
print(f'O peixe ultrapassou {peso_maior}kg dos 50.0kg estabelecidos. Multa  R${multa:.2f}')