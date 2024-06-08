# Classe Plano, representa o plano de um usuário de telefone
class Plano:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial  # Inicializa o saldo do plano

    # Método para verificar o saldo atual
    def verificar_saldo(self):
        return self.saldo

    # Método para calcular o custo de uma chamada (supondo o custo de $0.10 por minuto)
    def custo_chamada(self, duracao):
        return duracao * 0.10  # Custo da chamada é a duração multiplicada pelo custo por minuto

    # Método para deduzir o valor do saldo do plano
    def deduzir_saldo(self, custo_chamada):
        self.saldo -= custo_chamada  # Deduz o custo da chamada do saldo do plano


# Classe UsuarioTelefone e o encapsulamento dos atributos nome, numero e plano
class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self.nome = nome
        self.numero = numero
        self.plano = plano

    # Método especial __str__ para representação em string do objeto
    def __str__(self):
        return f"Usuário {self.nome} criado com sucesso."


# Classe UsuarioPrePago, herda os atributos e métodos da classe UsuarioTelefone
class UsuarioPrePago(UsuarioTelefone):
    def __init__(self, nome, numero, saldo_inicial):
        super().__init__(nome, numero, Plano(saldo_inicial))  # Inicializa o plano com o saldo fornecido

    # Método para fazer uma chamada telefônica
    def fazer_chamada(self, destinatario, duracao):
        custo = self.plano.custo_chamada(duracao)  # Calcula o custo da chamada
        saldo_atual = self.plano.verificar_saldo()  # Verifica o saldo atual do plano

        if saldo_atual >= custo:  # Verifica se o saldo é suficiente para a chamada
            self.plano.deduzir_saldo(custo)  # Deduz o custo da chamada do saldo do plano
            return f"Chamada para {destinatario} realizada com sucesso. Saldo: ${saldo_atual - custo:.2f}"
        else:
            return "Saldo insuficiente para fazer a chamada."


# Recebendo as informações do usuário
nome = input()
numero = input()
saldo_inicial = float(input())

# Objeto de UsuarioPrePago com os dados fornecidos
usuario_pre_pago = UsuarioPrePago(nome, numero, saldo_inicial)

# Recebendo as informações da chamada
destinatario = input()
duracao = int(input())

# Chamada do método fazer_chamada do objeto usuario_pre_pago e impressão do resultado
print(usuario_pre_pago.fazer_chamada(destinatario, duracao))
