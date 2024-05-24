# Definição da classe Pessoa.
class Pessoa:
    # Método inicializador da classe Pessoa. É chamado quando uma nova instância é criada.
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Método de classe que cria uma instância de Pessoa com base na data de nascimento.
    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        # Calcula a idade com base no ano de nascimento.
        idade = 2022 - ano
        # Retorna uma nova instância de Pessoa usando o construtor da classe.
        return cls(nome, idade)

    # Método estático que verifica se uma idade representa maioridade.
    @staticmethod
    def e_maior_idade(idade):
        # Retorna True se a idade for maior ou igual a 18, caso contrário, retorna False.
        return idade >= 18

# Cria uma instância de Pessoa usando o método de classe criar_de_data_nascimento.
p = Pessoa.criar_de_data_nascimento(1994, 3, 21, "Guilherme")
# Imprime o nome e a idade da pessoa criada.
print(p.nome, p.idade)  # Saída: Guilherme 28

# Verifica se uma idade é maioridade usando o método estático e imprime o resultado.
print(Pessoa.e_maior_idade(18))  # Saída: True
print(Pessoa.e_maior_idade(8))   # Saída: False
