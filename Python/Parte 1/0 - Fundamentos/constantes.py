##  1 - parte 1: Assim as variáveis, constantes são ultilizadas para armazenar valores. Uma constante nasce com um valor e permanece com ele até o final da execução do programa, ou seja, o valor é imutável. 

##PYTHON NÃO TEM CONSTANTES

# Não existe uma palavra reservada para informar ao interpretador que o valor é constante. Em algumas linguagens por exemplo: JAVA e C ultilizamos final e const, respectivamente para declarar uma constante.
# Em PYTHON usamos a convenção que diz ao progdramador que a variável é uma constante. Para fazer isso, você deve criar a variável com o nome todo em letras maíusculas:

nome = "Guilherme"
idade = 28

nome, idade = "Giovanna", 27

print(nome, idade)

limite_saque_diario = 1000

BRAZILIAN_STATES = ["SP", "RJ", "SC", "RS"] #isso é uma constante

print(BRAZILIAN_STATES) 

## boas praticas 

## -- o padrão de nomes deve ser snake case.
## -- escolher nomes sugestivos.
## -- nomes de constantes todo em maiúsculo.

