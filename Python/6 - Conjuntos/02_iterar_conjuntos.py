# Define um conjunto de carros
carros = {"gol", "celta", "palio"}

# Itera sobre os elementos do conjunto e imprime cada carro
for carro in carros:
    print(carro)

# Itera sobre os elementos do conjunto junto com seus índices e imprime cada índice e carro
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

# No primeiro loop for, cada carro do conjunto é impresso em uma linha separada.
# No segundo loop for, a função enumerate() é usada para obter tanto o índice quanto o valor de cada elemento do conjunto. Então, o índice e o carro são impressos em cada iteração.