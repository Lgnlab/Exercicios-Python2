#Exercício 18
#Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma.
#O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores
#além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor.
#Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete

opcoes = [0, 1, 2, 3, 4, 5, 6]
escolha = []
windows_server = unix = linux = netware = mac_os = outro = 0
total_votos = 0

print('Qual o melhor Sistema Operacional para uso em servidores?')
while True:
    votos = int(input('Voto: '))
    if votos not in opcoes:
        print('Voto Inválido! Tente Novamente.')
        continue
    if votos == 0:
        break
    else:
        escolha.append(votos)
for cont in escolha:
    if cont == 1:
        total_votos += 1
        windows_server += 1
    if cont == 2:
        total_votos += 1
        unix += 1
    if cont == 3:
        total_votos += 1
        linux += 1
    if cont == 4:
        total_votos += 1
        netware += 1
    if cont == 5:
        total_votos += 1
        mac_os += 1
    if cont == 6:
        total_votos += 1
        outro += 1

porc1 = (windows_server / total_votos) * 100
porc2 = (unix / total_votos) * 100
porc3 = (linux / total_votos) * 100
porc4 = (netware / total_votos) * 100
porc5 = (mac_os / total_votos) * 100
porc6 = (outro / total_votos) * 100

print(f'''
{"Sistema operacional":^25} {"Votos":^15} {"%":^10}
{"-"*25} {"-"*15} {"-"*10}
{"Windows Server":^25} {windows_server:^15} {porc1:^10.0f}%
{"Unix":^25} {unix:^15} {porc2:^10.0f}%
{"Linux":^25} {linux:^15} {porc3:^10.0f}%
{"Netware":^25} {netware:^15} {porc4:^10.0f}%
{"Mac OS":^25} {mac_os:^15} {porc5:^10.0f}%
{"Outro":^25} {outro:^15} {porc6:^10.0f}%
{"-"*25} {"-"*15}
{"Total":^25} {total_votos:^15}
''')



