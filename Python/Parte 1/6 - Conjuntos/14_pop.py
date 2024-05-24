# Define um conjunto de números com elementos duplicados
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

# Imprime o conjunto (os elementos duplicados são automaticamente removidos)
print(numeros)  # Output: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

# Remove e retorna um elemento aleatório do conjunto
print(numeros.pop())  # Output: 0

# Remove e retorna outro elemento aleatório do conjunto
print(numeros.pop())  # Output: 1

# Imprime o conjunto após as remoções
print(numeros)  # Output: {2, 3, 4, 5, 6, 7, 8, 9}

# O método pop() remove e retorna um elemento aleatório do conjunto.
# Como os conjuntos em Python não são ordenados, não há garantia sobre qual elemento será removido.
# Portanto, ao chamar numeros.pop(), o elemento removido pode ser qualquer um dos elementos do conjunto.