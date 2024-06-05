from datetime import date, datetime, time  # Importa as classes date, datetime e time do módulo datetime

# Cria um objeto de data específica (10 de julho de 2023) usando a classe date
data = date(2023, 7, 10)
print(data)  # Imprime a data especificada (2023-07-10)

# Imprime a data atual usando o método today() da classe date
print(date.today())

# Cria um objeto de data e hora específica (10 de julho de 2023, meia-noite) usando a classe datetime
data_hora = datetime(2023, 7, 10)
print(data_hora)  # Imprime a data e hora especificada (2023-07-10 00:00:00)

# Imprime a data e hora atual usando o método today() da classe datetime
print(datetime.today())

# Cria um objeto de hora específica (10:20:00) usando a classe time
hora = time(10, 20, 0)
print(hora)  # Imprime a hora especificada (10:20:00)
