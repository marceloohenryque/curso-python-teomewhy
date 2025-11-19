# Aprendendo sobre Manipulação de Arquivos
# Arquivos CSV

# %%
arquivo = "data.csv"

with open(arquivo) as open_file:
    lines = open_file.readlines()  # Cada linha do arquivo virou uma lista
# A cada linha de uma planilha se chama registro

print(lines)
# %%
# Usando comando For
for l in lines:
    print(l)

# %%
# Criando uma estrutura de dicionário
# 1ª: Defiindo as chaves dos dicionários
# 2ª: 'Fatiando' a string
chaves = lines[0].strip("\n").split(';')
chaves

# 3ª: Criando um dicionário com todas as chaves
dados = dict()

# Percorrendo c em chaves
for c in chaves:
    dados[c] = []
dados

# 4ª: Alimentando o dicionário
for l in lines[1:]:  # Percorrendo todas as linhas a partir da 2ª
    valores = l.strip("\n").split(";")  # Removendo \n e separando entre ;

    # Percorrendo a quantidade de valores
    for i in range(len(valores)):  # Passando por todas as chaves desta dict
        dados[chaves[i]].append(valores[i])
        # Atribuição de valores no dict vazio
dados

# %%
# convertendo idades de string para inteiros
idades = []
for i in dados["idade"]:
    idades.append(int(i))

media = sum(idades)/len(idades)
media
