#Exercício 22
#Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados num vetor .
#Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar números aleatórios, simulando os lançamentos dos dados.

import random
contadores = [0] * 6
for i in range(100):
    dado = random.randint(1, 6)
    contadores[dado - 1] += 1
for i in range(6):
    print(f'Número {i+1}: {contadores[i]} vezes')