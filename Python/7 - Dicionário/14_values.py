# Dicionário de contatos com várias entradas
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

# Obtendo uma view dos valores do dicionário usando .values()
resultado = contatos.values()
print(resultado)  # Saída: dict_values([{'nome': 'Guilherme', 'telefone': '3333-2221'}, {'nome': 'Giovanna', 'telefone': '3443-2121'}, {'nome': 'Chappie', 'telefone': '3344-9871'}, {'nome': 'Melaine', 'telefone': '3333-7766'}])

# Este código demonstra como usar o método .values() para obter uma view dos valores de um dicionário Python. 
# A view resultante contém uma lista de todos os valores no dicionário, que podem ser iterados ou acessados 
# conforme necessário. Isso pode ser útil quando você precisa trabalhar apenas com os valores de um dicionário,
# sem se preocupar com as chaves associadas.