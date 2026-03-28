#Exercício 01
#Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento.
#Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

frase1 = str(input('Frase 1: ')).strip()
frase2 = str(input('Frase 2: ')).strip()
print(f'Tamanho de "{frase1}": {len(frase1)} caracteres')
print(f'Tamanho de "{frase2}": {len(frase2)} caracteres')
if len(frase1) == len(frase2):
    print('As duas strings são de tamanhos iguais.')
else:
    print('As duas strings são de tamanhos diferentes.')
if frase1 == frase2:
    print('As duas strings possuem conteúdo iguais.')
else:
    print('As duas strings possuem conteúdo diferente.')