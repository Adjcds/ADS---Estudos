# while condição:
    # Bloco de código a ser repetido enquanto a condição for verdadeira

# Inicializa a variável 'opcao' com o valor -1 para garantir que o loop seja executado pelo menos uma vez,
# pois a condição do while verifica se 'opcao' é diferente de 0. Se 'opcao' fosse inicializado com 0,
# o loop não seria executado se o usuário digitasse 0 imediatamente.
opcao = -1  

# Inicia o loop 'while'. Enquanto a variável 'opcao' for diferente de 0, o bloco de código dentro do 'while' será executado repetidamente.
while opcao != 0:
    # Solicita ao usuário que escolha uma opção digitando um número. O valor digitado é armazenado na variável 'opcao'.
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    # Verifica se a opção escolhida pelo usuário é igual a 1. Se for, imprime "Sacando...".
    if opcao == 1:
        print("Sacando...")
    # Verifica se a opção escolhida pelo usuário é igual a 2. Se for, imprime "Exibindo o extrato...".
    elif opcao == 2:
        print("Exibindo o extrato...")
    # Se nenhuma das condições anteriores for atendida, ou seja, se o usuário escolher a opção 0 para sair,
    # o bloco de código dentro do 'else' será executado.
    else:
        # Imprime uma mensagem de agradecimento ao usuário por usar o sistema bancário e encerra o loop 'while'.
        print("Obrigado por usar nosso sistema bancário, até logo!")
