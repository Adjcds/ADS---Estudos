# Dicionário de contatos
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

# Removendo a chave "telefone" do dicionário interno associado à chave "guilherme@gmail.com"
del contatos["guilherme@gmail.com"]["telefone"]

# Removendo completamente a entrada associada à chave "chappie@gmail.com" do dicionário principal
del contatos["chappie@gmail.com"]

# Impressão do dicionário após as deleções
print(contatos)  # Saída: {'guilherme@gmail.com': {'nome': 'Guilherme'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3443-2121'}, 'melaine@gmail.com': {'nome': 'Melaine', 'telefone': '3333-7766'}}

# Este código demonstra como remover itens de um dicionário Python usando a instrução del. 
# Ele ilustra a remoção de uma chave específica de um dicionário interno e a remoção completa de 
# uma entrada de um dicionário principal. Essa técnica é útil quando você precisa limpar ou modificar
# um dicionário, removendo itens específicos.