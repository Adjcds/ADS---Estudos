# Criação de um dicionário de contatos com um e-mail como chave
# e um dicionário aninhado contendo nome e telefone como valor
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# Criação de uma cópia superficial do dicionário contatos
copia = contatos.copy()

# Modificação do valor associado à chave "guilherme@gmail.com" na cópia do dicionário
copia["guilherme@gmail.com"] = {"nome": "Gui"}

# Impressão do valor associado à chave "guilherme@gmail.com" no dicionário original
print(contatos["guilherme@gmail.com"])  # Saída: {"nome": "Guilherme", "telefone": "3333-2221"}

# Impressão do valor associado à chave "guilherme@gmail.com" na cópia do dicionário
print(copia["guilherme@gmail.com"])  # Saída: {"nome": "Gui"}

# Resumo:
# Este código demonstra a criação de uma cópia superficial de um dicionário em Python e como a modificação
# na cópia não afeta o dicionário original. Primeiro, cria um dicionário de contatos. Em seguida, faz uma
# cópia superficial do dicionário e modifica o valor associado a uma chave na cópia. Finalmente, mostra
# que o dicionário original permanece inalterado.
