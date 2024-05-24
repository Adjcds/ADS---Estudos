# Define uma função chamada calcular_total que recebe uma lista de números e retorna a soma desses números.
def calcular_total(numeros):
    return sum(numeros)  # Retorna a soma de todos os números na lista.

# Define uma função chamada retorna_antecessor_e_sucessor que recebe um número e retorna uma tupla com o antecessor e o sucessor desse número.
def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1  # Calcula o antecessor subtraindo 1 do número.
    sucessor = numero + 1    # Calcula o sucessor adicionando 1 ao número.

    return antecessor, sucessor  # Retorna uma tupla contendo o antecessor e o sucessor.

# Chama a função calcular_total com a lista [10, 20, 34] e imprime o resultado, que é 64.
print(calcular_total([10, 20, 34]))  # 64

# Chama a função retorna_antecessor_e_sucessor com o número 10 e imprime o resultado, que é a tupla (9, 11).
print(retorna_antecessor_e_sucessor(10))  # (9, 11)

# Resumo:
# O código define duas funções:
# 1. calcular_total(numeros): Recebe uma lista de números e retorna a soma desses números usando a função sum().
#    Exemplo de uso: calcular_total([10, 20, 34]) retorna 64.
# 2. retorna_antecessor_e_sucessor(numero): Recebe um número e retorna uma tupla com o antecessor (número - 1) e o sucessor (número + 1).
#    Exemplo de uso: retorna_antecessor_e_sucessor(10) retorna (9, 11).
# O código demonstra o uso dessas funções com exemplos específicos:
# - calcular_total([10, 20, 34]) retorna 64 e imprime 64.
# - retorna_antecessor_e_sucessor(10) retorna (9, 11) e imprime (9, 11).
