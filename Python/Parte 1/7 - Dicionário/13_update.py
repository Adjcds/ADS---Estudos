# Dicionário de contatos inicial
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# Atualizando o dicionário com novos valores para a chave existente "guilherme@gmail.com"
contatos.update({"guilherme@gmail.com": {"nome": "Gui"}})
print(contatos)  # Saída: {'guilherme@gmail.com': {'nome': 'Gui'}}

# Adicionando uma nova entrada ao dicionário para a chave "giovanna@gmail.com"
contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}})
print(contatos)  # Saída: {'guilherme@gmail.com': {'nome': 'Gui'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3322-8181'}}

# Este código demonstra como usar o método .update() para atualizar um dicionário Python com novos valores 
# ou adicionar novas entradas a ele. Quando uma chave existente é especificada, os valores correspondentes
# são substituídos. Se uma chave não existir, uma nova entrada é adicionada ao dicionário. 
# Isso é útil para modificar ou expandir dicionários existentes com novos dados.