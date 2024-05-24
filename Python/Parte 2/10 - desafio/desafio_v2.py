# Importing necessary modules
import textwrap  # For text formatting
from abc import ABC, abstractclassmethod, abstractproperty  # For abstract base classes
from datetime import datetime  # For handling date and time


# Class representing a client of the bank
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []  # List to store associated accounts

    # Method to perform a transaction on an account
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    # Method to add a new account to the client
    def adicionar_conta(self, conta):
        self.contas.append(conta)


# Subclass of Cliente representing an individual person
class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


# Class representing a bank account
class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()  # Instance of transaction history

    # Class method to create a new account
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    # Property to access the account balance
    @property
    def saldo(self):
        return self._saldo

    # Property to access the account number
    @property
    def numero(self):
        return self._numero

    # Property to access the agency of the account
    @property
    def agencia(self):
        return self._agencia

    # Property to access the client associated with the account
    @property
    def cliente(self):
        return self._cliente

    # Property to access the transaction history of the account
    @property
    def historico(self):
        return self._historico

    # Method to withdraw money from the account
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

        elif valor > 0:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True

        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

        return False

    # Method to deposit money into the account
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

        return True


# Subclass of Conta representing a checking account
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    # Method to withdraw money from the checking account
    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

        else:
            return super().sacar(valor)

        return False

    # Method to return a string representation of the checking account
    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """


# Class representing the transaction history
class Historico:
    def __init__(self):
        self._transacoes = []

    # Property to access the transactions of the history
    @property
    def transacoes(self):
        return self._transacoes

    # Method to add a transaction to the history
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )

# Definição de uma classe base abstrata (ABC) representando uma transação
class Transacao(ABC):
    # Propriedade abstrata representando o valor da transação
    @property
    @abstractproperty
    def valor(self):
        pass

    # Método de classe abstrato para registrar a transação em uma conta
    @abstractclassmethod
    def registrar(self, conta):
        pass


# Subclasse de Transacao representando uma transação de saque
class Saque(Transacao):
    # Construtor para inicializar a transação de saque com um valor especificado
    def __init__(self, valor):
        self._valor = valor

    # Propriedade para recuperar o valor do saque
    @property
    def valor(self):
        return self._valor

    # Método para registrar a transação de saque na conta
    def registrar(self, conta):
        # Realiza uma transação de saque na conta
        sucesso_transacao = conta.sacar(self.valor)

        # Se a transação de saque for bem-sucedida, adiciona-a ao histórico de transações da conta
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


# Subclasse de Transacao representando uma transação de depósito
class Deposito(Transacao):
    # Construtor para inicializar a transação de depósito com um valor especificado
    def __init__(self, valor):
        self._valor = valor

    # Propriedade para recuperar o valor do depósito
    @property
    def valor(self):
        return self._valor

    # Método para registrar a transação de depósito na conta
    def registrar(self, conta):
        # Realiza uma transação de depósito na conta
        sucesso_transacao = conta.depositar(self.valor)

        # Se a transação de depósito for bem-sucedida, adiciona-a ao histórico de transações da conta
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


# Função para exibir um menu de operações bancárias e solicitar entrada do usuário
def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


# Função para filtrar clientes com base no seu CPF
def filtrar_cliente(cpf, clientes):
    # Filtra clientes cujo CPF corresponde ao CPF fornecido
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    # Retorna o primeiro cliente correspondente, se encontrado, caso contrário, retorna None
    return clientes_filtrados[0] if clientes_filtrados else None


# Função para recuperar a primeira conta associada a um cliente
def recuperar_conta_cliente(cliente):
    # Se o cliente não tiver contas, exibe uma mensagem e retorna None
    if not cliente.contas:
        print("\n@@@ Cliente não possui conta! @@@")
        return

    # FIXME: Esta parte não permite que o cliente escolha a conta, sempre retorna a primeira conta
    return cliente.contas[0]


# Função para realizar uma transação de depósito para um cliente
def depositar(clientes):
    # Solicita ao usuário que informe o CPF do cliente
    cpf = input("Informe o CPF do cliente: ")
    # Filtra clientes com base no CPF fornecido
    cliente = filtrar_cliente(cpf, clientes)

    # Se nenhum cliente for encontrado, exibe uma mensagem e retorna
    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    # Solicita ao usuário que informe o valor do depósito
    valor = float(input("Informe o valor do depósito: "))
    # Cria um objeto de transação de depósito com o valor especificado
    transacao = Deposito(valor)

    # Recupera a primeira conta associada ao cliente
    conta = recuperar_conta_cliente(cliente)
    # Se nenhuma conta for encontrada, retorna
    if not conta:
        return

    # Realiza a transação de depósito para a conta do cliente
    cliente.realizar_transacao(conta, transacao)

# Função para realizar uma transação de saque para um cliente
def sacar(clientes):
    # Solicita ao usuário que informe o CPF do cliente
    cpf = input("Informe o CPF do cliente: ")
    # Filtra clientes com base no CPF fornecido
    cliente = filtrar_cliente(cpf, clientes)

    # Se nenhum cliente for encontrado, exibe uma mensagem e retorna
    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    # Solicita ao usuário que informe o valor do saque
    valor = float(input("Informe o valor do saque: "))
    # Cria um objeto de transação de saque com o valor especificado
    transacao = Saque(valor)

    # Recupera a primeira conta associada ao cliente
    conta = recuperar_conta_cliente(cliente)
    # Se nenhuma conta for encontrada, retorna
    if not conta:
        return

    # Realiza a transação de saque para a conta do cliente
    cliente.realizar_transacao(conta, transacao)


# Função para exibir o extrato bancário de um cliente
def exibir_extrato(clientes):
    # Solicita ao usuário que informe o CPF do cliente
    cpf = input("Informe o CPF do cliente: ")
    # Filtra clientes com base no CPF fornecido
    cliente = filtrar_cliente(cpf, clientes)

    # Se nenhum cliente for encontrado, exibe uma mensagem e retorna
    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    # Recupera a primeira conta associada ao cliente
    conta = recuperar_conta_cliente(cliente)
    # Se nenhuma conta for encontrada, retorna
    if not conta:
        return

    # Exibe um cabeçalho indicando que o extrato está sendo mostrado
    print("\n================ EXTRATO ================")
    # Obtém todas as transações da conta do cliente
    transacoes = conta.historico.transacoes

    # Inicializa uma string para armazenar o extrato
    extrato = ""
    # Verifica se há transações na conta
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        # Itera sobre cada transação e formata a string do extrato
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"

    # Imprime o extrato bancário e o saldo atual da conta
    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("==========================================")


# Função para criar um novo cliente
def criar_cliente(clientes):
    # Solicita ao usuário que informe o CPF do cliente
    cpf = input("Informe o CPF (somente número): ")
    # Filtra clientes com base no CPF fornecido
    cliente = filtrar_cliente(cpf, clientes)

    # Verifica se já existe um cliente com o CPF informado
    if cliente:
        print("\n@@@ Já existe cliente com esse CPF! @@@")
        return

    # Solicita ao usuário que informe os dados do novo cliente
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    # Cria um novo objeto de cliente PessoaFisica com os dados fornecidos
    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    # Adiciona o novo cliente à lista de clientes
    clientes.append(cliente)

    print("\n=== Cliente criado com sucesso! ===")


# Função para criar uma nova conta para um cliente
def criar_conta(numero_conta, clientes, contas):
    # Solicita ao usuário que informe o CPF do cliente
    cpf = input("Informe o CPF do cliente: ")
    # Filtra clientes com base no CPF fornecido
    cliente = filtrar_cliente(cpf, clientes)

    # Se nenhum cliente for encontrado, exibe uma mensagem e retorna
    if not cliente:
        print("\n@@@ Cliente não encontrado, fluxo de criação de conta encerrado! @@@")
        return

    # Cria uma nova conta corrente associada ao cliente e com o número de conta especificado
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    # Adiciona a nova conta à lista de contas
    contas.append(conta)
    # Adiciona a nova conta à lista de contas associadas ao cliente
    cliente.contas.append(conta)

    print("\n=== Conta criada com sucesso! ===")


# Função para listar todas as contas existentes
def listar_contas(contas):
    # Itera sobre cada conta na lista de contas
    for conta in contas:
        # Imprime uma linha de separação para cada conta
        print("=" * 100)
        # Imprime os detalhes da conta
        print(textwrap.dedent(str(conta)))


# Função principal responsável por executar o programa
def main():
    # Inicializa listas vazias para armazenar clientes e contas
    clientes = []
    contas = []

    # Loop principal do programa
    while True:
        # Exibe o menu de operações bancárias e solicita a escolha do usuário
        opcao = menu()

        # Verifica a opção selecionada pelo usuário e executa a operação correspondente
        if opcao == "d":
            depositar(clientes)
        elif opcao == "s":
            sacar(clientes)
        elif opcao == "e":
            exibir_extrato(clientes)
        elif opcao == "nu":
            criar_cliente(clientes)
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            break
        else:
            print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")


main()
