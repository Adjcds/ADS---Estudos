# Define três conjuntos
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

# Verifica se conjunto_a e conjunto_b são disjuntos e armazena o resultado em 'resultado'
resultado = conjunto_a.isdisjoint(conjunto_b)
print(resultado)  # Output: True

# Verifica se conjunto_a e conjunto_c são disjuntos e armazena o resultado em 'resultado'
resultado = conjunto_a.isdisjoint(conjunto_c)
print(resultado)  # Output: False

# O método isdisjoint() retorna True se não houver elementos em comum entre os dois conjuntos e False caso contrário. 
# Portanto, conjunto_a.isdisjoint(conjunto_b) retorna True porque não há elementos em comum 
# entre conjunto_a e conjunto_b, enquanto conjunto_a.isdisjoint(conjunto_c) retorna False 
# porque há elementos em comum entre conjunto_a e conjunto_c (o elemento 1).