# Define uma lista com elementos diferentes: um inteiro, uma string e outra lista
lista = [1, "Python", [40, 30, 20]]

# Cria uma cópia superficial da lista (não afeta a lista original)
copia_lista = lista.copy()

# Imprime a lista original
print(lista)  # [1, "Python", [40, 30, 20]]

# A cópia da lista é armazenada na variável 'copia_lista'
print(copia_lista)  # [1, "Python", [40, 30, 20]]

# lista.copy(): Cria uma cópia superficial da lista original. 
# A cópia contém os mesmos elementos, mas é uma nova lista independente da original.
# Alterações na cópia não afetam a lista original, e vice-versa.