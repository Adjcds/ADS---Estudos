# Define uma lista de caracteres "p", "y", "t", "h", "o" e "n"
lista = ["p", "y", "t", "h", "o", "n"]

# Imprime todos os elementos da lista a partir do terceiro elemento até o final
print(lista[2:])  # ["t", "h", "o", "n"]

# Imprime todos os elementos da lista até o segundo elemento (exclusivo)
print(lista[:2])  # ["p", "y"]

# Imprime os elementos da lista a partir do segundo elemento até o terceiro elemento (exclusivo)
print(lista[1:3])  # ["y", "t"]

# Imprime os elementos da lista do primeiro ao terceiro elemento (exclusivo), pulando de dois em dois
print(lista[0:3:2])  # ["p", "t"]

# Imprime todos os elementos da lista
print(lista[::])  # ["p", "y", "t", "h", "o", "n"]

# Imprime todos os elementos da lista em ordem reversa
print(lista[::-1])  # ["n", "o", "h", "t", "y", "p"]

# lista[2:]: Retorna todos os elementos da lista a partir do terceiro elemento até o final.
# lista[:2]: Retorna todos os elementos da lista até o segundo elemento (exclusivo).
# lista[1:3]: Retorna os elementos da lista do segundo ao terceiro elemento (exclusivo).
# lista[0:3:2]: Retorna os elementos da lista do primeiro ao terceiro elemento (exclusivo), pulando de dois em dois.
# lista[::]: Retorna todos os elementos da lista.
# lista[::-1]: Retorna todos os elementos da lista em ordem reversa.