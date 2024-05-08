# Neste exemplo, utilizamos a estrutura condicional ternária para verificar se o saldo é
# suficiente para realizar um saque. A expressão "status = "Sucesso" if saldo >= saque else "Falha""
# avalia se o saldo é maior ou igual ao valor do saque. Se for verdadeiro, atribui "Sucesso" à variável
# status, caso contrário, atribui "Falha". Em seguida, usamos uma f-string para imprimir o resultado
# da transação, indicando se foi um sucesso ou uma falha.

# Define o saldo e o valor do saque
saldo = 2000
saque = 2500

# Verifica se o saldo é suficiente para o saque e atribui "Sucesso" se for, senão "Falha"
status = "Sucesso" if saldo >= saque else "Falha"

# Imprime o status da transação de saque
print(f"{status} ao realizar o saque!")

