from datetime import datetime  # Importa a classe datetime do módulo datetime
import pytz  # Importa o módulo pytz para manipulação de fusos horários

# Obtém a data e hora atuais na zona de tempo "Europe/Oslo"
data = datetime.now(pytz.timezone("Europe/Oslo"))

# Obtém a data e hora atuais na zona de tempo "America/Sao_Paulo"
data2 = datetime.now(pytz.timezone("America/Sao_Paulo"))

# Imprime a data e hora atuais na zona de tempo "Europe/Oslo"
print(data)

# Imprime a data e hora atuais na zona de tempo "America/Sao_Paulo"
print(data2)
