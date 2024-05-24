# Define uma tupla de caracteres
tupla = ("p", "y", "t", "h", "o", "n",)

# Imprime os elementos da tupla a partir do índice 2 até o final
print(tupla[2:])  # ("t", "h", "o", "n")

# Imprime os elementos da tupla do início até o índice 1 (exclusivo)
print(tupla[:2])  # ("p", "y")

# Imprime os elementos da tupla do índice 1 (inclusive) até o índice 3 (exclusivo)
print(tupla[1:3])  # ("y", "t")

# Imprime os elementos da tupla do início até o índice 2 (exclusivo) pulando de 2 em 2
print(tupla[0:3:2])  # ("p", "t")

# Imprime todos os elementos da tupla
print(tupla[::])  # ("p", "y", "t", "h", "o", "n")

# Imprime todos os elementos da tupla em ordem reversa
print(tupla[::-1])  # ("n", "o", "h", "t", "y", "p")

# tupla[2:]: Retorna todos os elementos da tupla a partir do índice 2 até o final.
# tupla[:2]: Retorna todos os elementos da tupla do início até o índice 1 (exclusivo).
# tupla[1:3]: Retorna todos os elementos da tupla do índice 1 (inclusive) até o índice 3 (exclusivo).
# tupla[0:3:2]: Retorna todos os elementos da tupla do início até o índice 2 (exclusivo) pulando de 2 em 2.
# tupla[::]: Retorna todos os elementos da tupla.
# tupla[::-1]: Retorna todos os elementos da tupla em ordem reversa.