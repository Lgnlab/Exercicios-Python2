#Exercício 2
#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

while True:
    nome_usuario = str(input('Nome De Usuário: '))
    senha = str(input('Senha: '))
    if nome_usuario == senha:
        print('Nome De Usuário ou Senha Inválidos!\nTente Novamente.')
        continue
    else:
        print('Login Autorizado')
        break