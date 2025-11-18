# Aprendendo sobre Estruturas de Dados

# %%
# Listas são conjuntos ou coleção ordenada e mutávies de elementos.

# IMPORTANTE: Listas em Python não são os Arrays

# São utilizadas para armazenar coleções de itens do mesmo tipo ou
# quando a ordem e a capacidade de alteração são importantes.
idades = [28, 42, 43, 35, 39, 28, 38]
print(idades)

fulano = ["Fulano", "Ciclano", 45, True, "Solteiro", 2342.98]
print(fulano)

# Para descobrir o tipo de uma variável
type(fulano)

# %%
# Acessando os elementos de uma lista
# 1- Chame a variável que contém a lista;
# 2- Abre Cochetes e utilize como parâmetros o índice correspondete
# ao elemento que você quer acessar.
# OBS.: Os índices em python começam em 0!


# Acessando idade
print(fulano[2])

# renda
print(fulano[5])

# nome
print(fulano[0])

# %%
# Funções com listas

idades = [28, 42, 43, 35, 39, 28, 38]

# Soma
soma = sum(idades)
print(f"Soma das idades: {idades}")

# Média
media = sum(idades)/len(idades)
print(f"A média das idades é: {media}")

# Mínimo
print(f"A menor idade é:  {min(idades)}")

# Máximo
print(f"A menor idade é: {max(idades)}")

# %%

# Lista dentro de lista
fulano = ["Fulano Beltrano", 45,
          True, "Solteiro",
          ["estagiario", "ds jr", "ds pl", "ds sr.", "head"],
          [1500, 4000, 4550, 6500, 10000],
          ["Amina", "Ester", "Cetona"]
          ]

print("tamanho de fulano", len(fulano))

# %%
# Navegando sobre as listas
fulano[4]  # Acessando uma lista
fulano[4][0]  # Acessando a lista dentro da lista
exs = fulano[6]
primeira_ex = exs[0]
print(primeira_ex)

# %%

# Descobrindo o último elementod de uma lista de N elementos
tamanho = len(fulano)
posicao = tamanho - 1

exs = fulano[posicao]

# Resgatando o último elemento da lista baseando no tamanho
fulano[posicao][len(exs)-1]

# %%

# Outra maneira de acessar o último elemento da lista
fulano[-1][-1]

# Acessando o penúltimo elemento da lista
fulano[-1][-2]

# %%
# Fatiamento de lista
fulano

fulano[0:3]  # O python trabalha com intervalo aberto, neste caso, não irá
# pegar o último elemento, por isso não irá acessar o estado civil

fulano[0:4]  # Acessa o estado civil

# fulano[ start : stop ] | [ : ] -> pega todos elementos da lista
# Acessando as últimas posições de cargos do fulano
fulano[4][-2:5]


# %%
# Acessar a ordem inversa da lista
salario = fulano[5]
salario[::-1]
# Fulano[ start : stop : step] -> step: indica como será o comportamento
# de percorrer a lista
