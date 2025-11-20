# Aprendendo sobre API

# Extraindo dados da API de DOTA
# %%
# Adicionando bibliotecas
import requests
import pandas as pd

url = "https://api.opendota.com/api/heroes"
resposta = requests.get(url)
df = pd.DataFrame(resposta.json())
df

# Criando arquivo CSV usando pandas
df.to_csv("heroes_dota.csv", sep=";", index=False)
