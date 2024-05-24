# Define uma lista de carros
carros = ["gol", "celta", "palio"]

# Itera sobre cada elemento na lista carros e imprime cada carro
for carro in carros:
    print(carro)

# Itera sobre cada elemento na lista carros junto com seu índice e imprime o índice seguido pelo carro
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

# O primeiro loop for itera sobre cada elemento na lista carros e imprime cada carro.
# O segundo loop for utiliza a função enumerate() para iterar sobre cada elemento na lista
# carros juntamente com seu índice, e imprime o índice seguido pelo carro.