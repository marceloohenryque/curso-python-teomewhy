# Equivalente ao arquivo idades.py da aula
# Aprendendo sobre Métodos de Listas
# Métodos são ações que um objeto Python pode ter.

idades = [17, 32, 56, 87]

#%%
# Método de adição de elementos
idades.append(32) # Este método modifica a própria lista, não cria uma nova lista.
                    # As listas são objetos mutáveis (modificáveis)
print(idades)

#%%
# Como fazer uma lista vazia
novas_idades = []

while True:
    idade = input("Entre com a idade: ")
    
    if idade == "":
        break
    
    novas_idades.append(int(idade))

quantidade = len(novas_idades)
media = sum(novas_idades) / len(novas_idades)
minimo = min(novas_idades)
maximo = max(novas_idades)

print(f"MEDIA: {media}")
print(f"MINIMO: {minimo}")
print(f"MAXIMO: {maximo}")
print(f"QUANTIDADE: {quantidade}")
