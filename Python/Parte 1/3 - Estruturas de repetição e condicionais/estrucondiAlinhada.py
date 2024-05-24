# Estruturas alinhadas referem-se a múltiplos blocos de código aninhados dentro de outros blocos,
# geralmente dentro de estruturas condicionais ou de repetição. Esses blocos estão visualmente
# alinhados na indentação do código para indicar a sua relação hierárquica.

# Definindo o tipo de conta do cliente
conta_normal = False
conta_universitaria = False
conta_especial = True

# Definindo o saldo, valor do saque e limite do cheque especial
saldo = 2000
saque = 1500
cheque_especial = 450

# Verificando o tipo de conta e executando a lógica correspondente
if conta_normal:  # Se for uma conta normal

    if saldo >= saque:  # Verificando se o saldo é suficiente para o saque
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):  # Verificando se o saque pode ser realizado com o cheque especial
        print("Saque realizado com uso do cheque especial!")

# 'elif' é uma abreviação de 'else if' e é usado em Python para adicionar outra condição à estrutura condicional.
# Ele permite verificar múltiplas condições em uma estrutura condicional sem precisar aninhar mais 'if' dentro de 'else'.

    else:
        print("Não foi possível realizar o saque, saldo insuficiente!")

elif conta_universitaria:  # Se for uma conta universitária

    if saldo >= saque:  # Verificando se o saldo é suficiente para o saque
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")

elif conta_especial:  # Se for uma conta especial
    print("Conta especial selecionada!")

else:  # Se não for reconhecido nenhum tipo de conta
    print("Sistema não reconheceu seu tipo de conta, entre em contato com o seu gerente.")



