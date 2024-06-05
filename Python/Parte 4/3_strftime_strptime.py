from datetime import datetime  # Importa a classe datetime do módulo datetime

# Obtém a data e hora atuais
data_hora_atual = datetime.now()

# Define uma string representando uma data e hora específicas
data_hora_str = "2023-10-20 10:20"

# Define uma máscara de formatação para data e hora no formato brasileiro (dia/mês/ano dia-da-semana)
mascara_ptbr = "%d/%m/%Y %a"

# Define uma máscara de formatação para data e hora no formato ISO (ano-mês-dia hora:minuto)
mascara_en = "%Y-%m-%d %H:%M"

# Converte a data e hora atuais para a string formatada de acordo com a máscara brasileira
print(data_hora_atual.strftime(mascara_ptbr))

# Converte a string de data e hora para um objeto datetime usando a máscara ISO
data_convertida = datetime.strptime(data_hora_str, mascara_en)

# Imprime o objeto datetime resultante da conversão
print(data_convertida)

# Imprime o tipo do objeto datetime resultante para confirmar que é um objeto datetime
print(type(data_convertida))
