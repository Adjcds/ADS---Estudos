from abc import ABC, abstractclassmethod, abstractproperty  # Importa as classes ABC, abstractclassmethod e abstractproperty do módulo abc
from datetime import datetime  # Importa a classe datetime do módulo datetime

# Classe Cliente representa um cliente do banco
class Cliente:
    # Inicializa o cliente com um endereço e uma lista vazia de contas
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    # Método para realizar uma transação em uma conta
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    # Método para adicionar uma conta à lista de contas do cliente
    def adicionar_conta(self, conta):
        self.contas.append(conta)

# Classe PessoaFisica representa um cliente pessoa física do banco
class PessoaFisica(Cliente):
    # Inicializa a pessoa física com nome, data de nascimento, CPF e endereço
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

# Classe Conta representa uma conta bancária
class Conta:
    # Inicializa a conta com número, cliente associado, saldo e histórico
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    # Método de classe para criar uma nova conta
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    # Propriedades para saldo, número, agência, cliente e histórico da conta
    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    # Método para sacar dinheiro da conta
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

    # Método para depositar dinheiro na conta
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

        return True

# Classe ContaCorrente representa uma conta corrente
class ContaCorrente(Conta):
    # Inicializa a conta corrente com limite de saque e limite de saques
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    # Método para sacar dinheiro da conta corrente
    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

        else:
            return super().sacar(valor)

        return False

    # Representação em string da conta corrente
    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """

# Classe Historico representa o histórico de transações de uma conta
class Historico:
    # Inicializa o histórico com uma lista vazia de transações
    def __init__(self):
        self._transacoes = []

    # Propriedade para acessar a lista de transações
    @property
    def transacoes(self):
        return self._transacoes

    # Método para adicionar uma transação ao histórico
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )

# Classe Transacao é uma classe abstrata que representa uma transação bancária
class Transacao(ABC):
    # Propriedade abstrata para o valor da transação
    @property
    @abstractproperty
    def valor(self):
        pass

    # Método abstrato para registrar a transação em uma conta
    @abstractclassmethod
    def registrar(self, conta):
        pass

# Classe Saque representa uma transação de saque
class Saque(Transacao):
    # Inicializa o saque com um valor
    def __init__(self, valor):
        self._valor = valor

    # Propriedade para acessar o valor do saque
    @property
    def valor(self):
        return self._valor

    # Método para registrar o saque em uma conta
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

# Classe Deposito representa uma transação de depósito
class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
