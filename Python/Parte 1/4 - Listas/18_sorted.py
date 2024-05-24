# Define uma lista de linguagens de programação
linguagens = ["python", "js", "c", "java", "csharp"]

# Ordena a lista com base no comprimento das strings, em ordem crescente
print(sorted(linguagens, key=lambda x: len(x)))  # ["c", "js", "java", "python", "csharp"]

# Ordena a lista com base no comprimento das strings, em ordem decrescente
print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # ["python", "csharp", "java", "js", "c"]

# Este código ordena a lista de linguagens de programação, primeiro em ordem crescente com base no comprimento
# das strings e, em seguida, em ordem decrescente. Para isso, utiliza a função sorted() com o parâmetro key 
# definido como uma função lambda que retorna o comprimento de cada elemento. O primeiro print exibe a lista em
# ordem crescente e o segundo em ordem decrescente, de acordo com o comprimento das strings.