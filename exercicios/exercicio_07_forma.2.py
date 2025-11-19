# Desafio das aulas 09: Manipulação de arquivos
# Construa um programa que realiza o sorteio de um número entre 1 e 15.
# O usuário terá 3 chances de acertar o valor.
# A cada tentativa, deve-se informar se o chute é maior ou menor que o número
# sorteado. Caso o usuário acerte, parabenizâ-lo.

numero_sorteio = 7

import random


def get_input():
    while True:
        try:
            numero_usuario = int(input("Entre com um número: "))
        
        except ValueError as err:
            print("Valor inválido!")
            continue

        if 1 <= numero_usuario <= 15:  # Limitando o intervalor
            return numero_usuario
        
        print("Valor Inválido! O valor deve ser entre 1 e 15!")

def check_number(numero_sorteio, numero_usuario):
    if numero_sorteio == numero_usuario:
        print("Parabéns!\nVocê foi sorteado!\n")
        return True

    elif numero_sorteio > numero_usuario:
        print("Lance baixo!\nTente novamente!\n")
        return False

    else:
        print("Lance alto!\nTente novamente!\n")
        return False

numero_sorteio = random.randint(1, 15)


for i in range(3):
    numero_usuario = get_input()
    if check_number(sorteio=numero_sorteio, usuario=numero_usuario):
        break
else:
    print("Suas tentativas acabaram!")
