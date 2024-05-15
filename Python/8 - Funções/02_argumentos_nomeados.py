# Define uma função chamada salvar_carro que recebe os parâmetros marca, modelo, ano e placa.
def salvar_carro(marca, modelo, ano, placa):
    # Aqui normalmente haveria código para salvar o carro no banco de dados.
    # Para fins de exemplo, apenas imprime uma mensagem confirmando a inserção do carro.
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

# Chama a função salvar_carro passando os argumentos diretamente.
salvar_carro("Fiat", "Palio", 1999, "ABC-1234")

# Chama a função salvar_carro passando os argumentos nomeados.
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")

# Chama a função salvar_carro passando um dicionário com os argumentos usando o operador ** para desempacotar.
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})

# Resumo:
# O código define uma função salvar_carro que recebe quatro parâmetros: marca, modelo, ano e placa. 
# A função simula a inserção de um carro no banco de dados imprimindo uma mensagem de sucesso com as informações do carro.
# A função é chamada de três maneiras diferentes:
# 1. Passando os argumentos diretamente na chamada da função.
# 2. Passando os argumentos como parâmetros nomeados.
# 3. Passando os argumentos como um dicionário desempacotado usando o operador **.
# Todas as chamadas resultam na impressão da mensagem: "Carro inserido com sucesso! Fiat/Palio/1999/ABC-1234".
