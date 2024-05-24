from abc import ABC, abstractmethod, abstractproperty

# Classe abstrata ControleRemoto que define métodos abstratos para ligar, desligar e uma propriedade abstrata para a marca.
class ControleRemoto(ABC):
    # Método abstrato para ligar o dispositivo.
    @abstractmethod
    def ligar(self):
        pass

    # Método abstrato para desligar o dispositivo.
    @abstractmethod
    def desligar(self):
        pass

    # Propriedade abstrata para a marca do dispositivo.
    @property
    @abstractproperty
    def marca(self):
        pass

# Classe concreta ControleTV que herda de ControleRemoto e implementa os métodos ligar, desligar e a propriedade marca.
class ControleTV(ControleRemoto):
    # Implementação do método ligar para a TV.
    def ligar(self):
        print("Ligando a TV...")
        print("Ligada!")

    # Implementação do método desligar para a TV.
    def desligar(self):
        print("Desligando a TV...")
        print("Desligada!")

    # Implementação da propriedade marca para a TV.
    @property
    def marca(self):
        return "Philco"

# Classe concreta ControleArCondicionado que herda de ControleRemoto e implementa os métodos ligar, desligar e a propriedade marca.
class ControleArCondicionado(ControleRemoto):
    # Implementação do método ligar para o ar condicionado.
    def ligar(self):
        print("Ligando o Ar Condicionado...")
        print("Ligado!")

    # Implementação do método desligar para o ar condicionado.
    def desligar(self):
        print("Desligando o Ar Condicionado...")
        print("Desligado!")

    # Implementação da propriedade marca para o ar condicionado.
    @property
    def marca(self):
        return "LG"

# Cria uma instância de ControleTV e realiza operações de ligar, desligar e imprimir a marca.
controle_tv = ControleTV()
controle_tv.ligar()
controle_tv.desligar()
print(controle_tv.marca)

# Cria uma instância de ControleArCondicionado e realiza operações de ligar, desligar e imprimir a marca.
controle_ar = ControleArCondicionado()
controle_ar.ligar()
controle_ar.desligar()
print(controle_ar.marca)

