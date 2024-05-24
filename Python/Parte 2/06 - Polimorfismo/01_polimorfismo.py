# Definição da classe base Passaro.
class Passaro:
    # Método que simula o voo de um pássaro.
    def voar(self):
        print("Voando...")

# Definição da classe Pardal que herda da classe Passaro.
class Pardal(Passaro):
    # Método que simula o voo de um pardal, sobrescrevendo o método da classe base.
    def voar(self):
        print("Pardal pode voar")

# Definição da classe Avestruz que herda da classe Passaro.
class Avestruz(Passaro):
    # Método que indica que um avestruz não pode voar, sobrescrevendo o método da classe base.
    def voar(self):
        print("Avestruz não pode voar")

# Definição da classe Aviao que herda da classe Passaro.
# Nota: Este é um exemplo ruim de uso de herança, pois um avião não é um pássaro.
class Aviao(Passaro):
    # Método que simula a decolagem de um avião, sobrescrevendo o método da classe base.
    def voar(self):
        print("Avião está decolando...")

# Função que chama o método voar de um objeto passado como parâmetro.
def plano_voo(obj):
    obj.voar()

# Testa a função plano_voo com instâncias de Pardal, Avestruz e Aviao.
plano_voo(Pardal())   # Saída: Pardal pode voar
plano_voo(Avestruz()) # Saída: Avestruz não pode voar
plano_voo(Aviao())    # Saída: Avião está decolando...
