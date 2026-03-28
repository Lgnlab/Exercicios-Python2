print(f'{"HIPERMERCADO TABAJARA":=^40}')
tipo_carne = str(input('Escolha Sua Carne[File Duplo-Alcatra-Picanha]: ')).strip().upper()[0]
cont_carne = float(input('Quantidade De Carne kg: '))
forma_pagamento = str(input('Cartão Tabajara[S/N]: ')).upper().strip()[0]
print('=' * 35)
if tipo_carne == 'F':
    if cont_carne <= 5:
        calculo_carne = cont_carne * 4.90
        print(f'Tipo Da Carne: File Duplo R$4,90 kg\nQuantidade kg: {cont_carne}kg\nTotal: R${calculo_carne:.2f}')
    else:
        calculo_carne = cont_carne * 5.80
        print(f'Tipo Da Carne: File Duplo R$5,80 kg\nQuantidade kg: {cont_carne}kg\nTotal: R${calculo_carne:.2f}')
    if forma_pagamento == 'S':
        desconto = calculo_carne * (5 / 100)
        print(f'Desconto De 5% Aplicado!\nTotal: R${calculo_carne - desconto:.2f}')
    else:
        print(f'Forma De Pagamento Sem O Cartão Tabajara!\nDesconto De 5% Não Aplicado.\nTotal: R${calculo_carne:.2f}')
elif tipo_carne == 'A':
    if cont_carne <= 5:
        calculo_carne = cont_carne * 5.90
        print(f'Tipo Da Carne: Alcatra R$5,90 kg\nQuantidade kg: {cont_carne}kg\nTotal: R${calculo_carne:.2f}')
    else:
        calculo_carne = cont_carne * 6.80
        print(f'Tipo Da Carne: Alcatra R$6,80 kg\nQuantidade kg: {cont_carne}kg\nTotal: R${calculo_carne:.2f}')
    if forma_pagamento == 'S':
        desconto = calculo_carne * (5 / 100)
        print(f'Desconto De 5% Aplicado!\nTotal: R${calculo_carne - desconto:.2f}')
    else:
        print(f'Forma De Pagamento Sem O Cartão Tabajara!\nDesconto De 5% Não Aplicado.\nTotal: R${calculo_carne:.2f}')
elif tipo_carne == 'P':
    if cont_carne <= 5:
        calculo_carne = cont_carne * 6.90
        print(f'Tipo Da Carne: Picanha R$6,90 kg\nQuantidade kg: {cont_carne}kg\nTotal: R${calculo_carne:.2f}')
    else:
        calculo_carne = cont_carne * 7.80
        print(f'Tipo Da Carne: Picanha R$7,80 kg\nQuantidade kg: {cont_carne}kg\nTotal: R${calculo_carne:.2f}')
    if forma_pagamento == 'S':
        desconto = calculo_carne * (5 / 100)
        print(f'Desconto De 5% Aplicado!\nTotal: R${calculo_carne - desconto:.2f}')
    else:
        print(f'Forma De Pagamento Sem O Cartão Tabajara!\nDesconto De 5% Não Aplicado.\nTotal: R${calculo_carne:.2f}')
print('=' * 35)