# Aprendendo sobre Listas - Aula Extra
# List Comprehensions
# %%
# Criando lista a partir de um laço For
x = []
for i in range(1, 101):
    x.append(i)
x

# %%
# Outra forma:
# Estou colocando i dentro da iteração do laço for
y = [i for i in range(1, 101)]
y

# %%
# Exemplo: Este número é par ou não?


def numero_par(x):
    return x % 2 == 0


z = [numero_par(i) for i in range(1, 101)]
z
# %%
# Exemplo 2: Usando o exemplo 1 com filtro de Par
w = [i for i in range(1, 101) if numero_par(i)]
w
