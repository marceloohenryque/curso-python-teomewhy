# Desafio das aulas 09: Manipulação de arquivos
# Construa um programa que realiza o sorteio de um número entre 1 e 15.
# O usuário terá 3 chances de acertar o valor.
# A cada tentativa, deve-se informar se o chute é maior ou menor que o número
# sorteado. Caso o usuário acerte, parabenizâ-lo.

numero_sorteio = 7


# Téo utilizou aqui o Laço For para poder responder esta solução
# Eu tentei implementar utilizando o Laço While

numero_sorteado = 7
tentativa = 0

while True:
    tentativa += 1
    if tentativa == 6:  # O usuário terá 5 tentativas
        break

    numero_usuario = int(input("Entre com um número: "))
    if numero_sorteado == numero_usuario:
        print("Parabéns!\nVocê foi sorteado!\n")
        break
    elif numero_sorteado > numero_usuario:
        print("Lance baixo!\nTente novamente!\n")
    else:
        print("Lance alto!\nTente novamente!\n")
