# Define uma matriz (tupla de tuplas)
matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)

# Acessa e imprime a primeira tupla da matriz
print(matriz[0])  # (1, "a", 2)

# Acessa e imprime o primeiro elemento da primeira tupla da matriz
print(matriz[0][0])  # 1

# Acessa e imprime o último elemento da primeira tupla da matriz
print(matriz[0][-1])  # 2

# Acessa e imprime o último elemento da última tupla da matriz
print(matriz[-1][-1])  # "c"

# No caso da matriz matriz, matriz[0] retorna a primeira tupla da matriz, matriz[0][0]
# retorna o primeiro elemento da primeira tupla (que é 1), matriz[0][-1] retorna o último elemento 
# da primeira tupla (que é 2) e matriz[-1][-1] retorna o último elemento da última tupla da matriz (que é "c").