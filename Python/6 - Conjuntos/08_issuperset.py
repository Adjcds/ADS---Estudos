# Define dois conjuntos
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

# Verifica se conjunto_a é um superconjunto de conjunto_b e armazena o resultado em 'resultado'
resultado = conjunto_a.issuperset(conjunto_b)
print(resultado)  # Output: False

# Verifica se conjunto_b é um superconjunto de conjunto_a e armazena o resultado em 'resultado'
resultado = conjunto_b.issuperset(conjunto_a)
print(resultado)  # Output: True

# O método issuperset() retorna True se todos os elementos do conjunto especificado estiverem
# presentes no conjunto original e False caso contrário. Portanto, conjunto_a.issuperset(conjunto_b) 
# retorna False porque nem todos os elementos de conjunto_b estão presentes em conjunto_a,
# enquanto conjunto_b.issuperset(conjunto_a) retorna True porque todos os elementos de conjunto_a 
# estão presentes em conjunto_b.