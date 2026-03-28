#Exercício 09
#Faça um programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

fahr = float(input('Infome a temperatura em °F'))
convertendo = 5 * ((fahr - 32) / 9)
print(f'Convertendo °F{fahr:.1f} para °C{convertendo:.1f}')