# Equivalente ao arquivo Dobro.py da aula
# Trabalhando com entrada numérica de usuários

#%%
numero = input("Entre com um número para encontrar o seu dobro: ")
dobro = numero * 2
print(f"O dobro de {numero} é : {dobro}")
# O input lê um valor do usuário em formato de string, por causa disso, é necessário fazer uma conversão de tipo
numero_convertido = int(numero) # Conversão de string para número inteiro
dobro = numero_convertido * 2
print(f"O dobro de {numero_convertido} é : {dobro}")

#%%
# Se multiplicar uma string por um valor escalar, irá repetir a string na quantidade declarada de escalar
nome = "Marcelo"
nomes = nome * 3
print(nomes)