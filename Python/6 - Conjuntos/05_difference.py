# Define dois conjuntos
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

# Encontra a diferença entre conjunto_a e conjunto_b e armazena o resultado em 'resultado'
resultado = conjunto_a.difference(conjunto_b)
print(resultado)  # Output: {1}

# Encontra a diferença entre conjunto_b e conjunto_a e armazena o resultado em 'resultado'
resultado = conjunto_b.difference(conjunto_a)
print(resultado)  # Output: {4}

# O método difference() retorna um novo conjunto contendo os elementos que estão presentes no conjunto de origem 
# (neste caso, conjunto_a ou conjunto_b), mas não estão presentes no outro conjunto especificado 
# (neste caso, conjunto_b ou conjunto_a, respectivamente).

# Portanto, conjunto_a.difference(conjunto_b) retorna {1}, porque 1 está presente em conjunto_a mas não em conjunto_b, 
# enquanto conjunto_b.difference(conjunto_a) retorna {4}, pois 4 está presente em conjunto_b mas não em conjunto_a.

