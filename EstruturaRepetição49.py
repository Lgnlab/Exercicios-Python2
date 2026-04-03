#Exercício 49
#Faça um programa que mostre os n termos da Série a seguir:
#S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
#Imprima no final a soma da série.

soma = 0
while True:
    numero1 = int(input('Numerador: '))
    numero2 = int(input('Denominador: '))
    calculo = numero1 / numero2
    soma += calculo
    sair = input('Quer adicionar mais números [S/N]? ').strip().upper()[0]
    if sair == 'N':
        break
print(f'Soma da série: {soma:.0f}')