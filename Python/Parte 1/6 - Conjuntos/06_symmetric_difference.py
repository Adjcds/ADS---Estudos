# Define dois conjuntos
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

# Encontra a diferença simétrica entre conjunto_a e conjunto_b e armazena o resultado em 'resultado'
resultado = conjunto_a.symmetric_difference(conjunto_b)
print(resultado)  # Output: {1, 4}

# O método symmetric_difference() retorna um novo conjunto contendo os elementos que estão presentes em apenas 
# um dos conjuntos originais, mas não em ambos.

# Portanto, neste exemplo, o conjunto resultante resultado conterá {1, 4}, pois 1 está presente apenas em conjunto_a 
# e 4 está presente apenas em conjunto_b.

