#Exercício 07
#Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

#Quantos espaços em branco existem na frase.
#Quantas vezes aparecem as vogais a, e, i, o, u.

frase = str(input('Informe uma frase: ')).lower()
print(f'Espaços em branco na frase: {frase.count(' ')}')
vog_a = vog_e = vog_i = vog_o = vog_u = 0
for vogais in frase:
    if vogais == 'a':
        vog_a += 1
    if vogais == 'e':
        vog_e += 1
    if vogais == 'i':
        vog_i += 1
    if vogais == 'o':
        vog_o += 1
    if vogais == 'u':
        vog_u += 1
print(f'Vogal a: {vog_a}')
print(f'Vogal e: {vog_e}')
print(f'Vogal i: {vog_i}')
print(f'Vogal o: {vog_o}')
print(f'Vogal u: {vog_u}')