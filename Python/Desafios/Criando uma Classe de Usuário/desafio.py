# Definição da classe UsuarioTelefone
class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self.nome = nome  # Atributo nome do usuário
        self.numero = numero  # Atributo número de telefone
        self.plano = plano  # Atributo plano associado

    # Método especial __str__ para representação em string do objeto
    def __str__(self):
        return f"Usuário {self.nome} criado com sucesso."

# Entrada dos dados do usuário
nome = input()  # Solicitação do nome do usuário
numero = input()  # Solicitação do número de telefone
plano = input()  # Solicitação do plano associado

# Criação de um objeto UsuarioTelefone com os dados fornecidos
usuario = UsuarioTelefone(nome, numero, plano)

# Impressão da mensagem de sucesso
print(usuario)  # Saída da mensagem indicando que o usuário foi criado com sucesso
