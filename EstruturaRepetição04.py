pessoas_a = 80000
pessoas_b = 200000
anos = 0

while pessoas_a < pessoas_b:
    calculo_a = pessoas_a * (3 / 100)
    pessoas_a +=  calculo_a
    calculo_b = pessoas_b * (1.5 / 100)
    pessoas_b += calculo_b
    anos += 1
    if pessoas_a >= pessoas_b:
        break
print(f'População Do País A: {pessoas_a:.3f} - (quinhentos e quinze milhões, trinta e três mil, cento e três.)')
print(f'População Do País B: {pessoas_b:.3f} - (quinhentos e dez milhões, novecentos e sessenta e quatro mil, quatrocentos e dezessete.)')
print(f'Levou {anos} anos para o país A ultrapassar o país B')