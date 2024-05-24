# Definição da classe base Animal.
class Animal:
    # Método inicializador da classe Animal. É chamado quando uma nova instância é criada.
    def __init__(self, nro_patas):
        # Atributo da instância é definido com base no parâmetro fornecido.
        self.nro_patas = nro_patas

    # Método especial que define a representação em string da instância da classe.
    def __str__(self):
        # Retorna uma string que contém o nome da classe e os atributos com seus valores.
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

# Definição da classe Mamifero que herda da classe Animal.
class Mamifero(Animal):
    # Método inicializador da classe Mamifero. É chamado quando uma nova instância é criada.
    def __init__(self, cor_pelo, **kw):
        # Atributo específico da classe Mamifero.
        self.cor_pelo = cor_pelo
        # Chama o método inicializador da classe base (Animal) com os argumentos fornecidos.
        super().__init__(**kw)

# Definição da classe Ave que herda da classe Animal.
class Ave(Animal):
    # Método inicializador da classe Ave. É chamado quando uma nova instância é criada.
    def __init__(self, cor_bico, **kw):
        # Atributo específico da classe Ave.
        self.cor_bico = cor_bico
        # Chama o método inicializador da classe base (Animal) com os argumentos fornecidos.
        super().__init__(**kw)

# Definição da classe Gato que herda da classe Mamifero.
class Gato(Mamifero):
    # A classe Gato herda todos os métodos e atributos da classe Mamifero sem adicionar novos.
    pass

# Definição da classe Ornitorrinco que herda tanto da classe Mamifero quanto da classe Ave.
class Ornitorrinco(Mamifero, Ave):
    # Método inicializador da classe Ornitorrinco. É chamado quando uma nova instância é criada.
    def __init__(self, cor_bico, cor_pelo, nro_patas):
        # Chama o método inicializador das classes base (Mamifero e Ave) com os argumentos fornecidos.
        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, nro_patas=nro_patas)

# Cria uma instância da classe Gato com atributos especificados.
gato = Gato(nro_patas=4, cor_pelo="Preto")
# Imprime a representação em string da instância gato.
print(gato)

# Cria uma instância da classe Ornitorrinco com atributos especificados.
ornitorrinco = Ornitorrinco(nro_patas=2, cor_pelo="vermelho", cor_bico="laranja")
# Imprime a representação em string da instância ornitorrinco.
print(ornitorrinco)
