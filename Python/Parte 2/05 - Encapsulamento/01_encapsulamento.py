class Conta:
    # Método inicializador da classe Conta. É chamado quando uma nova instância é criada.
    def __init__(self, nro_agencia, saldo=0):
        # Atributos da instância são definidos com base nos parâmetros fornecidos.
        self._saldo = saldo
        self.nro_agencia = nro_agencia

    # Método para depositar um valor na conta.
    def depositar(self, valor):
        # Adiciona o valor ao saldo atual.
        self._saldo += valor

    # Método para sacar um valor da conta.
    def sacar(self, valor):
        # Subtrai o valor do saldo atual.
        self._saldo -= valor

    # Método para mostrar o saldo atual da conta.
    def mostrar_saldo(self):
        # Retorna o saldo atual.
        return self._saldo

# Cria uma instância da classe Conta com número da agência e saldo inicial especificados.
conta = Conta("0001", 100)

# Chama o método depositar da instância conta com um valor de 100.
conta.depositar(100)

# Imprime o número da agência da conta.
print(conta.nro_agencia)

# Chama o método mostrar_saldo da instância conta e imprime o saldo atual.
print(conta.mostrar_saldo())
