# Dicionário de contatos com um único contato
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# Tentativa de acesso a uma chave inexistente, resultando em KeyError
# contatos["chave"]  # KeyError

# Usando o método .get() para acessar o valor associado à chave "chave"
# Se a chave não existir, retorna None
resultado = contatos.get("chave")  # None
print(resultado)  # Saída: None

# Usando .get() com um valor padrão vazio ({}) para caso a chave não exista
# Retorna um dicionário vazio quando a chave não existe
resultado = contatos.get("chave", {})  # {}
print(resultado)  # Saída: {}

# Usando .get() com uma chave existente e um valor padrão vazio ({})
# Retorna o valor associado à chave existente
resultado = contatos.get("guilherme@gmail.com", {})  # {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
print(resultado)  # Saída: {"guilherme@gmail.com": {"nome": 
