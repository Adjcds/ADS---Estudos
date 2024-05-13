# Define uma lista de linguagens de programação
linguagens = ["python", "js", "c", "java", "csharp"]

# Ordena a lista em ordem crescente
linguagens.sort()
print(linguagens)  # ["c", "csharp", "java", "js", "python"]

# Define uma lista de linguagens de programação
linguagens = ["python", "js", "c", "java", "csharp"]

# Ordena a lista em ordem decrescente
linguagens.sort(reverse=True)
print(linguagens)  # ["python", "js", "java", "csharp", "c"]

# Define uma lista de linguagens de programação
linguagens = ["python", "js", "c", "java", "csharp"]

# Ordena a lista com base no comprimento das strings, em ordem crescente
linguagens.sort(key=lambda x: len(x))
print(linguagens)  # ["c", "js", "java", "python", "csharp"]

# Define uma lista de linguagens de programação
linguagens = ["python", "js", "c", "java", "csharp"]

# Ordena a lista com base no comprimento das strings, em ordem decrescente
linguagens.sort(key=lambda x: len(x), reverse=True)
print(linguagens)  # ["python", "csharp", "java", "js", "c"]

# linguagens.sort(linguagens.sort(): Ordena a lista linguagens em ordem crescente.
# linguagens.sort(linguagens.sort(reverse=True): Ordena a lista linguagens em ordem decrescente.
# linguagens.sort(key=lambda x: len(x)): Ordena a lista linguagens com base no comprimento das strings em ordem crescente.
# linguagens.sort(key=lambda x: len(x), reverse=True): Ordena a lista linguagens com base no comprimento das strings em ordem decrescente.