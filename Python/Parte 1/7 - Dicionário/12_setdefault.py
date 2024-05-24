# Dicionário de contato inicial
contato = {"nome": "Guilherme", "telefone": "3333-2221"}

# Definindo o valor padrão para a chave "nome" usando .setdefault()
# Como a chave já existe, o valor associado à chave "nome" não é modificado, apenas retornado
resultado_nome = contato.setdefault("nome", "Giovanna")  # "Guilherme"
print(contato)  # Saída: {'nome': 'Guilherme', 'telefone': '3333-2221'}

# Definindo o valor padrão para a chave "idade" usando .setdefault()
# Como a chave não existe, ela é adicionada com o valor padrão fornecido e retorna o valor padrão
resultado_idade = contato.setdefault("idade", 28)  # 28
print(contato)  # Saída: {'nome': 'Guilherme', 'telefone': '3333-2221', 'idade': 28}

# Este código demonstra como usar o método .setdefault() para definir valores padrão para chaves em um 
# dicionário Python. Se a chave especificada já existir no dicionário, o método retorna o valor associado a ela. 
# Se a chave não existir, ela é adicionada ao dicionário com o valor padrão fornecido, e esse valor é retornado. 
# Isso é útil para definir valores padrão para chaves que podem não estar presentes no dicionário.