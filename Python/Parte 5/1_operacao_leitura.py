# Lembre-se de substituir "C:/caminho/do/arquivo/lorem.txt" pelo caminho completo do arquivo no seu sistema!

# Abre o arquivo em modo de leitura e imprime todo o seu conteúdo
arquivo = open(
    "C:/Users/adrie/OneDrive/Imagens/Back-end/lorem.txt", "r"
)
print(arquivo.read())
arquivo.close()

# Abre o arquivo em modo de leitura, lê apenas a primeira linha e imprime
arquivo = open(
    "C:/Users/adrie/OneDrive/Imagens/Back-end/lorem.txt", "r"
)
print(arquivo.readline())
arquivo.close()

# Abre o arquivo em modo de leitura, lê todas as linhas e imprime
arquivo = open(
    "C:/Users/adrie/OneDrive/Imagens/Back-end/lorem.txt", "r"
)
print(arquivo.readlines())
arquivo.close()

# Abre o arquivo em modo de leitura e imprime todas as linhas usando um loop while
arquivo = open(
    "C:/Users/adrie/OneDrive/Imagens/Back-end/lorem.txt", "r"
)
while len(linha := arquivo.readline()):
    print(linha)
arquivo.close()
