maior_idade = homem = mulheres = 0

while True:
    idade = int(input('Idade: '))
    sexo = str(input('sexo[M/F]: ')).upper().strip()[0]
    if idade > 18:
        maior_idade += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    escolha = str(input('Quer continuar[S/N]? ')).strip().upper()[0]
    if escolha == 'N':
        break
print()
print(f'{maior_idade} Pessoa(s) tem mais de 18 anos.\n{homem} Homens foram cadastrados.\n{mulheres} Mulher(es) tem menos de 20 anos.')
