import textwrap  # Importa o módulo textwrap para manipulação de texto, para facilitar o ajuste conjunto de
#ferramentas valiosas para formatar texto de forma eficiente e elegante. Seja para ajustar o texto à largura da tela,
#remover espaços em branco redundantes ou criar parágrafos com visualização impecável,
# o textwrap se torna um aliado indispensável em diversas tarefas.

# Função para exibir o menu de opções e obter a escolha do usuário
def menu():
    menu = """\n
    ====== ESCOLHA UMA OPERAÇÃO ========

    [1]\tDepositar Valor
    [2]\tSacar Valor
    [3]\tConsultar Extrato
    [4]\tCriar Novo usuário
    [5]\tAbrir conta
    [6]\tListar contas
    [x]\tEncerrar Operação

    >>  """
    return input(textwrap.dedent(menu))  # Exibe o menu e retorna a escolha do usuário

# Função para realizar depósito
def depositar(saldo, valor, extrato, /):
    if valor > 0:  # Verifica se o valor do depósito é positivo
        saldo += valor  # Adiciona o valor ao saldo
        extrato += f"Depósito:\tR$ {valor:.2f}\n"  # Adiciona o depósito ao extrato
        print("\n!!! Depósito realizado com sucesso! !!!")
    else:
        print("\n## Falha na operação! O valor informado é inválido. ##")

    return saldo, extrato  # Retorna o saldo atualizado e o extrato

# Função para realizar saque
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo  # Verifica se o valor do saque excede o saldo
    excedeu_limite = valor > limite  # Verifica se o valor do saque excede o limite permitido
    excedeu_saques = numero_saques >= limite_saques  # Verifica se o número de saques excede o limite diário

    if excedeu_saldo:
        print("\n## Falha na operação! Você não tem saldo suficiente. ##")

    elif excedeu_limite:
        print("\n## Falha na operação! O valor do saque excede o limite de saque único. ##")

    elif excedeu_saques:
        print("\n## Falha na operação! Número máximo de saque diário excedido. ##")

    elif valor > 0:
        saldo -= valor  # Subtrai o valor do saldo
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"  # Adiciona o saque ao extrato
        numero_saques += 1  # Incrementa o contador de saques
        print("\n!!! Saque realizado! Recolha seu dinheiro. !!!")

    else:
        print("\n## Falha na operação! O valor informado é inválido. ##")

    return saldo, extrato, numero_saques  # Retorna saldo, extrato e número de saques atualizados

# Função para exibir o extrato
def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================\n")
    print("Não foram realizadas movimentações." if not extrato else extrato)  # Verifica se há movimentações
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")  # Exibe o saldo atual
    print("\n=========================================\n")

# Função para criar um novo usuário
def criar_usuario(usuarios):
    cpf = input("Digite seu CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)  # Verifica se o usuário já existe

    if usuario:
        print("\n## Erro! Já existe usuário com esse CPF! ##")
        return

    nome = input("Digite seu nome completo: ")
    data_nascimento = input("Digite sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Digite seu endereço (Logradouro, nº - Bairro - Cidade/UF): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})  # Adiciona o novo usuário à lista

    print("\n!!! Usuário criado com sucesso! !!!")

# Função para filtrar usuário por CPF
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]  # Busca o usuário pelo CPF
    return usuarios_filtrados[0] if usuarios_filtrados else None  # Retorna o usuário encontrado ou None

# Função para criar uma nova conta
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)  # Busca o usuário pelo CPF

    if usuario:
        print("\n!!! Conta criada com sucesso! !!!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}  # Retorna os detalhes da nova conta

    print("\n## Usuário não encontrado! Retornando para o início. ##")

# Função para listar todas as contas
def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 40)
        print(textwrap.dedent(linha))  # Exibe os detalhes de cada conta

# Função principal que coordena a execução do programa
def main():
    LIMITE_SAQUES = 3  # Define o limite diário de saques
    AGENCIA = "0001"  # Define o número da agência

    saldo = 0  # Saldo inicial
    limite = 500  # Limite de saque por operação
    extrato = ""  # Histórico de transações
    numero_saques = 0  # Contador de saques realizados
    usuarios = []  # Lista de usuários
    contas = []  # Lista de contas

    while True:  # Loop principal do programa
        opcao = menu()  # Exibe o menu e obtém a escolha do usuário

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)  # Realiza o depósito

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )  # Realiza o saque

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)  # Exibe o extrato

        elif opcao == "4":
            criar_usuario(usuarios)  # Cria um novo usuário

        elif opcao == "5":
            numero_conta = len(contas) + 1  # Gera o número da nova conta
            conta = criar_conta(AGENCIA, numero_conta, usuarios)  # Cria uma nova conta

            if conta:
                contas.append(conta)  # Adiciona a nova conta à lista

        elif opcao == "6":
            listar_contas(contas)  # Lista todas as contas

        elif opcao == "x":
            break  # Encerra o programa

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

# Chama a função principal para iniciar o programa
main()
