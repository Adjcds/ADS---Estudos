# Define um conjunto de números sorteados inicialmente contendo os números 1 e 23
sorteio = {1, 23}

# Adiciona o número 25 ao conjunto
sorteio.add(25)  # Resultado: {1, 23, 25}
print(sorteio)

# Adiciona o número 42 ao conjunto
sorteio.add(42)  # Resultado: {1, 23, 25, 42}
print(sorteio)

# Tenta adicionar o número 25 novamente ao conjunto (que já está presente)
sorteio.add(25)  # Resultado: {1, 23, 25, 42} - não ocorre mudança, pois 25 já está presente
print(sorteio)

# O método add() é usado para adicionar um único elemento a um conjunto. 
# Se o elemento já estiver presente no conjunto, a operação não terá efeito, pois os conjuntos em Python 
# são estruturas de dados que não permitem duplicatas. Portanto, no último caso, onde tentamos adicionar o 
# número 25 novamente ao conjunto sorteio, como ele já está presente, não há mudança no conjunto.