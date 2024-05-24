# # Define um conjunto de números com elementos duplicados
# numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

# # Imprime o conjunto (os elementos duplicados são automaticamente removidos)
# print(numeros)  # Output: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

# # Remove o elemento 0 do conjunto
# print(numeros.remove(0))  # Output: None (a função remove() não retorna valor)

# # Imprime o conjunto após a remoção
# print(numeros)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9}

# O método remove() é usado para remover um elemento específico de um conjunto. 
# Se o elemento estiver presente, ele será removido; caso contrário, uma exceção KeyError será levantada.
# No entanto, o método remove() não retorna o elemento removido, ele simplesmente remove o elemento do conjunto.
# Portanto, ao chamar numeros.remove(0), o elemento 0 é removido do conjunto numeros.