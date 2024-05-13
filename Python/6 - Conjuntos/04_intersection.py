# Define dois conjuntos
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

# Realiza a interseção dos conjuntos e armazena o resultado em 'resultado'
resultado = conjunto_a.intersection(conjunto_b)

# Imprime o resultado da interseção
print(resultado)  # Output: {2, 3}

# O método intersection() retorna um novo conjunto que contém apenas os elementos que estão presentes em ambos os conjuntos originais. Neste caso, o conjunto resultante resultado conterá os elementos {2, 3}, que são os elementos comuns a ambos os conjuntos conjunto_a e conjunto_b.