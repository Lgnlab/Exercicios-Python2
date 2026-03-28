#Exercício 10
#Faça um programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

celsius = float(input('Temperatura em °C'))
converte = (celsius * 9/5) + 32
print(f'De °C{celsius:.1f} para °F{converte:.1f}')
