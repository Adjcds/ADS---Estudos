# Define uma função chamada exibir_poema que recebe uma string data_extenso, qualquer número de argumentos *args e argumentos nomeados **kwargs.
def exibir_poema(data_extenso, *args, **kwargs):
    # Junta todos os argumentos em args em uma única string, separada por quebras de linha.
    texto = "\n".join(args)
    # Cria uma lista de strings no formato "Chave: Valor" para cada item em kwargs, e junta essas strings com quebras de linha.
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    # Forma a mensagem final concatenando data_extenso, texto e meta_dados com duas quebras de linha entre cada parte.
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    # Imprime a mensagem final.
    print(mensagem)

# Chama a função exibir_poema com uma data_extenso e várias linhas de poema como args,
# seguido por informações adicionais como kwargs.
exibir_poema(
    "Zen of Python",
    "Beautiful is better than ugly.",
    "Explicit is better than implicit.",
    "Simple is better than complex.",
    "Complex is better than complicated.",
    "Flat is better than nested.",
    "Sparse is better than dense.",
    "Readability counts.",
    "Special cases aren't special enough to break the rules.",
    "Although practicality beats purity.",
    "Errors should never pass silently.",
    "Unless explicitly silenced.",
    "In the face of ambiguity, refuse the temptation to guess.",
    "There should be one-- and preferably only one --obvious way to do it.",
    "Although that way may not be obvious at first unless you're Dutch.",
    "Now is better than never.",
    "Although never is often better than *right* now.",
    "If the implementation is hard to explain, it's a bad idea.",
    "If the implementation is easy to explain, it may be a good idea.",
    "Namespaces are one honking great idea -- let's do more of those!",
    autor="Tim Peters",
    ano=1999,
)

# Resumo:
# O código define uma função exibir_poema que formata e imprime um poema com metadados adicionais.
# - data_extenso: Uma string que representa a data ou título do poema.
# - *args: Linhas do poema passadas como argumentos variáveis.
# - **kwargs: Informações adicionais sobre o poema passadas como argumentos nomeados.
# A função combina esses componentes em uma mensagem formatada e a imprime.
# Na chamada da função, um poema famoso "Zen of Python" é passado com várias linhas e metadados
# (autor e ano), que são então exibidos formatados na saída do console.
