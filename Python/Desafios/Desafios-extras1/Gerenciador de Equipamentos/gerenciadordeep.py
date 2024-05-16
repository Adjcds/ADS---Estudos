itens = []

for _ in range(3):  # Loop para solicitar três itens
    item = input("")
    itens.append(item)

# Exibe a lista de itens
print("Lista de Equipamentos:")  
for item in itens:
    # Loop que percorre cada item na lista "itens"
    print(f"- {item}")