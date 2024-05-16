# Definição da classe Conta
class Conta():
    # Método inicializador da classe
    def __init__(self):
        # Definindo o limite de valor para saque diário
        self.LIMITE_VALOR_SAQUE = 500.0
        # Definindo o limite de quantidade de saques diários
        self.LIMITE_QUANTIDADE_SAQUE = 3
        # Inicializando o saldo da conta
        self.saldo = 0.0
        # Inicializando o extrato da conta como uma string vazia
        self.extrato = ''
        # Inicializando o contador de número de saques
        self.numero_de_saques = 0

    # Método para representar o objeto como string (extrato e saldo)
    def __str__(self):
        return f'{self.extrato}\nSaldo: R$ {self.saldo:.2f}'

    # Método para depositar dinheiro na conta
    def depositar(self):
        # Solicita o valor a ser depositado
        valor = input('Digite o valor depositado -> ')
        # Verifica se o valor é numérico
        if str(valor).isdecimal:
            aux = float(valor)
            # Verifica se o valor é positivo
            if aux > 0:
                # Adiciona o valor ao saldo
                self.saldo += aux
                # Atualiza o extrato
                self.extrato += f'R$ {aux:.2f} D\n'
            else:
                print('Valor inválido para depósito')
        else:
            print('Digite um valor adequado para depósito')

    # Método para sacar dinheiro da conta
    def sacar(self):
        # Solicita o valor a ser sacado
        valor = input('Digite o valor para saque -> ')
        # Verifica se o valor é numérico
        if str(valor).isdecimal:
            aux = float(valor)
            # Verifica se o valor é positivo
            if aux <= 0:
                print('Valor inválido para saque')
            # Verifica se há saldo suficiente
            elif self.saldo <= aux:
                print('Falta de saldo na conta')
            # Verifica se o valor ultrapassa o limite diário
            elif aux > self.LIMITE_VALOR_SAQUE:
                print(f'Limite do valor para saque ultrapassa o limite diário de R${self.LIMITE_VALOR_SAQUE:.2f}')
            # Verifica se o limite de saques diários foi atingido
            elif self.numero_de_saques >= self.LIMITE_QUANTIDADE_SAQUE:
                print(f'Limite de saques diários atingido: {self.LIMITE_QUANTIDADE_SAQUE}')
            else:
                # Subtrai o valor do saldo
                self.saldo -= aux
                # Atualiza o extrato
                self.extrato += f'R$ {aux:.2f} S\n'
                # Incrementa o contador de saques
                self.numero_de_saques += 1
        else:
            print('Digite um valor adequado para saque')

    # Método para exibir o menu de opções
    def exibir_menu(self):
        print('\nMenu: Escolha uma opção:')
        print('[1] Depositar')
        print('[2] Sacar')
        print('[3] Extrato')
        print('[4] Sair')

    # Método para executar a opção escolhida
    def executar_opcao(self, opcao):
        if opcao == '1':
            self.depositar()
        elif opcao == '2':
            self.sacar()
        elif opcao == '3':
            # Exibe o extrato e saldo
            print(self)
        elif opcao == '4':
            # Encerra o programa
            exit()
        else:
            print('Opção inválida, tente novamente')

# Criação de uma instância da classe Conta
conta = Conta()
# Loop principal para exibir o menu e executar a opção escolhida
while True:
    conta.exibir_menu()
    opcao = input('=> ')
    conta.executar_opcao(opcao)
