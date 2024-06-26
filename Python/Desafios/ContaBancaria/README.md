# Sistema Bancário em Python

## Visão Geral

Este é um projeto de desenvolvimento de um sistema bancário em Python para um banco de grande porte que busca modernizar suas operações. A primeira versão deste sistema oferecerá funcionalidades básicas, incluindo depósito, saque e visualização de extrato.

## :battery: Stack utilizada
[![My Stack](https://skillicons.dev/icons?i=vscode,py,git)](https://skillicons.dev)

## Funcionalidades Principais

### Depósito:

- Os usuários podem depositar valores positivos em suas contas bancárias.
- Para começar a utilizar o sistema, é necessário realizar um depósito inicial.
- A versão inicial (v1) do sistema trabalha com apenas um usuário, eliminando a necessidade de especificar número de agência e conta bancária.
- Todos os depósitos são armazenados em uma variável e exibidos na operação de extrato.

### Saque:

- O sistema permite até três saques diários, com um limite máximo de R$ 500,00 por saque.
- Se o usuário não possuir saldo suficiente em conta, uma mensagem é exibida indicando a impossibilidade de realizar o saque devido à falta de saldo.
- Todos os saques são registrados em uma variável e apresentados na operação de extrato.

### Extrato:

- Esta operação fornece um histórico detalhado de todas as transações realizadas na conta, incluindo depósitos e saques.
- O extrato exibe o saldo atual da conta ao final da lista de transações.
- Se não houver movimentações registradas, uma mensagem indicando "Não foram realizadas movimentações" é exibida.
- Os valores são formatados em reais (R$) seguindo o padrão R$ xxx.xx.

## Arquivos no Repositório

- `contabancaria.py`: Contém o código do sistema bancário sem comentários, pronto para execução.
- `explicacao.py`: Contém o mesmo código do sistema bancário, mas com comentários explicando cada linha para facilitar o entendimento.

## Como Usar:

1. Clone este repositório em sua máquina local.
2. Execute o arquivo principal do sistema, `contaBancaria.py`.
3. Siga as instruções fornecidas pelo sistema para realizar depósitos, saques e visualizar o extrato.

## Autor:

Este projeto faz parte do Desafio da Digital Innovation One.
