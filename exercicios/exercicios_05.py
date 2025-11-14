'''Exercícios das aulas 6.1 e 6,2
1- considere a lista [120, "Python", 120.1, "aws", False, [10, 20]]
Faça um programa que retorne as seguintes informações:
    * Elemento da posição -1 da lista
    * Elemento na 1ª posição da lista
    * O último caractere do segundo elemento da lista
2- Solicite ao usuário o nome de uma fruta e exiba o preço correspondente
maçã R$1,50
pera R$1,25
goiaba R$2,15
banana R$2,75
laranja R$0,65
abacaxi R$3,20
uva R$1,90
limao R$1,25
jaca R$5,80

3- Escreva um programa que solicite ao usuário uma palavra. Para parar de solicitar
frases, ele pode apenas apertar o 'enter'.
Seu programa deve apresentar cada frase e quantas vezes ela foi repetida.
'''

#%%
# Questão 01
# a)
lista_ex01 = [120, "Python", 120.1, "aws", False, [10, 20]]
print(lista_ex01[-1])

# b)
print(lista_ex01[0])

# c)
print(lista_ex01[1][-1])

#%%
# Questão 02:
fruta_escolhida = input("Escolha uma fruta: maçã, pera, goiaba, banana, laranja, abacaxi, uva, limao ou jaca")
frutaria = {
    "maçã": "R$1.50",
    "pera": "R$1.25",
    "goiaba": "R$2.15",
    "banana": "R$2.75",
    "laranja": "R$0.65",
    "abacaxi": "R$3.20",
    "uva": "R$1.90",
    "limao": "R$1.25",
    "jaca": "R$5.80",
}
if fruta_escolhida in frutaria:
    print(f"A {fruta_escolhida} custa {frutaria[fruta_escolhida]}!")
else:
    print("Entre com um valor válido")

#%%
# Questão 03
dados = {}


while True:
    entrada_da_frase = input("Entre com uma frase: ")
    if entrada_da_frase == "":
        break
    
    if entrada_da_frase not in dados: # se a frase não estiver em dados
        dados[entrada_da_frase] = 1 # A frase aparece uma vez
    else:
        dados[entrada_da_frase] += 1 # A frase está aparecendo mais de uma vez

# Ordenando os valores
# Em dicionários, não se garante as ordem
# Por isso, podemos trabalhar com seus itens
itens = list(dados.items())
# O método .sort está ordenando os valores das chaves em ordem alfabética
itens.sort()
itens.sort(key=lambda x: x[-1], reverse=True)
#Key = Como fazer a ordenação
# O Lambda diz que faremos a ordenação a partir do último valor da tupla
# Com isso, o programa irá considerar do maior para o menor
for i, j in dados.items():
    print(f"{i} -> {j}")