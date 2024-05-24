# Define variáveis para armazenar informações sobre uma pessoa
nome = "Adrielle"
idade = 20
profissao = "programadora"
linguagem = "Python"
saldo = 1.500

# Define um dicionário 'dados' com o nome e idade da pessoa
dados = {"nome": "Adrielle", "idade": 20}

# Imprime o nome e idade usando formatação de string com o operador % (antiga)
print("Nome: %s Idade: %d" % (nome, idade))

# Imprime o nome e idade usando formatação de string com o método format()
print("Nome: {} Idade: {}".format(nome, idade))

# Imprime o nome e idade usando formatação de string com índices
print("Nome: {1} Idade: {0}".format(idade, nome))
print("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome))

# Imprime o nome e idade usando formatação de string com nomes de argumentos
print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
print("Nome: {name} Idade: {age} {name} {name} {age}".format(age=idade, name=nome))

# Imprime o nome e idade usando formatação de string com unpacking de dicionário
print("Nome: {nome} Idade: {idade}".format(**dados))

# Imprime o nome e idade usando f-strings (Python 3.6+)
print(f"Nome: {nome} Idade: {idade}")

# Imprime o nome, idade e saldo com f-strings, com formatação de ponto flutuante
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")

# Imprime o nome, idade e saldo com f-strings, com formatação de ponto flutuante e largura especificada
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.1f}")
