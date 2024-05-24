# Define dois conjuntos
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

# Verifica se conjunto_a é um subconjunto de conjunto_b e armazena o resultado em 'resultado'
resultado = conjunto_a.issubset(conjunto_b)
print(resultado)  # Output: True

# Verifica se conjunto_b é um subconjunto de conjunto_a e armazena o resultado em 'resultado'
resultado = conjunto_b.issubset(conjunto_a)
print(resultado)  # Output: False

# O método issubset() retorna True se todos os elementos do
# conjunto original estiverem presentes no conjunto especificado e False caso contrário. 
# Portanto, conjunto_a.issubset(conjunto_b) dretorna True porque todos os elementos de conjunto_a 
# estão presentes em conjunto_b, enquanto conjunto_b.issubset(conjunto_a) 
# retorna False porque nem todos os elementos de conjunto_b estão presentes em conjunto_a.