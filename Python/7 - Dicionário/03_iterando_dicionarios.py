# Criação de um dicionário de contatos com e-mails como chaves
# e um dicionário aninhado contendo nome e telefone como valores
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

# Iteração sobre o dicionário usando apenas as chaves
for chave in contatos:
    print(chave, contatos[chave])

# Impressão de uma linha de separação
print("=" * 100)

# Iteração sobre o dicionário usando items() para obter chave e valor
for chave, valor in contatos.items():
    print(chave, valor)

# Resumo:
# Este código demonstra duas formas de iterar sobre um dicionário em Python.
# Primeiro, itera usando apenas as chaves do dicionário, acessando os valores a partir das chaves.
# Em seguida, imprime uma linha de separação.
# Depois, itera usando o método items() do dicionário para obter diretamente as chaves e os valores.
# Ambas as abordagens imprimem as chaves e os valores associados do dicionário.
