telefone = str(input('Digite o número de telefone: ')).strip()
telefone_limpo = telefone.replace('-', '')   #REMOVE O HIFEN E DEIXA SÓ OS NÚMEROS
print(f'Telefone Informado: {telefone}')

if len(telefone_limpo) == 7:
    print(f'Telefone possui 7 dígitos. Vou acrescentar o dígito três na frente.')
    novo_numero = '3' + telefone_limpo
    numero_formatado = novo_numero[:4] + '-' + novo_numero[4:]
    print(f'Telefone corrigido sem formatação: {novo_numero}')
    print(f'Telefone corrigido com formatação: {numero_formatado}')
else:
    print('O telefone não possui 7 dígitos ou já está correto.')