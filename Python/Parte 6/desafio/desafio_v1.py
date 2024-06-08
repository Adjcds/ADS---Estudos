# Importando módulos necessários
import textwrap
from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

# Classe iteradora para percorrer contas
class contasIterador:
    def __init__(self, contas):  # Inicializa com a lista de contas e um índice
        self.contas = contas
        self._index = 0

    def __iter__(self):  # Torna a classe iterável
        return self

    def __next__(self):  # Define a lógica para iterar sobre as contas
        try:
            conta = self.contas[self._index]
            return f"""\
            Agência:\t{conta.agencia}
            Número:\t\t{conta.numero}
            Titular:\t{conta.cliente.nome}
            Saldo:\t\tR$ {conta.saldo:.2f}
        """
        except IndexError:  # Levanta exceção ao atingir o final da lista
            raise StopIteration
        finally:
            self._index += 1  # Incrementa o índice para a próxima iteração

# Classe para clientes
class Cliente:
    def __init__(self, endereco):  # Inicializa com o endereço e lista de contas vazia
        self.endereco = endereco
        self.contas = []
        self.indice_conta = 0

    def realizar_transacao(self, conta, transacao):  # Realiza transação se não exceder o limite diário
        if len(conta.historico.transacoes_do_dia()) >= 2:
            print("\n@@@ Você excedeu o número de transações permitidas para hoje! @@@")
            return

        transacao.registrar(conta)  # Registra a transação

    def adicionar_conta(self, conta):  # Adiciona uma nova conta ao cliente
        self.contas.append(conta)

# Classe para clientes pessoa física
class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):  # Inicializa com dados específicos
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

# Classe base para contas
class Conta:
    def __init__(self, numero, cliente):  # Inicializa a conta com saldo zero, agência fixa e histórico
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):  # Método de classe para criar nova conta
        return cls(numero, cliente)

    @property
    def saldo(self):  # Retorna o saldo da conta
        return self._saldo

    @property
    def numero(self):  # Retorna o número da conta
        return self._numero

    @property
    def agencia(self):  # Retorna a agência da conta
        return self._agencia

    @property
    def cliente(self):  # Retorna o cliente da conta
        return self._cliente

    @property
    def historico(self):  # Retorna o histórico de transações da conta
        return self._historico

    def sacar(self, valor):  # Lógica para saque
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:  # Verifica se o saldo é suficiente
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
        elif valor > 0:  # Verifica se o valor do saque é positivo
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True
        else:  # Valor inválido para saque
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

        return False

    def depositar(self, valor):  # Lógica para depósito
        if valor > 0:  # Verifica se o valor do depósito é positivo
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
        else:  # Valor inválido para depósito
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

        return True

# Classe para conta corrente, herda de Conta
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):  # Inicializa com limite e limite de saques
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    @classmethod
    def nova_conta(cls, cliente, numero, limite, limite_saques):  # Método de classe para criar nova conta corrente
        return cls(numero, cliente, limite, limite_saques)

    def sacar(self, valor):  # Lógica específica para saque em conta corrente
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self._limite  # Verifica se excedeu o limite do saque
        excedeu_saques = numero_saques >= self._limite_saques  # Verifica se excedeu o limite de saques

        if excedeu_limite:  # Caso valor do saque exceda o limite
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
        elif excedeu_saques:  # Caso número de saques exceda o limite
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
        else:  # Realiza o saque
            return super().sacar(valor)

        return False

    def __str__(self):  # Representação em string da conta corrente
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """

# Classe para histórico de transações
class Historico:
    def __init__(self):  # Inicializa com lista de transações vazia
        self._transacoes = []

    @property
    def transacoes(self):  # Retorna a lista de transações
        return self._transacoes

    def adicionar_transacao(self, transacao):  # Adiciona uma transação ao histórico
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )

    def gerar_relatorio(self, tipo_transacao=None):  # Gera um relatório de transações, filtrando por tipo se necessário
        for transacao in self._transacoes:
            if tipo_transacao is None or transacao["tipo"].lower() == tipo_transacao.lower():
                yield transacao

    def transacoes_do_dia(self):  # Retorna as transações do dia atual
        data_atual = datetime.utcnow().date()
        transacoes = []
        for transacao in self._transacoes:
            data_transacao = datetime.strptime(transacao["data"], "%d-%m-%Y %H:%M:%S").date()
            if data_atual == data_transacao:
                transacoes.append(transacao)
        return transacoes

# Classe abstrata para transações
class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):  # Propriedade abstrata para valor da transação
        pass

    @abstractclassmethod
    def registrar(self, conta):  # Método abstrato para registrar a transação
        pass

# Classe para saque, herda de Transacao
class Saque(Transacao):
    def __init__(self, valor):  # Inicializa com valor do saque
        self._valor = valor

    @property
    def valor(self):  # Retorna o valor do saque
        return self._valor

    def registrar(self, conta):  # Registra o saque na conta
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:  # Adiciona transação ao histórico se bem-sucedida
            conta.historico.adicionar_transacao(self)

# Classe para depósito, herda de Transacao
class Deposito(Transacao):
    def __init__(self, valor):  # Inicializa com valor do depósito
        self._valor = valor

    @property
    def valor(self):  # Retorna o valor do depósito
        return self._valor

    def registrar(self, conta):  # Registra o depósito na conta
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:  # Adiciona transação ao histórico se bem-sucedida
            conta.historico.adicionar_transacao(self)

# Decorador para log de transações
def log_transacao(func):
    def envelope(*args, **kwargs):  # Função envelope para adicionar log
        resultado = func(*args, **kwargs)
        print(f"{datetime.now()}: {func.__name__.upper()}")
        return resultado

    return envelope

# Função para exibir o menu de operações
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

# Função para filtrar cliente pelo CPF
def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

# Função para recuperar a conta do cliente
def recuperar_conta_cliente(cliente):
    if not cliente.contas:  # Verifica se o cliente possui contas
        print("\n@@@ Cliente não possui conta! @@@")
        return

    # FIXME: não permite cliente escolher a conta
    return cliente.contas[0]

# Função para realizar depósito
@log_transacao
def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:  # Verifica se o cliente existe
        print("\n@@@ Cliente não encontrado! @@@")
        return

    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:  # Verifica se o cliente possui conta
        return

    cliente.realizar_transacao(conta, transacao)

# Função para realizar saque
@log_transacao
def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:  # Verifica se o cliente existe
        print("\n@@@ Cliente não encontrado! @@@")
        return

    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:  # Verifica se o cliente possui conta
        return

    cliente.realizar_transacao(conta, transacao)

# Função para exibir extrato
@log_transacao
def exibirExtrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:  # Verifica se o cliente existe
        print("\n@@@ Cliente não encontrado! @@@")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:  # Verifica se o cliente possui conta
        return

    print("\n================ EXTRATO ================")
    extrato = ""
    tem_transacao = False
    for transacao in conta.historico.gerar_relatorio():  # Itera sobre as transações
        tem_transacao = True
        extrato += f'\n{transacao["tipo"]}:\n\tR$ {transacao["valor"]:.2f}'

    if not tem_transacao:  # Verifica se houve transações
        extrato = "Não foram realizadas movimentações"

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("==========================================")

# Função para criar novo cliente
@log_transacao
def criarCliente(clientes):
    cpf = input("Informe o CPF (somente número): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:  # Verifica se o cliente já existe
        print("\n@@@ Já existe cliente com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    clientes.append(cliente)  # Adiciona o novo cliente à lista

    print("\n=== Cliente criado com sucesso! ===")

# Função para criar nova conta
@log_transacao
def criarConta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:  # Verifica se o cliente existe
        print("\n@@@ Cliente não encontrado, fluxo de criação de conta encerrado! @@@")
        return

    # NOTE: O valor padrão de limite de saques foi alterado para 50 saques
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta, limite=500, limite_saques=50)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\n=== Conta criada com sucesso! ===")

# Função para listar todas as contas
def listarContas(contas):
    for conta in contasIterador(contas):  # Usa o iterador para percorrer as contas
        print("=" * 100)
        print(textwrap.dedent(str(conta)))

# Função principal que executa o programa
def main():
    clientes = []  # Lista de clientes
    contas = []  # Lista de contas

    while True:  # Loop infinito para menu de operações
        opcao = menu()

        if opcao == "d":
            depositar(clientes)
        elif opcao == "s":
            sacar(clientes)
        elif opcao == "e":
            exibirExtrato(clientes)
        elif opcao == "nu":
            criarCliente(clientes)
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criarConta(numero_conta, clientes, contas)
        elif opcao == "lc":
            listarContas(contas)
        elif opcao == "q":
            break
        else:
            print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")


main()  # Chama a função principal para iniciar o programa
