# Dicionário de contatos
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

# Verificando se uma chave específica está presente no dicionário
resultado = "guilherme@gmail.com" in contatos  # True
print(resultado)

# Verificando se uma chave inexistente está presente no dicionário
resultado = "megui@gmail.com" in contatos  # False
print(resultado)

# Verificando se uma chave específica está presente no dicionário interno a outro dicionário
resultado = "idade" in contatos["guilherme@gmail.com"]  # False
print(resultado)

# Verificando se uma chave específica está presente no dicionário interno a outro dicionário
resultado = "telefone" in contatos["giovanna@gmail.com"]  # True
print(resultado)

# Este código demonstra como verificar a presença de chaves em dicionários Python, 
# tanto no nível mais externo quanto nos níveis internos de dicionários aninhados. 
# Isso é útil para determinar se determinadas chaves estão presentes antes de acessar seus valores.