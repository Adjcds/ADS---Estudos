# Criação de um dicionário de contatos com e-mails como chaves
# e um dicionário aninhado contendo nome e telefone como valores
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

# Limpeza de todos os itens do dicionário
contatos.clear()

# Impressão do dicionário vazio
print(contatos)  # Saída: {}
