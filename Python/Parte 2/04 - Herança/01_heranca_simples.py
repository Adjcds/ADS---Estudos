# Definição da classe base Veiculo.
class Veiculo:
    # Método inicializador da classe Veiculo. É chamado quando uma nova instância é criada.
    def __init__(self, cor, placa, numero_rodas):
        # Atributos da instância são definidos com base nos parâmetros fornecidos.
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    # Método para simular ligar o motor do veículo.
    def ligar_motor(self):
        print("Ligando o motor")

    # Método especial que define a representação em string da instância da classe.
    def __str__(self):
        # Retorna uma string que contém o nome da classe e os atributos com seus valores.
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

# Definição da classe Motocicleta que herda da classe Veiculo.
class Motocicleta(Veiculo):
    # A classe Motocicleta herda todos os métodos e atributos da classe Veiculo sem adicionar novos.
    pass

# Definição da classe Carro que herda da classe Veiculo.
class Carro(Veiculo):
    # A classe Carro herda todos os métodos e atributos da classe Veiculo sem adicionar novos.
    pass

# Definição da classe Caminhao que herda da classe Veiculo.
class Caminhao(Veiculo):
    # Método inicializador da classe Caminhao. É chamado quando uma nova instância é criada.
    def __init__(self, cor, placa, numero_rodas, carregado):
        # Chama o método inicializador da classe base (Veiculo).
        super().__init__(cor, placa, numero_rodas)
        # Adiciona um novo atributo específico da classe Caminhao.
        self.carregado = carregado

    # Método para verificar se o caminhão está carregado.
    def esta_carregado(self):
        # Imprime se o caminhão está carregado com base no valor do atributo self.carregado.
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")

# Cria uma instância da classe Motocicleta com atributos especificados.
moto = Motocicleta("preta", "abc-1234", 2)
# Cria uma instância da classe Carro com atributos especificados.
carro = Carro("branco", "xde-0098", 4)
# Cria uma instância da classe Caminhao com atributos especificados, incluindo o atributo específico carregado.
caminhao = Caminhao("roxo", "gfd-8712", 8, True)

# Imprime a representação em string das instâncias moto, carro e caminhao.
print(moto)
print(carro)
print(caminhao)
