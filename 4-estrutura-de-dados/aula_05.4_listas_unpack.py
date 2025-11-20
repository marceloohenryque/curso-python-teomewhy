# Aprendendo sobre Listas - Aula Extra
# List Unpack: Descompactação de uma estrutura de dados
# Isso é utilizada em funções *args
# %%
# Exemplo
a = 1
b = 5
# %%
# O que podemos fazer para que a receba o valor de b e Vice-versa?
c = a
a = b
b = a
print(a)
print(b)

# %%
# Outra forma
a, b = b, a
print(a)
print(b)

# %%
# Outro exemplo
dados = {
    "nome": "Fulano",
    "sobrenome": "Beltrano"
}
for i, j in dados.items():
    print(i, j)

# %%
# Por que isso acontece?
# Essa parte do código funciona da mesma forma que o exemplo de dados
b, a = a, b  # Isso é uma tupla
print(a, b)
# Com isso, estamos fazendo um enpack da tupla. Criando um novo item
# da tupla.
# %%
# O que acontece para adicionar um terceiro elemento?
# a, b = "fulano", [1, 2, 3], 1.0
# print(a, b)
# A ausência de um terceiro atribuidor quebra o código
# Para
c, d, *resto = 1, 2, 3, 4, 6, 7, 8
print(a, b, resto)
# A presença do * na variável resto induz que os valores
# salvo após o 2º valor seja atribuído dentro desta
# variável

# %%
# Retornando os dois últimos elementos
*resto, e, f = 1, 2, 3, 4, 5, 6.759, 8.898
print(e, f, resto)

# Retornando o primeiro e último elemento
e, *resto, f = 1, 2, 3, 4, 5, 6.759, 8.898
print(e, f, resto)
