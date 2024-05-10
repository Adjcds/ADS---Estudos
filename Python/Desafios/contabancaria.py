class Conta():
    def __init__(self):
        self.LIMITE_VALOR_SAQUE = 500.0
        self.LIMITE_QUANTIDADE_SAQUE = 3
        self.saldo = 0.0
        self.extrato = ''
        self.numero_de_saques = 0

    def __str__(self):
        return f'{self.extrato}\nSaldo: R$ {self.saldo:.2f}'

    def depositar(self):
        valor = input('Digite o valor depositado -> ')
        if str(valor).isdecimal:
            aux = float(valor)
            if aux > 0:
                self.saldo += aux
                self.extrato += f'R$ {aux:.2f} D\n'
            else:
                print('Valor inválido para depósito')
        else:
            print('Digite um valor adequado para depósito')

    def sacar(self):
        valor = input('Digite o valor para saque -> ')
        if str(valor).isdecimal:
            aux = float(valor)
            if aux <= 0:
                print('Valor inválido para saque')
            elif self.saldo <= aux:
                print('Falta de saldo na conta')
            elif aux > self.LIMITE_VALOR_SAQUE:
                print(f'Limite do valor para saque ultrapassa o limite diário de R${self.LIMITE_VALOR_SAQUE:.2f}')
            elif self.numero_de_saques >= self.LIMITE_QUANTIDADE_SAQUE:
                print(f'Limite de saques diários atingido: {self.LIMITE_QUANTIDADE_SAQUE}')
            else:
                self.saldo -= aux
                self.extrato += f'R$ {aux:.2f} S\n'
                self.numero_de_saques += 1
        else:
            print('Digite um valor adequado para saque')

    def exibir_menu(self):
        print('\nMenu: Escolha uma opção:')
        print('[1] Depositar')
        print('[2] Sacar')
        print('[3] Extrato')
        print('[4] Sair')

    def executar_opcao(self, opcao):
        if opcao == '1':
            self.depositar()
        elif opcao == '2':
            self.sacar()
        elif opcao == '3':
            print(self)
        elif opcao == '4':
            exit()
        else:
            print('Opção inválida, tente novamente')

conta = Conta()
while True:
    conta.exibir_menu()
    opcao = input('=> ')
    conta.executar_opcao(opcao)
