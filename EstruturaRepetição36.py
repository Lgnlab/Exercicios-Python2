#Exercício 36
#Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10,
#o valor inicial e final devem ser informados também pelo usuário.

numero = int(input('Tabuada: '))
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
for tab in range(inicio, fim + 1):
    print(f'{numero} X {tab} = {numero * tab}')
