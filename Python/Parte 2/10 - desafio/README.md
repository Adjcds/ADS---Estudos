# Sistema Bancário Simples

## Descrição do Projeto
Este projeto consiste em um sistema bancário simples desenvolvido em Python. Ele oferece funcionalidades básicas, como criar novos clientes, abrir novas contas bancárias, depositar e sacar dinheiro, exibir extrato e listar contas.

## Funcionalidades
### 1. Novo Usuário
Na opção "Novo Usuário", o programa permite a criação de um novo cliente informando o CPF, nome completo, data de nascimento e endereço.

### 2. Nova Conta
Após criar um novo usuário, o usuário pode abrir uma nova conta bancária na opção "Nova Conta". O sistema atribuirá automaticamente um número de conta e uma agência para a nova conta, que será associada ao cliente previamente cadastrado.

### 3. Depositar
Na opção "Depositar", é possível realizar depósitos em uma conta bancária existente. O usuário precisará fornecer o CPF do cliente e o valor do depósito.

### 4. Sacar
A opção "Sacar" permite que o usuário faça saques de uma conta bancária existente. O usuário precisará fornecer o CPF do cliente e o valor a ser sacado.

### 5. Extrato
Ao selecionar "Extrato", o programa exibirá o extrato bancário de uma conta específica, mostrando todas as transações realizadas, incluindo depósitos e saques, juntamente com o saldo atual da conta.

### 6. Listar Contas
Na opção "Listar Contas", o programa exibirá uma lista de todos os clientes e suas respectivas contas bancárias, juntamente com as informações de agência e número de conta.

### 7. Limite Diário
O sistema impõe um limite diário para saques, que é definido como R$ 500,00 por padrão. Além disso, o número máximo de saques permitidos por dia é definido como 3.

## Dados dos Clientes

O programa utiliza uma lista de nomes fictícios para gerar dados aleatórios de clientes. Abaixo está uma amostra dos nomes fictícios dos clientes utilizados no projeto, juntamente com outras informações como endereço, data de nascimento e CPF:

- **Nome:** João Silva
  - **Endereço:** 1234 Rua das Flores, 100 - Centro - São Paulo
  - **Data de Nascimento:** 01-05-1988
  - **CPF:** 123.456.789-00

- **Nome:** Maria Santos
  - **Endereço:** 5678 Avenida Monteiro, 200 - Vila - Rio de Janeiro
  - **Data de Nascimento:** 15-09-1975
  - **CPF:** 987.654.321-00

- **Nome:** Pedro Oliveira
  - **Endereço:** 9101 Rua Silva, 300 - Jardim - Belo Horizonte
  - **Data de Nascimento:** 10-11-1990
  - **CPF:** 456.789.123-00

- **Nome:** Ana Souza
  - **Endereço:** 2345 Avenida Pereira, 400 - Centro - São Paulo
  - **Data de Nascimento:** 20-03-1982
  - **CPF:** 654.321.987-00

- **Nome:** Lucas Pereira
  - **Endereço:** 6789 Rua das Flores, 150 - Jardim - Rio de Janeiro
  - **Data de Nascimento:** 05-07-1978
  - **CPF:** 321.987.654-00

Estes são exemplos de clientes fictícios utilizados no programa. Durante a execução do programa, esses clientes são utilizados para realizar diferentes operações bancárias, como abrir contas, realizar depósitos e saques, entre outros.

## Utilização
Para utilizar o programa, basta executar o arquivo `desafio_v2.py` em um ambiente Python. O programa exibirá um menu interativo que permitirá ao usuário selecionar as diferentes opções disponíveis.

