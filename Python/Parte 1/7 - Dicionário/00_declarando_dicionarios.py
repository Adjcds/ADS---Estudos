# Criação de um dicionário usando a sintaxe de chave-valor
pessoa = {"nome": "Guilherme", "idade": 28}

# Impressão do dicionário
print(pessoa)  # Saída: {'nome': 'Guilherme', 'idade': 28}

# Criação de um dicionário usando a função dict()
pessoa = dict(nome="Guilherme", idade=28)

# Impressão do dicionário
print(pessoa)  # Saída: {'nome': 'Guilherme', 'idade': 28}

# Adição de uma nova chave-valor ao dicionário existente
pessoa["telefone"] = "3333-1234"

# Impressão do dicionário atualizado
print(pessoa)  # Saída: {'nome': 'Guilherme', 'idade': 28, 'telefone': '3333-1234'}

# Resumo:
# Este código demonstra como criar e manipular um dicionário em Python.
# Primeiro, um dicionário é criado usando a sintaxe de chave-valor.
# Em seguida, o mesmo dicionário é recriado usando a função `dict()`.
# Após isso, uma nova chave-valor é adicionada ao dicionário.
# Finalmente, o conteúdo atualizado do dicionário é impresso,
# mostrando que a nova entrada foi adicionada com sucesso.