#Aprender como receber e exibir informações para o usuário.

## Função input 

### A função builtin input é utilizada quando queremos ler dados da entrada padrão(teclado). Ela recebe um argumento do tipo string, que é exibido para o usuário na saída padrão (tela). A função lê a entrada, converte para string e retorna o valor.
### A função builtin input é utilizada quando queremos exibir dados na saída padrão (tela). Ela recebe um argumneto obrigatório do tipo varargs de objetos e 4 argumentos opcionais (sep, end, file e flush). Todos os objetos são convertidos para string, separados por sep e terminados por end. A string final é exibida para o usuário.

nome = input("Informe o seu nome: ")
idade = input("Informe a sua idade: ")

print(nome, idade)
print(nome, idade, end="...\n")
print(nome, idade, sep="#", end="...\n")
print(nome, idade, sep="#")