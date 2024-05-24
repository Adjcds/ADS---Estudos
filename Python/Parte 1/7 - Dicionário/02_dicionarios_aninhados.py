# Criação de um dicionário de contatos com e-mails como chaves
# e um dicionário aninhado contendo nome e telefone como valores
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

# Acessando o telefone do contato com e-mail "giovanna@gmail.com"
telefone = contatos["giovanna@gmail.com"]["telefone"]  # Saída: "3443-2121"

# Impressão do telefone
print(telefone)  # Saída: "3443-2121"

# Resumo:
# Este código demonstra como acessar valores em um dicionário aninhado em Python.
# Primeiro, cria um dicionário onde cada chave é um e-mail e cada valor é outro dicionário contendo informações de contato.
# Em seguida, acessa o número de telefone associado ao e-mail "giovanna@gmail.com".
# Finalmente, imprime o número de telefone obtido.
