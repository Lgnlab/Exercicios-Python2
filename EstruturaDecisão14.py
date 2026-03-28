nota1 = float(input('Primeira Nota: '))
nota2 = float(input('Segunda Nota: '))
media = (nota1 + nota2) / 2

if media >= 9:
    print(f'Média:{media:.1f}\n\033[34mConceito A\033[m\n\033[32mAPROVADO\033[m')
elif media >= 7.5:
    print(f'Média:{media:.1f}\n\033[34mConceito B\n\033[32mAPROVADO\033[m')
elif media >= 6:
    print(f'Média:{media:.1f}\n\033[34mConceito C\n\033[mAPROVADO\033[m')
elif media >= 4:
    print(f'Média:{media:.1f}\n\033[34mConceito D\n\033[mREPROVADO\033[m')
elif media >= 0:
    print(f'Média:{media:.1f}\n\033[34mConceito E\n\033[mREPROVADO\033[m')