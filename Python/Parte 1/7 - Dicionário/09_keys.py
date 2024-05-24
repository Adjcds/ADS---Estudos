# Dicionário de contatos com um único contato
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# Obtendo uma view das chaves do dicionário usando o método .keys()
resultado = contatos.keys()  # dict_keys(['guilherme@gmail.com'])

# Impressão da view obtida
print(resultado)  # Saída: dict_keys(['guilherme@gmail.com'])

# Este código demonstra como usar o método .keys() para obter uma view das chaves do dicionário contatos. 
# A view retorna uma estrutura de dados dinâmica que reflete as chaves atuais do dicionário. 
# Isso pode ser útil ao iterar sobre as chaves do dicionário ou ao verificar a presença de uma chave específica.