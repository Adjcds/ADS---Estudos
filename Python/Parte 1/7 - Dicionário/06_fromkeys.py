# Criação de um dicionário com chaves especificadas e valores padrão None
resultado = dict.fromkeys(["nome", "telefone"])  # {"nome": None, "telefone": None}
print(resultado)  # Saída: {"nome": None, "telefone": None}

# Criação de um dicionário com chaves especificadas e valores padrão "vazio"
resultado = dict.fromkeys(["nome", "telefone"], "vazio")  # {"nome": "vazio", "telefone": "vazio"}
print(resultado)  # Saída: {"nome": "vazio", "telefone": "vazio"}

# Resumo:
# Este código demonstra o uso do método `dict.fromkeys()` para criar dicionários em Python.
# Primeiro, cria um dicionário com chaves especificadas e valores padrão `None`.
# Em seguida, cria um dicionário com as mesmas chaves, mas com valores padrão "vazio".
# Finalmente, imprime os dicionários resultantes para mostrar a estrutura criada.
