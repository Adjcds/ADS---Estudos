# Define uma função geradora chamada 'meu_gerador' que aceita uma lista de inteiros como argumento
def meu_gerador(numeros: list[int]):
    # Itera sobre cada número na lista fornecida
    for numero in numeros:
        # Usa 'yield' para retornar o número multiplicado por 2
        yield numero * 2

# Usa um loop 'for' para iterar através dos valores gerados pela função 'meu_gerador'
for i in meu_gerador(numeros=[1, 2, 3]):
    # Imprime cada valor gerado
    print(i)
