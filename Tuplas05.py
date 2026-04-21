#Exercício 5: Gestão de Chamados de suporte (setor de TI): o sistema de chamados precisa de um resumo diário.
#Crie uma função resumo_chamados que receba uma lista com tempos de resposta (em minutos). Ela deve retornar a
#quantidade de chamados e o tempo máximo de espera. Teste a função com a lista tempos = [15, 45, 10, 120, 30].
#Desempacote os resultados e exiba uma mensagem formatada alertando sobre o tempo máximo encontrado.

def resumo_chamados(lista_tempo_chamado):
    quantidade_chamados = len(lista_tempo_chamado)
    tempo_espera = max(lista_tempo_chamado)
    return quantidade_chamados, tempo_espera

#Programa Principal
lista_tempos = [15, 45, 10, 120, 30]
qtde, tempo_maximo = resumo_chamados(lista_tempos)
print(f'Quantidade de chamados: {qtde}\nTempo máximo de espera: {tempo_maximo}')