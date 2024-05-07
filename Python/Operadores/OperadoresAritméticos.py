#  ## Tipos de Operadores em Python

# Este projeto inclui exemplos dos diferentes tipos de operadores disponíveis em Python, incluindo operadores aritméticos, de comparação, lógicos e de atribuição.

# ### Operadores Aritméticos

# Os operadores aritméticos são usados para realizar operações matemáticas entre dois valores.

# | Símbolo | Operação      | Exemplo     | Resultado   |
# |---------|---------------|-------------|-------------|
# | +       | Adição        | 5 + 3       | 8           |
# | -       | Subtração     | 7 - 2       | 5           |
# | *       | Multiplicação | 4 * 6       | 24          |
# | /       | Divisão       | 10 / 3      | 3.333...    |
# | %       | Módulo        | 10 % 3      | 1           |
# | **      | Potenciação   | 2 ** 3      | 8           | 

produto_1 = 20
produto_2 = 10

print(produto_1 + produto_2)  # Soma: 30
print(produto_1 - produto_2)  # Subtração: 10
print(produto_1 / produto_2)  # Divisão: 2.0
print(produto_1 // produto_2)  # Divisão inteira: 2
print(produto_1 * produto_2)  # Multiplicação: 200
print(produto_1 % produto_2)  # Resto da divisão: 0
print(produto_1 ** produto_2)  # Potenciação: 10240000000000

x = (10 + 5) * 4  # x = (15) * 4 = 60
y = (10 / 2) + 25 * ((2 - 2) ** 2)  # y = 5 + 25 * (0 ** 2) = 5 + 25 * 0 = 5 + 0 = 5
print(x)  # 60
print(y)  # 5

