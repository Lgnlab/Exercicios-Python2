#Exercício 1
#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

while True:
    numero = int(input('Informe um número entre 0 e 10: '))
    if numero > 10:
        continue
    else:
        break