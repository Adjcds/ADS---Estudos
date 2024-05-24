# Cria um conjunto a partir de uma lista de números
numeros = set([1, 2, 3, 1, 3, 4])
print(numeros)  # {1, 2, 3, 4}

# Cria um conjunto a partir de uma string
letras = set("abacaxi")
print(letras)  # {"b", "a", "c", "x", "i"}

# Cria um conjunto a partir de uma tupla
carros = set(("palio", "gol", "celta", "palio"))
print(carros)  # {"gol", "celta", "palio"}

# Um conjunto em Python é uma coleção não ordenada de elementos únicos. 
# Quando criamos um conjunto a partir de uma lista, ele remove automaticamente quaisquer elementos duplicados.
# Quando criamos um conjunto a partir de uma string, ele considera cada caractere único. 
# O mesmo acontece quando criamos um conjunto a partir de uma tupla.