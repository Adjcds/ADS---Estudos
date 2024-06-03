# Define um decorador chamado 'meu_decorador' que recebe uma função como argumento
def meu_decorador(funcao):
    # Define uma função interna chamada 'envelope'
    def envelope():
        # Imprime uma mensagem antes de executar a função decorada
        print("faz algo antes de executar")
        # Chama a função passada como argumento (a função que está sendo decorada)
        funcao()
        # Imprime uma mensagem depois de executar a função decorada
        print("faz algo depois de executar")

    # Retorna a função 'envelope'
    return envelope

# Define uma função simples chamada 'ola_mundo'
def ola_mundo():
    # Imprime "Olá mundo!"
    print("Olá mundo!")

# Aplica o decorador 'meu_decorador' à função 'ola_mundo'
# Isso substitui 'ola_mundo' pela função 'envelope' retornada pelo decorador
ola_mundo = meu_decorador(ola_mundo)

# Chama a função decorada (que agora é 'envelope')
ola_mundo()
