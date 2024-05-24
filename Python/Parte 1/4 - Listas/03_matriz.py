# Define uma matriz (lista de listas) com três listas internas, cada uma contendo elementos diversos
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

# Imprime a primeira lista da matriz, que contém os elementos [1, "a", 2]
print(matriz[0])  # [1, "a", 2]

# Imprime o primeiro elemento da primeira lista da matriz, que é 1
print(matriz[0][0])  # 1

# Imprime o último elemento da primeira lista da matriz, que é 2, utilizando indexação negativa
print(matriz[0][-1])  # 2

# Imprime o último elemento da última lista da matriz, que é "c", utilizando indexação negativa
print(matriz[-1][-1])  # "c"

# Em Python, uma matriz é representada como uma lista de listas. 
# Portanto, matriz[0] retorna a primeira lista da matriz, matriz[0][0] retorna o primeiro 
# elemento da primeira lista, matriz[0][-1] retorna o último elemento da primeira lista usando
# indexação negativa, e matriz[-1][-1] retorna o último elemento da última lista usando indexação negativa.