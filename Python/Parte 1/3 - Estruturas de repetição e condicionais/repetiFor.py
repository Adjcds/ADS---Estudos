# Solicita ao usuário que informe um texto
texto = input("Informe um texto: ")

# Define as vogais em maiúsculas
VOGAIS = "AEIOU"

# Itera sobre cada caractere do texto
for letra in texto:
    # Verifica se a letra (convertida para maiúscula) está entre as vogais definidas
    if letra.upper() in VOGAIS:
        # Se a letra for uma vogal, imprime-a
        print(letra, end="")
else:
    # Quando o loop terminar, adiciona uma quebra de linha para separar da próxima saída
    print()

# Adiciona um commit explicando o exemplo com iterável
"""
Adiciona exemplo de iteração sobre um texto para imprimir apenas as vogais. 
Utiliza um iterável para percorrer cada letra do texto, verificando se é uma vogal.
"""

# Itera sobre os números de 0 a 50, (51 pq é o final é -1) pulando de 5 em 5
for numero in range(0, 51, 5):
    # Imprime cada número seguido de um espaço
    print(numero, end=" ")


