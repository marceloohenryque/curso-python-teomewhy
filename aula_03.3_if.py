# Aprendendo sobre Fluxo Condicional

idade = int(input("Qual a sua idade? "))

if idade >=70:
    print("Cuidado com a bebida! \nVerifique com seu geriatra!")
elif idade >= 18:
    print("Você pode beber cerveja! \nBeba com moderação!")
# Python funciona com identação. Isso representa a mesma forma que {} em outras linguagens de programação
elif idade == 17:
    print("Ainda não pode beber cerveja! \nFique no Refrigerante!")
else:
    print("Você não pode beber cerveja! \nVá para casa beber leite!")