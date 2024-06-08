# Desafio v2: Sistema Bancário com Transações Limitadas e Iterador de Contas

## Introdução
Este código implementa um sistema bancário em Python que permite a criação de clientes e contas, além de realizar operações de depósito, saque e exibição de extratos. O sistema também inclui restrições no número de transações diárias e usa iteradores para listar contas. Este exemplo demonstra o uso prático do código e suas funcionalidades.

### Estrutura do Código
1. **Classes e Heranças:**
    - `Cliente` e `PessoaFisica`
    - `Conta` e `ContaCorrente`
    - `Historico`, `Transacao`, `Saque` e `Deposito`

2. **Funcionalidades:**
    - Criação de novos clientes e contas.
    - Realização de depósitos e saques com logs.
    - Limitação de transações diárias.
    - Exibição de extratos.
    - Iteração e listagem de contas.

### Exemplo de Uso

#### Configuração Inicial
```python
# Criação de Clientes
cliente1 = PessoaFisica(nome="João Silva", data_nascimento="01-01-1980", cpf="12345678900", endereco="Rua A, 123 - Bairro B - Cidade C/UF")
cliente2 = PessoaFisica(nome="Maria Oliveira", data_nascimento="05-05-1990", cpf="09876543211", endereco="Av. X, 456 - Bairro Y - Cidade Z/UF")

# Criação de Contas
conta1 = ContaCorrente.nova_conta(cliente=cliente1, numero=1, limite=500, limite_saques=3)
conta2 = ContaCorrente.nova_conta(cliente=cliente2, numero=2, limite=500, limite_saques=3)

# Adicionar Contas aos Clientes
cliente1.adicionar_conta(conta1)
cliente2.adicionar_conta(conta2)

# Lista de Clientes e Contas
clientes = [cliente1, cliente2]
contas = [conta1, conta2]
```

#### Operações de Depósito
```python
# Depositar dinheiro na conta de João
transacao_deposito = Deposito(200)
cliente1.realizar_transacao(conta1, transacao_deposito)

# Depositar dinheiro na conta de Maria
transacao_deposito = Deposito(300)
cliente2.realizar_transacao(conta2, transacao_deposito)
```

#### Operações de Saque
```python
# Sacar dinheiro da conta de João
transacao_saque = Saque(100)
cliente1.realizar_transacao(conta1, transacao_saque)

# Tentativa de saque que excede o saldo de Maria
transacao_saque = Saque(400)
cliente2.realizar_transacao(conta2, transacao_saque)
```

#### Exibição de Extrato
```python
# Exibir extrato da conta de João
for transacao in conta1.historico.gerar_relatorio():
    print(transacao)

# Exibir extrato da conta de Maria
for transacao in conta2.historico.gerar_relatorio():
    print(transacao)
```

#### Limitação de Transações Diárias
```python
# Realizar múltiplos saques na conta de João no mesmo dia
transacao_saque = Saque(50)
cliente1.realizar_transacao(conta1, transacao_saque)
cliente1.realizar_transacao(conta1, transacao_saque)
# Terceiro saque deve falhar devido ao limite diário
cliente1.realizar_transacao(conta1, transacao_saque)
```

#### Listagem de Contas
```python
# Listar todas as contas
for conta in ContasIterador(contas):
    print(conta)
```

#### Considerações Finais
O código apresentado demonstra um sistema bancário básico com funcionalidades de clientes e contas, incluindo restrições de transações diárias e uso de iteradores para listar contas. Este exemplo é uma base sólida para um sistema bancário mais completo e pode ser expandido conforme necessário.