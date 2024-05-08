# Adiciona exemplo de utilização da instrução 'break' em um loop 'while' em Python.
# Explica que o 'break' é usado para interromper prematuramente a execução do loop,
# No exemplo a seguir, o código solicita repetidamente ao usuário que informe um número
# neste caso, quando o usuário informa o número 10.
# Se o número fornecido for igual a 10, o loop é interrompido com a instrução 'break'.
# Se o número fornecido for par, o loop continua sem imprimir o número com a instrução 'continue'.
# Caso contrário, o número é impresso.

# Código utilizando a estrutura de repetição while
while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    if numero % 2 == 0:
        continue

    print(numero)

# Código utilizando a estrutura de repetição for e a função built-in range
# for numero in range(100):

#     if numero % 2 == 0:
#         continue

#     print(numero, end=" ")
