# Define um decorador chamado 'meu_decorador' que recebe uma função como argumento
def meu_decorador(funcao):
    # Define uma função interna chamada 'envelope' que aceita argumentos variáveis
    def envelope(*args, **kwargs):
        # Imprime uma mensagem antes de executar a função decorada
        print("faz algo antes de executar")
        # Chama a função passada como argumento com os argumentos fornecidos
        funcao(*args, **kwargs)
        # Imprime uma mensagem depois de executar a função decorada
        print("faz algo depois de executar")

    # Retorna a função 'envelope'
    return envelope

# Aplica o decorador 'meu_decorador' à função 'ola_mundo' usando a sintaxe @decorator
@meu_decorador
def ola_mundo(nome, outro_argumento):
    # Imprime uma mensagem personalizada com o argumento 'nome'
    print(f"Olá mundo {nome}!")

# Chama a função decorada 'ola_mundo' com os argumentos "João" e 1000
ola_mundo("João", 1000)
