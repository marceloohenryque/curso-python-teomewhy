# Aprendeendo sobre laço de repetição While
# Usamos o while quando necessita de comparação lógica repetida

#%%
numero = 2

print("2 x 1 =", numero * 1)
print("2 x 2 =", numero * 2)
print("2 x 3 =", numero * 3)
print("2 x 4 =", numero * 4)
print("2 x 5 =", numero * 5)
print("2 x 6 =", numero * 6)
print("2 x 7 =", numero * 7)
print("2 x 8 =", numero * 8)
print("2 x 9 =", numero * 9)
print("2 x 10 =", numero * 10)

#%%
# Comando While cria um loop de repetição enquanto a condição for verdadeira
# Esse laço é para quando não sabemos quantas iterações se deve fazer.

# Criando uma condição de parada
count = 1

while count <= 10:
    print("Entre no laço", count)
    count += 1 # Usando incrementação para aumentar o valor a variável count

#%%
# Criando Tabuada usando while
count = 1
numero = 2
while count <= 100:
    print(f"{numero} x {count} = {numero * count}")
    count = count + 1
print("Fim da execução!")


#%%
# Quais números são divisíveis por 4 no intervalo de 4 a 100?
count = 4
while count <=100:
    resto = count %4
    if resto == 0:
        print(count)
    count += 1