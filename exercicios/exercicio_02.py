'''Exercício da aula 03.3_if
1- Faça um programa que vende uma garrafa de água:
    a) Se o cliente escolher água mineral natural, será cobrado R$1,50.
    b) Se o cliente escolher água mineral com gás, será cobrado R$2,50.
2- Altere o programa anterior para considerar a quantidade de água.
3- Faça o programa de uma sorveteria, onde o usuário pode escolher:
    a) Tipo de sorvete:
        - Casquinha (R$1,00)
        - Cascão (R$2,50)
        - Cestinha (R$4,00)
    b)  Sabor do Sorvete:
        - Morango
        - Creme
        - Chocolate
    c) Cobertura:
        - Caramelo (R$1,50)
        - Morango (R$1,50)
        - Chocolate (R$1,50)
        - Sem Combertura (R$0,00)
    Apresente o valor a ser pago
'''
# Questão 01
#%%
print("Bom dia!")
agua = input("Você vai querer água mineral ou água com gás")
if agua == "água mineral":
    print(f"A {agua} custa R$1,50")
elif agua == "água com gás":
    print(f"A {agua} custa R$2,50")
else:
    print("Não tem essa opção!")

# Questão 02
#%%
print("Bom dia!")
agua = input("Você vai querer água mineral ou água com gás")
agua_mineral = 1.5
agua_gas = 2.5
quantidade = int(input("Quantas você irá querer?"))
if agua == "água mineral":
    total = quantidade * agua_mineral
    print(f"A {agua} custa R${total:.2f}")
elif agua == "água com gás":
    total = quantidade * agua_gas
    print(f"A {agua} custa R${total:.2f}")
else:
    print("Não tem essa opção!")

# Questão 03
#%%
print("Bem-vindo a Sorveteria Gabmar")
print(
    "Temos as seguintes opções:\n"
    "* Casca:\n1- casquinha (R$1,50)\n2- cascão(R$2,50)\n3- cestinha (R$4,00)\n\n"
    "* Sabores:\n1- Morango\n2- Creme\n3- Chocolate\n\n"
    "* Cobertura:\n1- caramelo (R$1,50)\n2- morango (R$1,50)\n3- chocolate (R$1,50)\n4- sem cobertura (R$0,00)\n"
)
sorvete = int(input("Qual você casca você vai querer? "))
if sorvete == 1:
    print("Você escolheu a casquinha")
    total = 1.5
elif sorvete == 2:
    print("Você escolheu cascão")
    total = 2.5
elif sorvete == 3:
    total = 4.0
    print("Você escolheu a cestinha")
else:
    print("Nenhuma das opções")

sabor = int(input("Qual você sabor você vai querer? "))
if sabor == 1:
    print("Você escolheu a Morango")
elif sabor == 2:
    print("Você escolheu Creme")
elif sabor == 3:
    print("Você escolheu a Chocolate")
else:
    print("Nenhuma das opções")

cobertura = int(input("Qual você cobertura você vai querer? "))
if cobertura == 1:
    print("Você escolheu a Caramelo")
    total = total + 1.5
    print(f"O total deu R${total:.2f}")
elif cobertura == 2:
    print("Você escolheu Morango")
    total = total + 1.5
    print(f"O total deu R${total:.2f}")
elif cobertura == 3:
    print("Você escolheu a Chocolate")
    total = total + 1.5
    print(f"O total deu R${total:.2f}")
else:
    print("Sem cobertura!")
    total = total + 0
    print(f"O total deu R${total:.2f}")
