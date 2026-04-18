#Exercício 1: Localização de Entregas (setor de Logística): uma empresa de logística armazena as coordenadas de entrega em tuplas:
#coordenadas = (-23.5505, -46.6333).
#Crie um código que receba essa tupla e use o unpacking para extrair os valores em duas variáveis: latitude e longitude. Em seguida, exiba a mensagem:
#“Iniciando entrega. Latitude: [valor], Longitude: [valor]”.

coordenadas = (-23.5505, -46.6333)

latitude, longitude = coordenadas   # Unpacking Básico
print(f'Latitude: {latitude}\nLongitude: {longitude}')