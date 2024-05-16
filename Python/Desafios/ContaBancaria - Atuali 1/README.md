# :bank:💰💸 Sistema Bancário Aprimorado em Python

## Visão Geral

Este projeto aprimora o sistema bancário original em Python, atendendo às necessidades do desafio da Digital Innovation One. As funcionalidades básicas de depósito, saque e extrato foram otimizadas e novas funções foram implementadas para maior modularidade e flexibilidade.

## :battery: Stack utilizada
[![My Stack](https://skillicons.dev/icons?i=vscode,py,git)](https://skillicons.dev)

## Melhorias Implementadas

* **Separação em Funções:** As operações de saque, depósito e extrato agora são realizadas por funções independentes, tornando o código mais organizado e reutilizável.
* **Argumentos Aprimorados:** As funções possuem argumentos nomeados e posicionais, facilitando a compreensão e o uso.
* **Novas Funções:**
    * `criar_usuario(nome, data_nascimento, cpf, endereco)`: Cadastra um novo usuário no sistema, armazenando seus dados em uma lista.
    * `criar_conta_corrente(agencia, numero_conta, usuario)`: Cria uma conta corrente para um usuário, associando-a à agência 0001 e incrementando automaticamente o número da conta.
* **Validação de CPF:** O sistema garante que não existam usuários com CPFs duplicados.
* **Vinculação Usuário-Conta:** A criação de uma conta corrente vincula automaticamente o usuário informado à conta.
* **Referência ao Desafio Original:** Incluída para facilitar a consulta e o acompanhamento do progresso.

## Instruções de Uso

1. Clone o repositório em sua máquina local.
2. Execute o arquivo `contabancaria2.py`.
3. Siga as instruções na tela para realizar as operações bancárias.

## Observações

* O sistema ainda está em desenvolvimento e novas funcionalidades podem ser implementadas no futuro.

## Próximos Passos

* Implementar autenticação de usuário para maior segurança.
* Permitir a consulta de saldo e extrato por conta específica.
* Oferecer a opção de transferência entre contas.

## Esperamos que este sistema bancário aprimorado seja útil para você!

## Contribuições e Melhorias

Este projeto está em constante evolução e agradecemos suas contribuições para torná-lo ainda melhor. Sinta-se à vontade para sugerir novas funcionalidades, reportar bugs ou enviar pull requests com suas melhorias.

Juntos, podemos construir um sistema bancário completo e robusto em Python!

## Documentação Detalhada

Além disso, o arquivo `explicacao.py` contém uma explicação detalhada do código linha por linha, ajudando a entender como cada parte do sistema funciona. Certifique-se de consultá-lo para um entendimento aprofundado da implementação.

## Autor:

Este projeto faz parte do Desafio da Digital Innovation One.
