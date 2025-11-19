# Aprendendo sobre Manipulação de Arquivos

# %%
# Abrindo arquivos
nome_arquivo = "lorem_ipsum.txt"
open_file = open(nome_arquivo)
print(open_file)

# Exibindo conteúdo do texto
conteudo = open_file.read()
print(conteudo)
# Como fechar o arquivo
open_file.close()
# Garante a modificação do arquivo em outro software sem corrompê-lo

# %%
# Melhores práticas de leituras de arquivos

# Enquanto este arquivo estiver aberto, atribui o arquivo e a leitura dele
with open(open_file) as open_file:
    conteudo = open_file.read()
