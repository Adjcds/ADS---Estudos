# Define uma variável global chamada salario com o valor inicial de 2000.
salario = 2000

# Define uma função chamada salario_bonus que recebe um parâmetro bonus.
def salario_bonus(bonus):
    global salario  # Declara que vamos usar a variável global salario dentro da função.
    salario += bonus  # Adiciona o valor do bonus ao salario.
    return salario  # Retorna o novo valor de salario.

# Chama a função salario_bonus com o argumento 500.
# Isso adicionará 500 ao salario global, resultando em um novo salario de 2500.
salario_bonus(500)  # 2500

# Resumo:
# O código define uma variável global salario com um valor inicial de 2000 e uma função salario_bonus que adiciona um bônus a essa variável global.
# A função salario_bonus usa a declaração global para modificar a variável global salario.
# Quando salario_bonus(500) é chamada, 500 é adicionado ao salario, resultando em um novo valor de 2500.
# O valor atualizado de salario é então retornado pela função.
