import textwrap
# Importa o módulo 'textwrap' para facilitar a formatação de texto

from abc import ABC, abstractclassmethod, abstractproperty
# Importa 'ABC', 'abstractclassmethod' e 'abstractproperty' do módulo 'abc' para criação de classes abstratas

from datetime import datetime
# Importa 'datetime' para manipulação de datas e horas

class ContasIterador:
    def __init__(self, contas):
        self.contas = contas
        self._index = 0
    # Inicializa a classe 'ContasIterador' com uma lista de contas e define o índice inicial

    def __iter__(self):
        return self
    # Define o método '__iter__' que retorna o iterador

    def __next__(self):
        try:
            conta = self.contas[self._index]
            return f"""\
            Agência:\t{conta.agencia}
            Número:\t\t{conta.numero}
            Titular:\t{conta.cliente.nome}
            Saldo:\t\tR$ {conta.saldo:.2f}
        """
        except IndexError:
            raise StopIteration
        finally:
            self._index += 1
    # Define o método '__next__' que retorna os detalhes da próxima conta na lista, ou levanta 'StopIteration' se não houver mais contas

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
        self.indice_conta = 0
    # Inicializa a classe 'Cliente' com um endereço, uma lista de contas vazia e um índice de conta

    def realizar_transacao(self, conta, transacao):
        if len(conta.historico.transacoes_do_dia()) >= 2:
            print("\n@@@ Você excedeu o número de transações permitidas para hoje! @@@")
            return
        transacao.registrar(conta)
    # Realiza uma transação na conta, limitando a duas transações por dia

    def adicionar_conta(self, conta):
        self.contas.append(conta)
    # Adiciona uma conta à lista de contas do cliente

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
    # Inicializa a classe 'PessoaFisica' herdando de 'Cliente' e adicionando nome, data de nascimento e CPF

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
    # Inicializa a classe 'Conta' com número, cliente, saldo zero, agência e histórico

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    # Método de classe para criar uma nova conta

    @property
    def saldo(self):
        return self._saldo
    # Retorna o saldo da conta

    @property
    def numero(self):
        return self._numero
    # Retorna o número da conta

    @property
    def agencia(self):
        return self._agencia
    # Retorna a agência da conta

    @property
    def cliente(self):
        return self._cliente
    # Retorna o cliente da conta

    @property
    def historico(self):
        return self._historico
    # Retorna o histórico da conta

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
    # Método para sacar dinheiro da conta, verificando saldo e valor válido

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False
        return True
    # Método para depositar dinheiro na conta, verificando valor válido

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques
    # Inicializa a classe 'ContaCorrente' herdando de 'Conta' e adicionando limite e limite de saques

    @classmethod
    def nova_conta(cls, cliente, numero, limite, limite_saques):
        return cls(numero, cliente, limite, limite_saques)
    # Método de classe para criar uma nova conta corrente

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
    # Método para sacar dinheiro da conta corrente, verificando limite e número de saques

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """
    # Método para representar a conta corrente como string

class Historico:
    def __init__(self):
        self._transacoes = []
    # Inicializa a classe 'Historico' com uma lista de transações vazia

    @property
    def transacoes(self):
        return self._transacoes
    # Retorna a lista de transações

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )
    # Adiciona uma transação ao histórico

    def gerar_relatorio(self, tipo_transacao=None):
        for transacao in self._transacoes:
            if tipo_transacao is None or transacao["tipo"].lower() == tipo_transacao.lower():
                yield transacao
    # Gera um relatório das transações, filtrando por tipo se necessário

    def transacoes_do_dia(self):
        data_atual = datetime.utcnow().date()
        transacoes = []
        for transacao in self._transacoes:
            data_transacao = datetime.strptime(transacao["data"], "%d-%m-%Y %H:%M:%S").date()
            if data_atual == data_transacao:
                transacoes.append(transacao)
        return transacoes
    # Retorna as transações realizadas no dia atual

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass
    # Propriedade abstrata 'valor' para a classe 'Transacao'

    @abstractclassmethod
    def registrar(self, conta):
        pass
    # Método abstrato 'registrar' para a classe 'Transacao'

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
    # Inicializa a classe 'Saque' com o valor

    @property
    def valor(self):
        return self._valor
    # Retorna o valor do saque

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
    # Registra a transação de saque na conta

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor
    # Inicializa a classe 'Deposito' com o valor

    @property
    def valor(self):
        return self._valor
    # Retorna o valor do depósito

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
    # Registra a transação de depósito na conta

def log_transacao(func):
    def envelope(*args, **kwargs):
        resultado = func(*args, **kwargs)
        print(f"{datetime.now()}: {func.__name__.upper()}")
        return resultado
    return envelope
# Função decoradora para registrar logs de transações

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
# Função para exibir o menu principal e obter a escolha do usuário

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None
# Função para filtrar um cliente pelo CPF

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n@@@ Cliente não possui conta! @@@")
        return
    # FIXME: não permite cliente escolher a conta
    return cliente.contas[0]
# Função para recuperar a conta de um cliente, não permitindo escolher entre múltiplas contas

@log_transacao
def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return
    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    cliente.realizar_transacao(conta, transacao)
# Função para realizar um depósito, decorada para logar a transação

@log_transacao
def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return
    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    cliente.realizar_transacao(conta, transacao)
# Função para realizar um saque, decorada para logar a transação

@log_transacao
def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    print("\n================ EXTRATO ================")
    extrato = ""
    tem_transacao = False
    for transacao in conta.historico.gerar_relatorio():
        tem_transacao = True
        extrato += f'\n{transacao["tipo"]}:\n\tR$ {transacao["valor"]:.2f}'
    if not tem_transacao:
        extrato = "Não foram realizadas movimentações"
    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("==========================================")
# Função para exibir o extrato de um cliente, decorada para logar a transação

@log_transacao
def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente número): ")
    cliente = filtrar_cliente(cpf, clientes)
    if cliente:
        print("\n@@@ Já existe cliente com esse CPF! @@@")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
    clientes.append(cliente)
    print("\n=== Cliente criado com sucesso! ===")
# Função para criar um novo cliente, decorada para logar a transação

@log_transacao
def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print("\n@@@ Cliente não encontrado, fluxo de criação de conta encerrado! @@@")
        return
    # NOTE: O valor padrão de limite de saques foi alterado para 50 saques
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta, limite=500, limite_saques=50)
    contas.append(conta)
    cliente.contas.append(conta)
    print("\n=== Conta criada com sucesso! ===")
# Função para criar uma nova conta, decorada para logar a transação

def listar_contas(contas):
    for conta in ContasIterador(contas):
        print("=" * 100)
        print(textwrap.dedent(str(conta)))
# Função para listar todas as contas usando 'ContasIterador'

def main():
    clientes = []
    contas = []
    while True:
        opcao = menu()
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
# Função principal para executar o menu e realizar as operações com base na escolha do usuário

main()
# Executa a função principal para iniciar o programa
