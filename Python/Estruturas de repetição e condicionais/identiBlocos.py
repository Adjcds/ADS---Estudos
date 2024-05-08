#exemplo da aula:
def sacar(valor):
    saldo = 500
    
    if saldo >= valor:
        print("Valor sacado!")
        print("Retire o seu dinheiro na boca do caixa.")
    
    print("Obrigado por ser nosso cliente, tenha um bom dia!")

def depositar(valor):
    saldo = 500
    saldo += valor

sacar(1000)

#como seria o codigo com a logica feito por mim:

def sacar(saldo, valor):
    """
    Função para sacar dinheiro de uma conta.

    Parâmetros:
    - saldo: O saldo atual da conta.
    - valor: A quantia que o usuário deseja sacar.

    Retorna:
    - Nenhuma.
    """
    if saldo >= valor:
        print("Valor sacado!")
        print("Retire o seu dinheiro na boca do caixa.")
    else:
        print("Saldo insuficiente para sacar esse valor!")

    print("Obrigado por ser nosso cliente, tenha um bom dia!")


def depositar(saldo, valor):
    """
    Função para depositar dinheiro em uma conta.

    Parâmetros:
    - saldo: O saldo atual da conta.
    - valor: A quantia que o usuário deseja depositar.

    Retorna:
    - O novo saldo após o depósito.
    """
    saldo += valor
    return saldo


# Definindo o saldo inicial da conta como 500 unidades monetárias
saldo_inicial = 500

# Exibindo o saldo inicial para o usuário
print("Seu saldo atual é:", saldo_inicial)

# Solicitando ao usuário que digite a quantia que deseja sacar e convertendo-a para um número real
quantia = float(input("Digite a quantia que deseja sacar: "))

# Calculando o novo saldo após o saque, subtraindo a quantia sacada do saldo inicial
novo_saldo = saldo_inicial - quantia

# Chamando a função 'sacar' para processar o saque com o novo saldo e a quantia solicitada
sacar(novo_saldo, quantia)

