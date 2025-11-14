# Aprendendo sobre Estruturas de Dados

#%%

# Relembrando listas
lista = [2, 132, "fulano", ["ds", "de", "da"], True]
lista[2]

#%%
# Dicionários: São pares de chave-valor, isto é, tem-se uma chave que corresponde
# a um único valor associado a ela.

# Pares chave/valor
# Adiciona primeiro a chave e depois o valor correspondente a esta chave
# As chaves podem ser tanto Strings quanto Inteiros (Float também mas não é recomendado!)
# Já os valores podem ser de quaisquer tipos.
dados_fulano = {
    "nome":"fulano",
    "sobrenome":"beltrano",
    "filhos":True,
    "formação":["ciência da computação", "engenharia de dados"],
    "cargos": [ # Neste caso, o valor é uma lista e cada elemento é um dicionário
        {"nome": "estágio", "empresa": "Datainfo"},
        {"nome": "de jr.", "empresa": "Datainfo"},
        {"nome": "de pl.", "empresa": "Senior Sistemas"},
        {"nome": "de sr.", "empresa": "Amcom"},
        {"nome": "de espec..", "empresa": "Phillips"},
    ]
}
print(dados_fulano)

#%%
# Acessando dados do dicionário
#dados_fulano[0] # Não há como acessar pois não existe chave 0

# Acessando o último elemento de formação
dados_fulano["formação"][-1]

# Acessando dados de dicionário de lista
print(dados_fulano["cargos"][-1]["empresa"]) # Isto é muito utilizado em chamada de API's

#%%
# Atribuindo uma chave nova no dicionário
dados_fulano["estado civl"] = "solteiro"
print(dados_fulano)

#%%
# Como descobrir os nomes das chaves
# Keys é um métodos
print(f"Chaves: {dados_fulano.keys()}")
print("\n")
# Descobrindo os nomes dos valores
print(f"Valores: {dados_fulano.values()}")
print("\n")
# Mostrando os pares de chaves-valores
print(f"Itens: {dados_fulano.items()}")

#%%
# Como percorrer dicionário
# 1ª forma:
for i in dados_fulano:
    print(f"{i}: {dados_fulano[i]}")
print("\t")

# 2ª forma:
for chave in dados_fulano:
    print(f"{chave} -> {dados_fulano[chave]}")
print("\t")

# 3ª Forma:
## [chave, valor] = i, j
for [chave, valor] in dados_fulano.items():
    print(f"{chave} -> {valor}")