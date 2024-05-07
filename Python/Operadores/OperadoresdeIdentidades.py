# ### Operadores de Identidade

# Os operadores de identidade em Python são utilizados para verificar se dois objetos têm a mesma identidade na memória. Em Python, todos os objetos têm um identificador único, que pode ser obtido usando a função `id()`. Os operadores de identidade mais comuns são `is` e `is not`.

# - O operador `is` retorna `True` se os dois objetos compartilham o mesmo espaço de memória, ou seja, se são o mesmo objeto.
# - O operador `is not` retorna `True` se os dois objetos não compartilham o mesmo espaço de memória, ou seja, se não são o mesmo objeto.

# Exemplo:


x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x is y)   # False, x e y têm valores iguais, mas apontam para diferentes espaços de memória
print(x is z)   # True, x e z compartilham o mesmo espaço de memória
print(x is not y)   # True, x e y não compartilham o mesmo espaço de memória

## outro exemplo

saldo = 1000
limite = 1000

print(saldo is limite)       # False
print(saldo is not limite)   # True
