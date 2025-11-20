# Aprendendo sobre Funções
# Podemos utilizar também uma função dentro de outra função:

#%%

#%%
def soma(a: float, b :float) -> float:
    return a + b

def media(a: float, b: float) -> float:
    return soma(a,b)/2

# Declarando variáveis:
a = float(input("Entre com um valor de a: "))
b = float(input("Entre com um valor de b: "))
c = float(input("Entre com um valor de c: "))

#%%
# Pode-se também utilizar argumentos opcional:
# O c é o argumento opcional, ficam depois dos obrigatórios!
def nova_soma(d: float, e :float, f: float) -> float:
    return d + e + f
def nova_media(d: float, e: float, f=0.0) -> float:
    return nova_soma(d, e, f)/3

# Declarando variáveis:
d = float(input("Entre com um valor de a: "))
e = float(input("Entre com um valor de b: "))
f = float(input("Entre com um valor de c: "))


print(f"A média de {d}, {e} e {f} é {nova_media(d, e)}!")

#%%
# Para consertar a média devido a influência do argumento opcional
def new_sum(valores: list)->float:
    return  sum(valores)

def new_avarage(valores: list)->float:
    return new_sum(valores) / len(valores)

# Declarando variáveis:
g = float(input("Entre com um valor de g: "))
h = float(input("Entre com um valor de h: "))
i = float(input("Entre com um valor de i: "))

print(f"A média de g={g}, h={h}, i={i} é {new_avarage([g, h, i])}!")