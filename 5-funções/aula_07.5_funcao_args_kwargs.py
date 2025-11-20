# Aprendendo sobre Funções
# Argumentos Opcionais

# %%
# Sem utilizar listas e sim, usando valores inteiros.
# *args: lista ou conjuntos de elementos
# Neste caso, usamos *args: tudo que passar na função sem ser valor obrigatório
# o args atribui esses valores!
def soma_com_args(a, b, *args) -> float:
    valores = [a, b] + list(args)  # Args é uma tupla, então estamos
# convertendo
    return sum(valores)


def media_com_args(a: float, b: float, *args) -> float:
    return soma_com_args(a, b, *args) / (len(args) + 2)


a = float(input("Entre com um valor de a: "))
b = float(input("Entre com um valor de b: "))
c = float(input("Entre com um valor de c: "))
d = float(input("Entre com um valor de d: "))

print(f"A média é {media_com_args(a, b, c, d)}!")

# %%
# Criando função que recebe o preço de um produto e o imposto:

# **Kwargs: Cria um  argumento e se comporta como um dicionário, ou seja,
# argumentos nomeados para adicionar chave-valor.


def calculo_imposto(preco: float, taxa_base: float, **kwargs):
    imposto = preco * taxa_base

    for i in kwargs:
        print(i, kwargs[i])
        imposto += preco * kwargs[i]

    return imposto

# %%

# Melhores Práticas


impostos_gerais = {
    "municipio": 0.01,
    "estadual": 0.005,
    "nacional": 0.001,
    "internacional": 0.001,
}


calculo_imposto(100, 0.03, **impostos_gerais)
# É a mesma coisa que:
# calculo_imposto(100, 0.03, municipio=0.01, estadual=0.005, nacional:0.001)
