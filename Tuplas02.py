#Exercício 2: Resumo de Folha de Pagamento (setor de RH): crie uma função chamada calcular_folha que receba o salário bruto de um funcionário.
#A função deve calcular e retornar dois valores:
#O valor do desconto de impostos (fixado em 10%).
#O salário líquido (salário bruto – desconto). Após criar a função, chame-a para um salário de **R$ 5.000,00**, faça o unpacking do retorno e exiba:
#“Desconto: R$[valor] | Salário Líquido: R$[valor]”.

def calcular_folha(salar):
    imposto = salar * (10 / 100)
    liquido = salar - imposto
    return imposto, liquido

#Programa Principal
salario = float(input('Informe o salário bruto: R$'))
imposto, liquido = calcular_folha(salario)
print(f'Desconto: R${imposto:.2f}\nSalário Líquido: R${liquido:.2f}')
