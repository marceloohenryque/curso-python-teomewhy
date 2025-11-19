# Aprendendo sobre Manipulação de Arquivos
# %%

txt = "Este é um novo lorem ipsum\n"

nome_arquivo = "lorem_ipsum_2.txt"

# mode w = write
with open(nome_arquivo, mode="a") as open_file:
    open_file.write(txt)
