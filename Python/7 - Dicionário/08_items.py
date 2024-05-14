# Dicionário de contatos com um único contato
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# Obtenção de uma view do dicionário usando o método .items()
resultado = contatos.items()  # dict_items([('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})])

# Impressão da view obtida
print(resultado)  # Saída: dict_items([('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})])

# Este código demonstra como usar o método .items() para obter uma view do dicionário contatos.
# A view retorna uma sequência de tuplas contendo pares de chave-valor do dicionário. 
# Isso pode ser útil ao iterar sobre o dicionário ou ao precisar manipular os itens do dicionário de forma mais flexível.