class Cachorro:
    # Método inicializador da classe Cachorro. É chamado quando uma nova instância é criada.
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")
        # Atributos da instância são definidos com base nos parâmetros fornecidos.
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    # Método especial chamado quando a instância é destruída.
    def __del__(self):
        print("Removendo a instância da classe.")

    # Método para simular o latido do cachorro.
    def falar(self):
        print("auau")


# Função que cria uma instância da classe Cachorro.
def criar_cachorro():
    # Cria uma instância local da classe Cachorro.
    c = Cachorro("Zeus", "Branco e preto", False)
    # Imprime o nome do cachorro.
    print(c.nome)
    # A instância c será removida ao final da função, chamando o método __del__.

# Cria uma instância da classe Cachorro com atributos especificados.
c = Cachorro("Chappie", "amarelo")
# Chama o método falar da instância c.
c.falar()

print("Ola mundo")

# Remove a instância c, chamando o método __del__.
del c

print("Ola mundo")
print("Ola mundo")
print("Ola mundo")

# Descomentar a linha abaixo para testar a função criar_cachorro.
# criar_cachorro()
