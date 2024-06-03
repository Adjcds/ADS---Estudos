# Define a função 'principal'
def principal():
    # Imprime uma mensagem indicando que a função 'principal' está sendo executada
    print("executando a funcao principal")

    # Define uma função interna chamada 'funcao_interna'
    def funcao_interna():
        # Imprime uma mensagem indicando que a 'funcao_interna' está sendo executada
        print("executando a funcao interna")

    # Define uma segunda função interna chamada 'funcao_2'
    def funcao_2():
        # Imprime uma mensagem indicando que a 'funcao_2' está sendo executada
        print("executando a funcao 2")

    # Chama a função interna 'funcao_interna'
    funcao_interna()
    # Chama a função interna 'funcao_2'
    funcao_2()

# Chama a função 'principal'
principal()
