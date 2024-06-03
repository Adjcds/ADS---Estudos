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

# Aplica o decorador 'meu_decorador' à função 'ola_mundo' usando a sintaxe @decorator
@meu_decorador
def ola_mundo():
    # Imprime "Olá mundo!"
    print("Olá mundo!")

# Chama a função decorada (que agora é 'envelope')
ola_mundo()
