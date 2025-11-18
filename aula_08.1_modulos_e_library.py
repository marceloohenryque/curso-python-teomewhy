# Aprendendo sobre Módulos e biliotecas

# %%
# Importando bibliotecas
import math
import random

# Impostando apenas uma função da biblioteca
from math import pi

# %%
# Exemplo de raíz quadrada


def raiz_quadrada(numero):
    return numero ** (1/2)


print(raiz_quadrada(9))

# %%
# Importando biblioteca

# para acessar os recursos dessa biblioteca:
math.sqrt(9)

# %%
# Calculando
math.e

# %%
pi

# %%
random.randint(1, 10)
# %%
x = ["Fulano", "Beltrano", "Amina", "Cetona"]
random.choice(x)
