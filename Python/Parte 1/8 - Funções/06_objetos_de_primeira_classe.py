# Define uma função chamada somar que recebe dois parâmetros, a e b, e retorna a soma deles.
def somar(a, b):
    return a + b  # Retorna a soma de a e b.

# Define uma função chamada exibir_resultado que recebe três parâmetros: a, b e funcao.
# A função aplica funcao aos parâmetros a e b, e exibe o resultado.
def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)  # Chama a função funcao com os argumentos a e b, e armazena o resultado em resultado.
    print(f"O resultado da operação {a} + {b} = {resultado}")  # Imprime o resultado da operação formatado.

# Chama a função exibir_resultado com os argumentos 10, 10 e a função somar.
# Isso resultará na chamada somar(10, 10) e na impressão do resultado.
exibir_resultado(10, 10, somar)  # O resultado da operação 10 + 10 = 20

# Resumo:
# O código define duas funções:
# 1. somar(a, b): Recebe dois números, a e b, e retorna a soma deles.
# 2. exibir_resultado(a, b, funcao): Recebe dois números, a e b, e uma função, funcao. Aplica a função aos números e imprime o resultado formatado.
# A chamada exibir_resultado(10, 10, somar) demonstra o uso dessas funções, passando a função somar como argumento para exibir_resultado,
# resultando na impressão: "O resultado da operação 10 + 10 = 20".
