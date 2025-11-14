# Aprendendo sobre Estruturas de Dados
# Tupla: É uma lista imutável

#%%
# Relembrando lista
dados_fulano = [32, 1, "Solteiro", "estudante de Ciência da Computação"]
dados_fulano

# Adicionando elemento na lista
dados_fulano.append("1200")
dados_fulano

#%%
# Tupla
# Existem duas formas de declarar umad tupla
# 1ª opção:
# tupla_fulano = (32, 1, "Solteiro", "estudante de Ciência da Computação")
# 2ª opção:
tupla_fulano = (32, 1, "Solteiro", "estudante de Ciência da Computação", ["Amina", "Ester"])
print(type(tupla_fulano))
print(tupla_fulano)


# Um dos exemplos seria a busca de um dados do banco de dados
# e você não quer que eles sejam alterados, pode-se adicionar
# em uma tupla para manter a integridade destes dados.

#%%
# Caso tenha uma lista dentro de uma tupla, é possível modificar ela:
tupla_fulano[-1]
tupla_fulano[-1].append("Cetona") # Aqui adicionamos um elemento dentro da lista
print(tupla_fulano)
