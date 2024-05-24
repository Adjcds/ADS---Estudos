class Bicicleta:
    # Método inicializador da classe Bicicleta. É chamado quando uma nova instância é criada.
    def __init__(self, cor, modelo, ano, valor):
        # Atributos da instância são definidos com base nos parâmetros fornecidos.
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    # Método para simular o som da buzina da bicicleta.
    def buzinar(self):
        print("Plim plim...")

    # Método para simular a ação de parar a bicicleta.
    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    # Método para simular a bicicleta correndo.
    def correr(self):
        print("Vrummmmm...")

    # Método especial que define a representação em string da instância da classe.
    def __str__(self):
        # Retorna uma string que contém o nome da classe e os atributos com seus valores.
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

# Cria uma instância da classe Bicicleta com atributos especificados.
b1 = Bicicleta("vermelha", "caloi", 2022, 600)
# Chama o método buzinar da instância b1.
b1.buzinar()
# Chama o método correr da instância b1.
b1.correr()
# Chama o método parar da instância b1.
b1.parar()
# Imprime os atributos cor, modelo, ano e valor da instância b1.
print(b1.cor, b1.modelo, b1.ano, b1.valor)

# Cria outra instância da classe Bicicleta com atributos diferentes.
b2 = Bicicleta("verde", "monark", 2000, 189)
# Utiliza o método __str__ para imprimir a representação da instância b2.
print(b2)
# Chama o método correr da instância b2.
b2.correr()
