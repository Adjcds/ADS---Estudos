# Define uma variável 'nome' com o valor "AdRieLlE"
nome = "AdRieLlE"

# Imprime o valor da variável 'nome' em letras maiúsculas
print(nome.upper())

# Imprime o valor da variável 'nome' em letras minúsculas
print(nome.lower())

# Imprime o valor da variável 'nome' com a primeira letra de cada palavra em maiúscula
print(nome.title())

# Define uma variável 'texto' com o valor "  Olá mundo!    "
texto = "  Olá mundo!    "

# Imprime o valor da variável 'texto' seguido por um ponto
print(texto + ".")

# Imprime o valor da variável 'texto' com os espaços removidos do início e do fim, seguido por um ponto
print(texto.strip() + ".")

# Imprime o valor da variável 'texto' com os espaços removidos do fim, seguido por um ponto
print(texto.rstrip() + ".")

# Imprime o valor da variável 'texto' com os espaços removidos do início, seguido por um ponto
print(texto.lstrip() + ".")

# Define uma variável 'menu' com o valor "Python"
menu = "Python"

# Imprime o valor da variável 'menu' cercado por cerquilhas (#)
print("####" + menu + "####")

# Imprime o valor da variável 'menu' centralizado em uma largura de 14 caracteres
print(menu.center(14))

# Imprime o valor da variável 'menu' centralizado em uma largura de 14 caracteres, com cerquilhas (#) preenchendo os espaços vazios
print(menu.center(14, "#"))

# Imprime o valor da variável 'menu' com "-" entre cada caractere
print("-".join(menu))
