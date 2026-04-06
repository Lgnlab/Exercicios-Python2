#Exercício 04
#Faça um programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

letra = ''
while True:
    palavra = str(input('Digite uma palavra: ')).split()
    if len(palavra) > 10:
        print('Sua palavra não pode ter mais de 10 caracteres! Tente novamente.')
        continue
    else:
        break
letra = ''.join(palavra)
print('Consoantes:')
for l in letra:
    if l not in 'aeiou':
        print(l, end=' ')