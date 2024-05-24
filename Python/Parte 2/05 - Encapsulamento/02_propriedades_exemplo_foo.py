class Foo:
    # Método inicializador da classe Foo. É chamado quando uma nova instância é criada.
    def __init__(self, x=None):
        # Atributo privado _x é definido com base no parâmetro fornecido.
        self._x = x

    # Propriedade x para acessar o valor de _x.
    @property
    def x(self):
        # Retorna _x se for não-nulo, caso contrário retorna 0.
        return self._x or 0

    # Setter para a propriedade x.
    @x.setter
    def x(self, value):
        # Adiciona o valor fornecido a _x.
        self._x += value

    # Deleter para a propriedade x.
    @x.deleter
    def x(self):
        # Define _x como 0.
        self._x = 0

# Cria uma instância da classe Foo com o valor inicial de _x definido como 10.
foo = Foo(10)

# Imprime o valor da propriedade x, que deve ser 10.
print(foo.x)

# Deleta a propriedade x, definindo _x como 0.
del foo.x

# Imprime o valor da propriedade x, que agora deve ser 0.
print(foo.x)

# Define a propriedade x, adicionando 10 a _x (que atualmente é 0).
foo.x = 10

# Imprime o valor da propriedade x, que agora deve ser 10.
print(foo.x)
