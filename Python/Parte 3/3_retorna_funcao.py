# Define a função 'calculadora' que recebe um parâmetro 'operacao'
def calculadora(operacao):
    # Define a função 'soma' que recebe dois parâmetros 'a' e 'b' e retorna a soma deles
    def soma(a, b):
        return a + b

    # Define a função 'sub' que recebe dois parâmetros 'a' e 'b' e retorna a subtração de 'a' por 'b'
    def sub(a, b):
        return a - b

    # Define a função 'mul' que recebe dois parâmetros 'a' e 'b' e retorna a multiplicação deles
    def mul(a, b):
        return a * b

    # Define a função 'div' que recebe dois parâmetros 'a' e 'b' e retorna a divisão de 'a' por 'b'
    def div(a, b):
        return a / b

    # Usa a estrutura 'match' para selecionar a operação com base no valor do parâmetro 'operacao'
    match operacao:
        case "+":  # Se a operação for '+', retorna a função 'soma'
            return soma
        case "-":  # Se a operação for '-', retorna a função 'sub'
            return sub
        case "*":  # Se a operação for '*', retorna a função 'mul'
            return mul
        case "/":  # Se a operação for '/', retorna a função 'div'
            return div

# Obtém a função correspondente à operação '+' e a atribui à variável 'op'
op = calculadora("+")
# Chama a função 'op' com os argumentos 2 e 2, e imprime o resultado
print(op(2, 2))

# Obtém a função correspondente à operação '-' e a atribui à variável 'op'
op = calculadora("-")
# Chama a função 'op' com os argumentos 2 e 2, e imprime o resultado
print(op(2, 2))

# Obtém a função correspondente à operação '*' e a atribui à variável 'op'
op = calculadora("*")
# Chama a função 'op' com os argumentos 2 e 2, e imprime o resultado
print(op(2, 2))

# Obtém a função correspondente à operação '/' e a atribui à variável 'op'
op = calculadora("/")
# Chama a função 'op' com os argumentos 2 e 2, e imprime o resultado
print(op(2, 2))
