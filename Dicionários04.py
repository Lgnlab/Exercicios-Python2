#Exercício 4: sistema de RH – Média de Desempenho (setor de RH): o RH armazena as últimas 3 notas de desempenho de cada funcionário num dicionário:
#desempenho = {“Lira”: [8, 9, 7], “Paula”: [10, 9, 10], “Tiago”: [6, 7, 8]}.
#O gestor quer saber a média da funcionária “Paula”. Crie um código que:
#Acesse a lista de notas da “Paula”.
#Calcule a média das notas (soma das notas dividida pela quantidade de notas). 3. Exiba o resultado: “A média de Paula foi [media]”.

desempenho = {"Lira": [8, 9, 7], "Paula": [10, 9, 10], "Tiago": [6, 7, 8]}
soma = 0
funcionaria_paula = desempenho["Paula"]
for media in funcionaria_paula:
    soma += media
print(f'Média Da Paula: {soma / 3:.1f}')
