# Define uma tupla de frutas
frutas = (
    "maçã",
    "laranja",
    "uva",
    "pera",
)

# Acessa o último elemento da tupla usando indexação negativa e imprime
print(frutas[-1])  # pera

# Acessa o terceiro elemento a partir do final da tupla usando indexação negativa e imprime
print(frutas[-3])  # laranja

# Em Python, a indexação negativa permite acessar elementos da tupla a partir do final,
# onde -1 refere-se ao último elemento, -2 ao penúltimo e assim por diante. Portanto, frutas[-1] 
# retorna o último elemento da tupla frutas (que é "pera"), e frutas[-3] retorna o 
# terceiro elemento a partir do final (que é "laranja").