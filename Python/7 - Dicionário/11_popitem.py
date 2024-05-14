# Dicionário de contatos com um único contato
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# Removendo e retornando um par chave-valor arbitrário usando .popitem()
resultado = contatos.popitem()  # ('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})
print(resultado)  # Saída: ('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})

# Tentativa de remover um par chave-valor quando o dicionário está vazio, resultando em KeyError
# contatos.popitem()  # KeyError

# Este código demonstra como usar o método .popitem() para remover e retornar um par chave-valor arbitrário
#  de um dicionário Python. No entanto, ao tentar usar .popitem() em um dicionário vazio, isso resultará em 
# um KeyError, já que não há itens para remover. Isso ocorre porque os dicionários em Python não mantêm uma ordem
# específica para os itens.