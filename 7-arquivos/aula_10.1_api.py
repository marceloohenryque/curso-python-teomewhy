# Aprendendo sobre API

# Aplication Programming Interface (API) são conjunto de regras
# e protocolos que permitem diferentes sistemas de software se
# comuniquem entre si, atuando como intermerdiarios para troca
# de dados e funcionalidade.

# Nesta aula, iremos usar de API o HTTP (HyperText Transfer Protocol)

# Importando biblioteca para acessar API

# %%
import requests  # Biblioteca para acessar API / requisição na web
import json  # Biblioteca para salvar dados json
# tratar lista ou dict para json

from tqdm import tqdm  # Biblioteca para medir de progresso

import pandas as pd

# %%
# Endereço de internet
url = "https://viacep.com.br/ws/68447000/json/"

# Fazendo requisição
# usando o get, estamos solicitando informações da internet
resposta = requests.get(url)  # Consumindo dados de uma API

# %%
print(resposta)
# A saída <Response [200]> significa que a requisição foi concluída.

# %%
# Verificando as informações da API
resposta.text  # Este atributo mostra o conteúdo da API

# %%
# A API devolve um arquivo de formato json e podemos acessa-lo
# da seguinte maneira.
dados = resposta.json()
dados

# Verificando o tipo do arquivo json
print("Este arquivo possui um formato", type(dados))
# O formato json está sendo convertido para dict em Python

# %%
# Trabalhando com listas de ceps
ceps = [
    "01310200",
    "22031050",
    "30130110",
    "40060010",
    "50030120",
    "60060230",
    "70070120",
    "80010020",
    "88030010",
    "90035230",
    ]

# Obtendo todos os dados desse cep usando For
nova_url = "https://viacep.com.br/ws/{cep}/json/"  # aplicando placeholder
novos_dados = []  # Armazenamento dos ceps
# for i in ceps: Sem a biblioteca tqdm
for i in tqdm(ceps):  # É usado para poder medir progresso
    resposta = requests.get(nova_url.format(cep=i))
    # Obtenho a resposta da request
    # cep=i: pegando o valor do cep e substitui por i
    if resposta.status_code == 200:  # Checando o status da resposta
        novos_dados.append(resposta.json())  # Transforma a resposta em json
        # e adiciono na lista novos_dados
novos_dados

# %%
# Visualizando esses novos dados
print(novos_dados)

# Salvando os dados em um novo arquivo
# Abre arquivo ceps.json em forma de escrita
# enconding = 'UTF-8: conversão de string para Unicode Characters
with open("ceps.json", "w", encoding='UTF-8') as open_file:
    json.dump(novos_dados, open_file, ensure_ascii=False, indent=4)
    # método dump: converter arquivo python em json
    # Pega os dados do arquivo aberto em formato de escrita,
    # ignora ascii e formatação de identação.

# %%
# Trabalhando com Visualização de dados
dataset = pd.DataFrame(novos_dados)
dataset.to_csv("ceps.csv", sep=";")  # criando um arquivo csv
