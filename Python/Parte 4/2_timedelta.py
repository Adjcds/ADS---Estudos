from datetime import date, datetime, timedelta  # Importa as classes date, datetime e timedelta do módulo datetime

tipo_carro = "M"  # Define o tipo de carro como "M" (Médio). Pode ser "P" (Pequeno), "M" (Médio) ou "G" (Grande)
tempo_pequeno = 30  # Define o tempo estimado para carros pequenos (30 dias)
tempo_medio = 45  # Define o tempo estimado para carros médios (45 dias)
tempo_grande = 60  # Define o tempo estimado para carros grandes (60 dias)
data_atual = datetime.now()  # Obtém a data e hora atuais

# Verifica o tipo de carro e calcula a data estimada com base no tempo correspondente
if tipo_carro == "P":
    # Calcula a data estimada para carros pequenos subtraindo 30 dias da data atual
    data_estimada = data_atual - timedelta(days=tempo_pequeno)
    # Imprime a data de chegada e a data estimada para conclusão do serviço
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
elif tipo_carro == "M":
    # Calcula a data estimada para carros médios subtraindo 45 dias da data atual
    data_estimada = data_atual - timedelta(days=tempo_medio)
    # Imprime a data de chegada e a data estimada para conclusão do serviço
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
else:
    # Calcula a data estimada para carros grandes subtraindo 60 dias da data atual
    data_estimada = data_atual - timedelta(days=tempo_grande)
    # Imprime a data de chegada e a data estimada para conclusão do serviço
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")

# Calcula a data de ontem subtraindo 1 dia da data de hoje e imprime
print(date.today() - timedelta(days=1))

# Calcula o horário resultante subtraindo 1 hora de um datetime específico e imprime apenas o tempo
resultado = datetime(2023, 7, 25, 10, 19, 20) - timedelta(hours=1)
print(resultado.time())

# Imprime a data atual
print(datetime.now().date())
