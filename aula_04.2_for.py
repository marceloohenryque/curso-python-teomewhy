# Aprendendo sobre o laço de Repetição For
# Usa-se o For quando você quer percorrer os elementos
#%%
nome = "Fulano"
for letra in nome:
    print(letra)

#%%
numero = 2
max_numero = 100
# range() é uma estrutura de python para criação de sequencia numérica
# o range() trabalha com intervalo aberto, isso significa que ele 
# não considera o último valor!
for iteracao in range(1, max_numero+1):
    print(f"{numero} x {iteracao} = {numero * iteracao}")


#%%
# Quais números são divisíveis por 4 no intervalo de 4 a 100?
for i in range(4, 100):
    if i % 4 == 0:
        print(i)