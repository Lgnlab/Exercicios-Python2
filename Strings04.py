nome = str(input('Digite seu nome: ')).upper()
for letra in range(1, len(nome) + 1):
    print(nome[:letra])