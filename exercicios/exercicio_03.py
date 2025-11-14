'''Exercícios da aula 04.1
1- Faça um programa que conte quantas vezes a letra "a" aparece
em uma palavra.
2- Faça um programa que receba 4 alturas usando um laço de repetição e
realize soma dessas alturas.
3- Faça um programa que receba quam quantidade indefinida de valores
correspondentes a "saldo em conta. Porém, quando o usuario apertar "enter"
sem digitar valor algum, o programa para de receber valores, e exibe a
soma de todos os valores digitados anteriormente.
'''
#%%
# Questão 1
palavra = input("Digite uma palavra: ")


#%%
# Questão 02
soma = 0
quantidade_de_entradas = 4
while quantidade_de_entradas > 0:
    altura = input("Entre com um valor de altura: ")
    altura = float(altura)
    soma += altura
    quantidade_de_entradas -= 1
print("Soma das alturas:", soma)

#%%
# Questão 02 - For
soma = 0
quantidade_de_entradas = 4
for i in range(quantidade_de_entradas): # range(0, quantidade_de_entradas)
    altura = float(input("Entre com uma altura: "))
    soma += altura
print(f"Soma das alturas: {soma}")

#%%
# Questão 03 - While
saldo_Total = 0
while True:
    saldo = input("Entre com um saldo: ")
    if saldo == "":
        break # comando para forçar a saída do laço
    else:    
        saldo_Total += float(saldo)
print(f" O saldo total é de R${saldo_Total:.2f}")

