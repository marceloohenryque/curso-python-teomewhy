# Aprendendo sobre Funções
# O que são Funções: Em matemática, as funções são relações de conjuntos,
# ou seja, uma associação entre um elemento de entrada (Domínio) com um
# elemento de saída (Contra-domínio). Ela é bem importante para descrever
# comportamentos matemáticos que acontecem em diversos aspectos multi-
# disciplinares.

# Dentro da programação, elas são essenciais para reutilização
# de tarefas códigos, tornando-o mais limpo e estruturado.

#%%
# Função existentes

# São funções já determinadas pela linguagem Python para que seja executada.
print("Hello World!")

nome = input("Entre com o seu nome: ")
print(nome)
#%%
# Criando Funções
# f(x) = x + 1

def f(x):
    resultado = 1 + x
    return resultado

f(0)
#%%
# Exemplo de funções de números compostos
# Juros Compostos: f(x) = 1000 * 1,13**x
# Montante aplicado: 1000
# Taxa ao ano: 1,13
# Ano: x
def juros_compostos(x):
    resultado = 1000 * (1.13**x)
    return resultado

juros_compostos(4) # É necessário declarar os parâmetros na ordem correta!