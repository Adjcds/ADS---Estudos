### Exemplo de Uso - Desafio V1

#### 1. Criar um Novo Cliente

- **Menu:** `=> [nu]`
- **Entrada:** 
  ```sh
  Informe o CPF (somente número): 12345678900
  Informe o nome completo: João Silva
  Informe a data de nascimento (dd-mm-aaaa): 01-01-1990
  Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): Rua das Flores, 123 - Centro - São Paulo/SP
  ```
- **Saída:**
  ```sh
  === Cliente criado com sucesso! ===
  ```

#### 2. Criar uma Nova Conta para o Cliente

- **Menu:** `=> [nc]`
- **Entrada:** 
  ```sh
  Informe o CPF do cliente: 12345678900
  ```
- **Saída:**
  ```sh
  === Conta criada com sucesso! ===
  ```

#### 3. Realizar um Depósito

- **Menu:** `=> [d]`
- **Entrada:** 
  ```sh
  Informe o CPF do cliente: 12345678900
  Informe o valor do depósito: 1000.00
  ```
- **Saída:**
  ```sh
  === Depósito realizado com sucesso! ===
  ```

#### 4. Realizar um Saque

- **Menu:** `=> [s]`
- **Entrada:** 
  ```sh
  Informe o CPF do cliente: 12345678900
  Informe o valor do saque: 200.00
  ```
- **Saída:**
  ```sh
  === Saque realizado com sucesso! ===
  ```

#### 5. Exibir Extrato

- **Menu:** `=> [e]`
- **Entrada:** 
  ```sh
  Informe o CPF do cliente: 12345678900
  ```
- **Saída:**
  ```sh
  ================ EXTRATO ================
  Deposito:
      R$ 1000.00
  Saque:
      R$ 200.00
  Saldo:
      R$ 800.00
  ==========================================
  ```

#### 6. Listar Todas as Contas

- **Menu:** `=> [lc]`
- **Saída:**
  ```sh
  ====================================================================================================
  Agência: 0001
  Número: 1
  Titular: João Silva
  Saldo: R$ 800.00
  ```

#### 7. Sair do Programa

- **Menu:** `=> [q]`

### Resumo

Neste exemplo de uso do **Desafio V1**, o cliente João Silva foi criado e uma conta corrente foi aberta para ele. Foi realizado um depósito de R$ 1000,00 e um saque de R$ 200,00. O extrato da conta foi exibido, mostrando as transações e o saldo restante. Finalmente, todas as contas foram listadas e o programa foi encerrado.