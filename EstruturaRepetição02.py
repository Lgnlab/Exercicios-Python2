while True:
    nome_usuario = str(input('Nome De Usuário: '))
    senha = str(input('Senha: '))
    if nome_usuario == senha:
        print('Nome De Usuário ou Senha Inválidos!\nTente Novamente.')
        continue
    else:
        print('Login Autorizado')
        break