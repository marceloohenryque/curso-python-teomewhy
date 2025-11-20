# Aprendendo sobre Funções
# uma das melhores práticas sobre funções é pdoer documentar para um outro usuário
# do que se trata a função criada, quais são os parâmetros e seus tipos, qual o
# resultado gerado e implementado boas práticas
#%%
# Retornando ao Exemplo de funções de números compostos
# Juros Compostos: f(x) = 1000 * 1,13**x
# Aporte aplicado: 1000
# Taxa ao ano: 1,13
# Ano: x
def juros_compostos(aporte: int, taxa: float, anos: int) -> float:
    """juros_compostos: serve para calcular o retorno financeiro a partir de um aporte.
    Deve-se considerar: valor, a taxa de juros atual e o tempo(anos) para realização
    do cálculo do valor a ser retornado.

    Args:
        aporte (int): representa o valor em reais.
        taxa (float): número entre 0 e 1 que represente o valor da taxa de juros.
        anos (int): representa o tempo de investimento que terá liquidez, deve ser >= 1.

    Returns:
        _type_: _description_
    """
    return aporte * ( 1 + taxa) ** anos

# melhores praticas
# Explícito é melhor que implícito - Zen Python
juros_compostos(aporte=1000, taxa=0.13, anos=4)

#%%
# Exemplo de tarifa de Táxi
# Em uma determinada cidade, as tarifas de táxi consistem em um valor inicial de
# R$ 4,00 mais R$ 0,25 a cada 140 metros percorridos. Escreva uma função que recebe como
# seu único parâmetro a distância percorrida em quilômetros, e retorna como seu único
# resultado o valor total da corrida. Escreva um programa principal que demonstre o
# funcionamento de sua função.

# Tarifa de Táxi: 4 + 0.25x

def tarifa_de_taxi(distância_percorrida: float):
    """tarifa_de_taxi: Realiza um cálculo de tarifas de uma corrida de taxi a partir de uma
    distância percorrida (metros) e tem seu resultado final dado em quilômetro.
    
    Args:
        distância_percorrida (float): Representa a distância da corrida (metros).

    Returns:
        valor_total: Representa o valor total da tarifa da corrida, já convertida em
        quilômetro.
    """
    taxa_fixa = 4
    # metros -> quilometros: 1 * 1000
    conversao_quilometro = distância_percorrida * 1000
    trecho_percorrido = conversao_quilometro / 140
    taxa_variavel = 0.25 * trecho_percorrido
    valor_total = taxa_fixa + taxa_variavel
    return valor_total

tarifa_de_taxi(distância_percorrida = 140)