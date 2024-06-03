# Define a função 'mensagem' que recebe um parâmetro 'nome'
def mensagem(nome):
    # Imprime uma mensagem indicando que a função 'mensagem' está sendo executada
    print("executando mensagem")
    # Retorna uma string formatada com o nome recebido
    return f"Oi {nome}"

# Define a função 'mensagem_longa' que também recebe um parâmetro 'nome'
def mensagem_longa(nome):
    # Imprime uma mensagem indicando que a função 'mensagem longa' está sendo executada
    print("executando mensagem longa")
    # Retorna uma string formatada mais longa com o nome recebido
    return f"Olá tudo bem com você {nome}?"

# Define a função 'executar' que recebe dois parâmetros: uma função 'funcao' e um 'nome'
def executar(funcao, nome):
    # Imprime uma mensagem indicando que a função 'executar' está sendo executada
    print("executando executar")
    # Chama a função passada como parâmetro com o nome fornecido e retorna o resultado
    return funcao(nome)

# Chama a função 'executar' passando a função 'mensagem' e o nome 'Joao'
# Imprime o resultado da chamada da função 'executar'
print(executar(mensagem, "Joao"))

# Chama a função 'executar' passando a função 'mensagem_longa' e o nome 'Joao'
# Imprime o resultado da chamada da função 'executar'
print(executar(mensagem_longa, "Joao"))
