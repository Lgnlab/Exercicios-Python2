#Exercício 15
#Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado
#um valor igual a −1 (que não deve ser armazenado). Após esta entrada de dados, faça:
#Mostre a quantidade de valores lidos;
#Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
#Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
#Calcule e mostre a soma dos valores;
#Calcule e mostre a média dos valores;

numeros = []
soma = 0
while True:
    nota = float(input('Nota: '))
    if nota == -1:
        break
    else:
        numeros.append(nota)

print(f'Quantidade de valores lidos: {len(numeros)}')
print(f'Valores lidos na ordem informada: {numeros}')
lista_invertida = numeros[::-1]
print(f'Lista invertida:')
for i in lista_invertida:
    soma += i
    print(i)
print(f'Soma dos valores informados: {soma:.1f}')
print(f'Média dos valores: {soma / len(numeros):.1f}')


