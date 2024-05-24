class Pessoa:
    # Método inicializador da classe Pessoa. É chamado quando uma nova instância é criada.
    def __init__(self, nome, ano_nascimento):
        # Atributos da instância são definidos com base nos parâmetros fornecidos.
        self.nome = nome
        self._ano_nascimento = ano_nascimento

    # Propriedade calculada idade, que retorna a idade da pessoa.
    @property
    def idade(self):
        # Ano atual fixo para o cálculo da idade.
        _ano_atual = 2022
        # Calcula a idade subtraindo o ano de nascimento do ano atual.
        return _ano_atual - self._ano_nascimento

# Cria uma instância da classe Pessoa com nome e ano de nascimento especificados.
pessoa = Pessoa("Guilherme", 1994)

# Imprime o nome e a idade da pessoa.
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")
