# Dicionário de contatos com um único contato
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# Removendo e retornando o valor associado à chave "guilherme@gmail.com" usando .pop()
resultado = contatos.pop("guilherme@gmail.com")  # {'nome': 'Guilherme', 'telefone': '3333-2221'}
print(resultado)  # Saída: {'nome': 'Guilherme', 'telefone': '3333-2221'}

# Tentando remover uma chave que não existe, fornecendo um valor padrão {}
resultado = contatos.pop("guilherme@gmail.com", {})  # {}
print(resultado)  # Saída: {}

# Este código demonstra como usar o método .pop() para remover e retornar valores associados a chaves em 
# um dicionário Python. Ele remove a chave especificada e retorna seu valor associado. 
# Se a chave não existir, o valor padrão fornecido (se especificado) será retornado, sem modificar o dicionário original.
# Isso é útil quando você precisa remover itens de um dicionário e lidar com casos em que a chave pode não existir.