# Define um conjunto de números com elementos duplicados
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

# Imprime o conjunto (os elementos duplicados são automaticamente removidos)
print(numeros)  # Output: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

# Remove o elemento 1 do conjunto (se presente)
numeros.discard(1)

# Tenta remover o elemento 45 do conjunto (que não está presente)
numeros.discard(45)

# Imprime o conjunto após as remoções
print(numeros)  # Output: {0, 2, 3, 4, 5, 6, 7, 8, 9}

# O método discard() é usado para remover um elemento específico de um conjunto, 
# se ele estiver presente. Se o elemento não estiver presente, nenhuma ação é realizada (não ocorre erro). 
# Portanto, após chamar numeros.discard(1), o elemento 1 é removido do conjunto numeros, 
# e após chamar numeros.discard(45), como o elemento 45 não está presente, nenhuma mudança ocorre no conjunto.