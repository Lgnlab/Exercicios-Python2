#Exercício 06
#Faça um programa que converta a notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M.
#A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M.
#como um valor ‘A’ para A.M. e ‘P’ para P.M.
#Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário repita
#esse cálculo para novos valores de entrada todas às vezes que desejar.

def conversor(horas, minutos):
    calculo = None
    if horas > 12:
        calculo = horas - 12
        print(f'{calculo}:{minutos} P.M')
    elif horas == 00 and minutos == 00:
        print(f'12:00 A.M')
    else:
        print(f'{horas}:{minutos} A.M')

#Programa Principal
while True:
    try:
        hora = int(input('Informe as horas: '))
        minuto = int(input('Informe os minutos: '))
    except ValueError:
        print('\033[31mERRO! Informe um valor inteiro.\033[m')
    except TypeError:
        print('\033[31mERRO! Informe um valor inteiro.\033[m')
    else:
        conversor(hora, minuto)
        sair = str(input('Quer continuar?[S/N]')).upper().strip()[0]
        if sair == 'N':
            break