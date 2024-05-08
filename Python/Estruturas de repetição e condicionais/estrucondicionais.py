# Definindo constantes para a idade mínima para tirar a CNH
MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

# Solicitando ao usuário que informe sua idade
idade = int(input("Informe sua idade: "))

# Verificando se a idade informada é maior ou igual à idade mínima para tirar a CNH
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CHN.")
    
# Verificando se a idade informada é menor que a idade mínima para tirar a CNH
if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH.")

# Utilizando uma estrutura condicional com 'if' e 'else'
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CHN.")
else:
    print("Ainda não pode tirar a CNH.")

# Utilizando uma estrutura condicional com 'if', 'elif' e 'else'
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CHN.")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas.")
else:
    print("Ainda não pode tirar a CNH.")
