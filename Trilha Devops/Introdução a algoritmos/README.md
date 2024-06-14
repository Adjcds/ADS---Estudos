# Guia sobre Introdução a Algoritmos

## Sumário
1. [Apresentando algoritmos](#apresentando-algoritmos)
2. [Fluxos simples e Sequencial](#fluxos-simples-e-sequencial)
3. [Tipos de Dados](#tipos-de-dados)
4. [Decisão](#decisão)
5. [Repetição](#repetição)
6. [Exercícios Part 1](#exercícios-part-1)
    - [Questão 1](#questão-1)
    - [Questão 2](#questão-2)
    - [Questão 3](#questão-3)
7. [Listas/Arrays](#listas-arrays)
8. [Funções](#funções)
9. [Exercício completo (pseudocódigo)](#exercício-completo-pseudocódigo)
10. [Desempenho de algoritmos](#desempenho-de-algoritmos)
11. [Dicas para montar algoritmos](#dicas-para-montar-algoritmos)

## Apresentando algoritmos

Algoritmos são conjuntos de instruções bem definidas e finitas para resolver um problema ou realizar uma tarefa específica. Eles podem ser representados em linguagem natural, pseudocódigo ou diagramas de fluxo.

## Fluxos simples e Sequencial

### Fluxos simples
Fluxos simples representam a execução linear de instruções, onde uma instrução segue a outra.

### Fluxo Sequencial
No fluxo sequencial, as instruções são executadas em ordem, uma após a outra, exatamente como estão escritas.

## Tipos de Dados

### Tipos de Dados Comuns

- **Inteiros (INTEIRO)**: Números sem parte decimal.
- **Reais (REAL)**: Números com parte decimal.
- **Caracteres (CARACTER)**: Letras, números ou símbolos.
- **Cadeia de caracteres (STRING)**: Sequência de caracteres.
- **Booleanos (BOOLEANO)**: Verdadeiro ou falso.

## Decisão

A estrutura de decisão permite que um algoritmo tome diferentes caminhos com base em condições especificadas.

### Estruturas de Decisão
- **SE...ENTAO...SENAO**: Executa um bloco de código se a condição for verdadeira, senão executa outro bloco.

## Repetição

A estrutura de repetição permite que um bloco de código seja executado várias vezes com base em uma condição.

### Estruturas de Repetição
- **ENQUANTO**: Repete um bloco de código enquanto a condição for verdadeira.

## Exercícios Part 1

### Questão 1

**Código:**

```plaintext
REAL a, b

ESCREVA "digite um número: "
LEIA a
ESCREVA "digite um número: "
LEIA b
ESCREVA "a * b = ", a * b
```

**Execução:**

```plaintext
digite um número: 50
digite um número: 2
a * b = 100
```

**Resposta:** a * b = 100

### Questão 2

**Código:**

```plaintext
CARACTER senha
INTEIRO i

ESCREVA "Para continuar, digite sua senha: "
LEIA senha

i <- 0

ENQUANTO senha != "a6b5c4" FAÇA
  ESCREVA "Senha inválida"
  i <- i + 1
  ESCREVA "Para continuar, digite sua senha: "
  LEIA senha

FIM_ENQUANTO

ESCREVA "Seja bem-vindo(a) à área do cliente"
```

**Execução:**
Márcia digita a senha 7 vezes até acertar, ou seja, ela erra 6 vezes antes de digitar a senha correta.

**Resposta:** O valor armazenado em i ao final da execução é 6.

### Questão 3

**Código:**

```plaintext
INTEIRO x1, x2
REAL res

ESCREVA "digite um número positivo"
LEIA x1
ESCREVA "digite outro número positivo"
LEIA x2

SE (x1 > x2) ENTAO FAÇA
    res <- (x1 - x2) / x1
SENAO FAÇA
    res <- (x2 - x1) / x2
FIM_SE

ESCREVA res
```

**Execução:**

- Para os valores [3, 12]:
  - `x1 = 3`, `x2 = 12`
  - `res <- (12 - 3) / 12 = 0.75`
  - Resposta: 0.75

- Para os valores [5, 5]:
  - `x1 = 5`, `x2 = 5`
  - `res <- (5 - 5) / 5 = 0.0`
  - Resposta: 0.0

- Para os valores [10, 8]:
  - `x1 = 10`, `x2 = 8`
  - `res <- (10 - 8) / 10 = 0.2`
  - Resposta: 0.2

**Resposta:** 0.75, 0.0, 0.2

## Listas/Arrays

Listas ou arrays são estruturas de dados que armazenam múltiplos valores em uma única variável. Cada valor pode ser acessado por um índice.

### Exemplo

```plaintext
INTEIRO lista[5]
lista[0] <- 10
lista[1] <- 20
lista[2] <- 30
lista[3] <- 40
lista[4] <- 50
```

## Funções

Funções são blocos de código reutilizáveis que realizam uma tarefa específica. Elas podem receber parâmetros e retornar valores.

### Exemplo

```plaintext
FUNÇÃO SOMA(a, b)
  RETORNE a + b
FIM_FUNÇÃO

INTEIRO resultado
resultado <- SOMA(5, 3)
ESCREVA resultado
```

## Exercício completo (pseudocódigo)

**Problema:** Calcular a média de uma lista de números.

**Pseudocódigo:**

```plaintext
FUNÇÃO CALCULA_MEDIA(lista, tamanho)
  REAL soma, media
  INTEIRO i
  soma <- 0
  PARA i DE 0 ATÉ tamanho - 1 FAÇA
    soma <- soma + lista[i]
  FIM_PARA
  media <- soma / tamanho
  RETORNE media
FIM_FUNÇÃO

INTEIRO lista[5], tamanho
REAL media
tamanho <- 5
lista[0] <- 10
lista[1] <- 20
lista[2] <- 30
lista[3] <- 40
lista[4] <- 50

media <- CALCULA_MEDIA(lista, tamanho)
ESCREVA "A média é: ", media
```

## Desempenho de algoritmos

O desempenho de um algoritmo é medido em termos de tempo de execução e uso de memória. A análise de complexidade de tempo e espaço ajuda a avaliar a eficiência de algoritmos.

### Complexidade de Tempo

- **O(1)**: Tempo constante
- **O(n)**: Tempo linear
- **O(n^2)**: Tempo quadrático

## Dicas para montar algoritmos

1. **Defina o problema claramente**: Entenda o que precisa ser resolvido.
2. **Divida o problema em partes menores**: Resolva cada parte individualmente.
3. **Use pseudocódigo**: Escreva um esboço do algoritmo em linguagem natural.
4. **Teste com exemplos**: Verifique se o algoritmo funciona com diferentes casos de teste.
5. **Otimize**: Procure maneiras de tornar o algoritmo mais eficiente.

---

Este guia é parte do curso de DevOps do Santander Coders 2024 em parceria com a Ada Tech. Para mais informações, consulte a documentação oficial e os recursos de aprendizado disponíveis.

**Autor:** [AdrielleJcds](https://github.com/Adjcds)  
**E-mail:** adrielle.dev@gmail.com  
**Última Atualização:** [14/06/2024]