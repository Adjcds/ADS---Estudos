def recomendar_plano(consumo_mensal):
  """
  Recomenda o plano de internet ideal com base no consumo médio mensal de dados.

  Args:
    consumo_mensal (float): O consumo médio mensal de dados em GB.

  Returns:
    str: A descrição do plano de internet ideal.
  """

  if consumo_mensal <= 10:
    return "Plano Essencial Fibra - 50Mbps"
  elif consumo_mensal <= 20:
    return "Plano Prata Fibra - 100Mbps"
  else:
    return "Plano Premium Fibra - 300Mbps"

# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input())
# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
print(recomendar_plano(consumo))