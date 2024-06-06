# Lembre-se de substituir o caminho abaixo pelo caminho completo do arquivo no seu sistema!

arquivo = open(
    "C:/Users/adrie/OneDrive/Imagens/Back-end/teste.txt", "w"
)
arquivo.write("Escrevendo dados em um novo arquivo.")
arquivo.writelines(["\n", "escrevendo", "\n", "um", "\n", "novo", "\n", "texto"])
arquivo.close()
