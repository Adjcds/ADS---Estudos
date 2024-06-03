import functools  # Importa o módulo functools para usar o decorator wraps

# Define um decorador chamado 'meu_decorador' que recebe uma função como argumento
def meu_decorador(funcao):
    # Usa functools.wraps para garantir que o metadata da função original seja preservado
    @functools.wraps(funcao)
    def envelope(*args, **kwargs):
        # Chama a função passada como argumento com os argumentos fornecidos
        funcao(*args, **kwargs)

    # Retorna a função 'envelope'
    return envelope

# Aplica o decorador 'meu_decorador' à função 'ola_mundo' usando a sintaxe @decorator
@meu_decorador
def ola_mundo(nome, outro_argumento):
    # Imprime uma mensagem personalizada com o argumento 'nome'
    print(f"Olá mundo {nome}!")

# Imprime o nome da função 'ola_mundo'
print(ola_mundo.__name__)
