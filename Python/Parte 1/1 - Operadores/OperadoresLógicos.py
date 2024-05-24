# ### Operadores Lógicos

# Os operadores lógicos são usados para combinar expressões condicionais.

# | Operador | Significado |
# |----------|-------------|
# | and      | Retorna True se ambas as expressões forem verdadeiras |
# | or       | Retorna True se pelo menos uma das expressões for verdadeira |
# | not      | Inverte o valor da expressão lógica |

# Exemplo:

# ```python
# a = 5
# b = 3

# # Verifica se a é maior que b e se a é menor que 10
# if a > b and a < 10:
#     print("a é maior que b e menor que 10")

# # AND = para ser True tudo tem que ser True
# # OR = para ser True apenas um tem que ser True

print(True and True and True)  # True
print(True and False and True) # False
print(False and False and False) # False
print(True or True or True) # True
print(True or False or False) # True
print(False or False or False) # False

saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp) # True

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp_2) # True

conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp_3) # Truef


## Operador not

# O operador lógico not é utilizado para inverter o valor de uma expressão booleana. Se a expressão for verdadeira, not a torna falsa, e se a expressão for falsa, not a torna verdadeira.

# Exemplo:

x = True
y = False

print(not x)  # False
print(not y)  # True

# Neste exemplo, not x resulta em False porque x é originalmente True, então not inverte o valor para False. Similarmente, not y resulta em True porque y é originalmente False, então not inverte o valor para True