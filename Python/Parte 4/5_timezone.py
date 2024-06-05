from datetime import datetime, timedelta, timezone  # Importa as classes datetime, timedelta e timezone do módulo datetime

# Obtém a data e hora atuais na zona de tempo "Europe/Oslo", que está 2 horas à frente do UTC
data_oslo = datetime.now(timezone(timedelta(hours=2)))

# Obtém a data e hora atuais na zona de tempo "America/Sao_Paulo", que está 3 horas atrás do UTC
data_sao_paulo = datetime.now(timezone(timedelta(hours=-3)))

# Imprime a data e hora atuais na zona de tempo "Europe/Oslo"
print(data_oslo)

# Imprime a data e hora atuais na zona de tempo "America/Sao_Paulo"
print(data_sao_paulo)
