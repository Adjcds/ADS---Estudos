# Define uma lista de números
numeros = [1, 30, 21, 2, 9, 65, 34]

# Filtra a lista de números, selecionando apenas os números pares
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

# Calcula o quadrado de cada número na lista
quadrado = [numero**2 for numero in numeros]
print(quadrado)

# A expressão [numero for numero in numeros if numero % 2 == 0] cria uma nova lista chamada pares,
# onde cada elemento da lista original numeros é verificado se é par (numero % 2 == 0).
# Apenas os números pares são incluídos na lista resultante.
# A expressão [numero**2 for numero in numeros] cria uma nova lista chamada quadrado, 
# onde cada elemento da lista original numeros é elevado ao quadrado (numero**2). 
# A lista resultante contém o quadrado de cada número na lista original.