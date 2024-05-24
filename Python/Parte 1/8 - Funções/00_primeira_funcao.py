# Define uma função chamada exibir_mensagem que não recebe argumentos e imprime "Olá mundo!".
def exibir_mensagem():
    print("Olá mundo!")  # Imprime a mensagem "Olá mundo!" no console.

# Define uma função chamada exibir_mensagem_2 que recebe um argumento 'nome' e imprime uma mensagem personalizada.
def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")  # Imprime a mensagem "Seja bem vindo" seguida do nome fornecido.

# Define uma função chamada exibir_mensagem_3 que recebe um argumento opcional 'nome' com valor padrão "Anônimo".
def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")  # Imprime a mensagem "Seja bem vindo" seguida do nome fornecido ou "Anônimo" se nenhum nome for passado.

# Chama a função exibir_mensagem, que imprime "Olá mundo!".
exibir_mensagem()

# Chama a função exibir_mensagem_2 com o argumento 'nome' definido como "Adrielle", que imprime "Seja bem vindo Adrielle!".
exibir_mensagem_2(nome="Adrielle")

# Chama a função exibir_mensagem_3 sem argumentos, então imprime "Seja bem vindo Anônimo!".
exibir_mensagem_3()

# Chama a função exibir_mensagem_3 com o argumento 'nome' definido como "Challie", que imprime "Seja bem vindo Challie!".
exibir_mensagem_3(nome="Challie")

# Resumo:
# O código define três funções para exibir mensagens de boas-vindas no console.
# 1. exibir_mensagem(): Imprime "Olá mundo!" sem precisar de argumentos.
# 2. exibir_mensagem_2(nome): Imprime uma mensagem personalizada de boas-vindas com o nome fornecido como argumento.
# 3. exibir_mensagem_3(nome="Anônimo"): Semelhante à segunda função, mas usa "Anônimo" como valor padrão se nenhum nome for fornecido.
#    Se um nome for fornecido, ele substitui o valor padrão.
# As chamadas às funções demonstram seu funcionamento:
# - exibir_mensagem(): Imprime "Olá mundo!".
# - exibir_mensagem_2(nome="Adrielle"): Imprime "Seja bem vindo Adrielle!".
# - exibir_mensagem_3(): Imprime "Seja bem vindo Anônimo!".
# - exibir_mensagem_3(nome="Challie"): Imprime "Seja bem vindo Challie!".
