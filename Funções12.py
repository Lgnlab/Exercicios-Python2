#Exercício 12
#Embaralha palavra. Construa uma função que receba uma string como parâmetro e devolva outra string com os caracteres embaralhados.
#Por exemplo: se a função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória.
#Padronize na sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.

import random
letras = []
def embaralha_palavra(palavra='Vazio'):
    for c in palavra:
        letras.append(c)
        random.shuffle(letras)
    for e in letras:
        print(e, end='')


pal = str(input('Informe uma palavra: '))
embaralha_palavra(pal)