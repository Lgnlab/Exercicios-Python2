#Exercício 3
#Faça um programa que leia e valide as seguintes informações:

#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Estado Civil: 's', 'c', 'v', 'd';

while True:
    nome = str(input('Nome: '))
    if len(nome) <= 3:
        print('Digite nome e sobrenome!')
        continue
    else:
        print('Nome Válido')
        break
while True:
    idade = int(input('Idade: '))
    if idade > 150:
        print('Idade Inválida! Tente novamente.')
        continue
    else:
        print('Idade Válida')
        break
while True:
    salario = float(input('Salário: R$'))
    if salario == 0:
        print('Salário Inválido! Tente novamente.')
        continue
    else:
        print('Salário Válido')
        break
while True:
    estado_civil = str(input('Estado Civil(S, C, V, D): ')).strip().upper()[0]
    if estado_civil == 'S' or 'C' or 'V' or 'D':
        print('Estado Civil Válido!')
        break
    else:
        print('Estado Civil Inválido! Tente novamente.')
        continue