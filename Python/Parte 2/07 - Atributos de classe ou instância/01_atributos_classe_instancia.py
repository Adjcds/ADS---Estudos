# Definição da classe Estudante.
class Estudante:
    # Atributo de classe, compartilhado por todas as instâncias da classe.
    escola = "DIO"

    # Método inicializador da classe Estudante. É chamado quando uma nova instância é criada.
    def __init__(self, nome, matricula):
        # Atributos da instância são definidos com base nos parâmetros fornecidos.
        self.nome = nome
        self.matricula = matricula

    # Método especial que define a representação em string da instância da classe.
    def __str__(self) -> str:
        # Retorna uma string que contém o nome, matrícula e o nome da escola.
        return f"{self.nome} - {self.matricula} - {self.escola}"

# Função que aceita um número variável de objetos e imprime cada um deles.
def mostrar_valores(*objs):
    # Itera sobre os objetos fornecidos.
    for obj in objs:
        # Imprime a representação em string de cada objeto.
        print(obj)

# Cria instâncias da classe Estudante com nome e matrícula especificados.
aluno_1 = Estudante("Guilherme", 1)
aluno_2 = Estudante("Giovanna", 2)

# Chama a função mostrar_valores com as instâncias aluno_1 e aluno_2.
mostrar_valores(aluno_1, aluno_2)

# Modifica o atributo de classe escola para "Python".
Estudante.escola = "Python"

# Cria uma nova instância da classe Estudante com nome e matrícula especificados.
aluno_3 = Estudante("Chappie", 3)

# Chama a função mostrar_valores com as instâncias aluno_1, aluno_2 e aluno_3.
mostrar_valores(aluno_1, aluno_2, aluno_3)
