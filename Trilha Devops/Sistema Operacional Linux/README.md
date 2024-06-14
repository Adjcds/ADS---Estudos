# Guia sobre Sistema Operacional Linux

## Sumário
1. [Introdução ao Linux](#introdução-ao-linux)
2. [Introdução ao Terminal/Bash](#introdução-ao-terminalbash)
3. [Executando os primeiros comandos](#executando-os-primeiros-comandos)
4. [Identificando e criando arquivos e diretórios](#identificando-e-criando-arquivos-e-diretórios)
5. [Copiando e apagando arquivos e diretórios](#copiando-e-apagando-arquivos-e-diretórios)
6. [Exercícios de fixação I](#exercícios-de-fixação-i)
    - [Questão 1](#questão-1)
    - [Questão 2](#questão-2)
    - [Questão 3](#questão-3)
    - [Questão 4](#questão-4)
    - [Questão 5](#questão-5)
7. [Instalando programas e movendo arquivos e diretórios](#instalando-programas-e-movendo-arquivos-e-diretórios)
8. [Visualizando o conteúdo e editando arquivos](#visualizando-o-conteúdo-e-editando-arquivos)
9. [Comprimindo arquivos e diretórios](#comprimindo-arquivos-e-diretórios)
10. [Um pouco sobre Shell Script e Permissões](#um-pouco-sobre-shell-script-e-permissões)
11. [Procurando Arquivos e Diretórios](#procurando-arquivos-e-diretórios)
12. [Exercícios de fixação II](#exercícios-de-fixação-ii)
    - [Questão 1](#questão-1)
    - [Questão 2](#questão-2)

## Introdução ao Linux

Linux é um sistema operacional de código aberto amplamente utilizado em servidores, dispositivos embarcados e desktops. É conhecido por sua estabilidade, segurança e flexibilidade.

## Introdução ao Terminal/Bash

O Terminal é a interface de linha de comando do Linux, onde os usuários podem digitar comandos para executar tarefas. O Bash (Bourne Again Shell) é um dos interpretadores de comandos mais populares no Linux.

### Abrindo o Terminal

Para abrir o Terminal, você pode usar o atalho de teclado `Ctrl + Alt + T` ou procurar por "Terminal" no menu de aplicativos.

## Executando os primeiros comandos

Aqui estão alguns comandos básicos para começar no Terminal:

- `ls`: Lista os arquivos e diretórios no diretório atual.
- `pwd`: Mostra o caminho do diretório atual.
- `cd [diretório]`: Navega para o diretório especificado.
- `echo [mensagem]`: Exibe uma mensagem no Terminal.

## Identificando e criando arquivos e diretórios

### Comandos para Arquivos e Diretórios

- `touch [nome_do_arquivo]`: Cria um novo arquivo vazio.
- `mkdir [nome_do_diretório]`: Cria um novo diretório.
- `ls -l`: Lista arquivos e diretórios com detalhes.

### Exemplos

```sh
touch arquivo.txt
mkdir novo_diretorio
ls -l
```

## Copiando e apagando arquivos e diretórios

### Comandos

- `cp [origem] [destino]`: Copia arquivos ou diretórios.
- `mv [origem] [destino]`: Move ou renomeia arquivos ou diretórios.
- `rm [arquivo]`: Remove arquivos.
- `rmdir [diretório]`: Remove diretórios vazios.
- `rm -r [diretório]`: Remove diretórios e seu conteúdo recursivamente.

### Exemplos

```sh
cp arquivo.txt copia_arquivo.txt
mv copia_arquivo.txt novo_diretorio/
rm arquivo.txt
rmdir novo_diretorio
rm -r diretorio_com_arquivos
```

## Exercícios de fixação I

### Questão 1

**Pergunta:** Qual comando é utilizado para remover (excluir) diretórios vazios no Linux?

**Resposta:** `rmdir`

**Explicação:** O comando `rmdir` é usado para remover diretórios vazios. Ele falha se o diretório contiver qualquer arquivo ou subdiretório.

### Questão 2

**Pergunta:** Qual comando é utilizado para remover arquivos e diretórios de forma permanente no Linux?

**Resposta:** `rm`

**Explicação:** O comando `rm` remove arquivos e diretórios permanentemente. Quando usado sem opções, ele remove arquivos. Para remover diretórios, é necessário utilizar opções adicionais, como `-r` para remoção recursiva.

### Questão 3

**Pergunta:** Qual argumento é utilizado no comando `rm` para remover recursivamente um diretório e todo o seu conteúdo?

**Resposta:** `-r`

**Explicação:** A opção `-r` (ou `--recursive`) no comando `rm` é usada para remover diretórios e seus conteúdos de forma recursiva. Isso significa que todos os arquivos e subdiretórios dentro do diretório especificado serão removidos.

### Questão 4

**Pergunta:** Qual opção do comando `cp` preserva as permissões originais dos arquivos copiados?

**Resposta:** `-p`

**Explicação:** A opção `-p` (ou `--preserve`) no comando `cp` preserva as permissões, o proprietário e o grupo dos arquivos copiados, mantendo as mesmas propriedades dos arquivos originais.

### Questão 5

**Pergunta:** Qual opção do comando `cp` copia apenas os arquivos de origem que são mais recentes do que os arquivos de destino ou que não existem?

**Resposta:** `-u`

**Explicação:** A opção `-u` (ou `--update`) no comando `cp` faz com que apenas os arquivos de origem que são mais novos que os arquivos de destino ou que não existam no destino sejam copiados. Isso evita a substituição de arquivos no destino que já são mais novos ou idênticos aos de origem.

## Instalando programas e movendo arquivos e diretórios

### Instalando Programas

Para instalar programas, você pode usar o gerenciador de pacotes da sua distribuição Linux. Exemplos:

- **Ubuntu/Debian:** `sudo apt-get install [nome_do_programa]`
- **Fedora:** `sudo dnf install [nome_do_programa]`
- **Arch Linux:** `sudo pacman -S [nome_do_programa]`

### Movendo Arquivos e Diretórios

Para mover arquivos e diretórios, use o comando `mv`:

```sh
mv arquivo.txt /caminho/para/novo_local/
mv diretorio /caminho/para/novo_local/
```

## Visualizando o conteúdo e editando arquivos

### Visualizando Conteúdo

- `cat [arquivo]`: Exibe o conteúdo do arquivo.
- `less [arquivo]`: Exibe o conteúdo do arquivo de forma paginada.
- `head [arquivo]`: Exibe as primeiras linhas do arquivo.
- `tail [arquivo]`: Exibe as últimas linhas do arquivo.

### Editando Arquivos

Editores de texto comuns no Terminal:

- **nano:** Simples e fácil de usar. `nano [arquivo]`
- **vim:** Poderoso e altamente configurável. `vim [arquivo]`

## Comprimindo arquivos e diretórios

### Comandos de Compressão

- `tar -czvf arquivo.tar.gz [arquivos/diretórios]`: Cria um arquivo comprimido no formato .tar.gz.
- `tar -xzvf arquivo.tar.gz`: Extrai um arquivo comprimido no formato .tar.gz.

### Exemplos

```sh
tar -czvf backup.tar.gz diretorio/
tar -xzvf backup.tar.gz
```

## Um pouco sobre Shell Script e Permissões

### Shell Script

Shell scripts são arquivos que contêm uma série de comandos do shell. Eles são usados para automatizar tarefas.

### Exemplo de Shell Script

```sh
#!/bin/bash
echo "Hello, World!"
```

Para executar o script:

```sh
chmod +x script.sh
./script.sh
```

### Permissões

Permissões de arquivos determinam quem pode ler, escrever ou executar um arquivo.

- `chmod [permissões] [arquivo]`: Altera as permissões de um arquivo.
- `chown [dono]:[grupo] [arquivo]`: Altera o dono e o grupo de um arquivo.

## Procurando Arquivos e Diretórios

### Comando find

O comando `find` é usado para localizar arquivos e diretórios no sistema.

### Exemplos

```sh
find /caminho/ -name "arquivo.txt"
find /caminho/ -type d -name "diretorio"
```

## Exercícios de fixação II

### Questão 1

**Pergunta:** Qual é a função principal do comando `find` no Linux?

**Resposta:** Localizar arquivos e diretórios no sistema.

**Explicação:** O comando `find` é amplamente utilizado para buscar arquivos e diretórios em um sistema de arquivos com base em vários critérios, como nome, tipo, permissões, etc. É uma ferramenta poderosa para localizar itens específicos no sistema.

### Questão 2

**Pergunta:** Qual opção do comando `find` é usada para buscar arquivos pelo seu nome?

**Resposta:** `-name`

**Explicação:** A opção `-name` no comando `find` é usada para especificar o nome do arquivo que você deseja procurar.

Este guia é parte do curso de DevOps do Santander Coders 2024 em parceria com a Ada Tech. Para mais informações, consulte a documentação oficial e os recursos de aprendizado disponíveis.

**Autor:** [AdrielleJcds](https://github.com/Adjcds)  
**E-mail:** adrielle.dev@gmail.com  
**Última Atualização:** [14/06/2024]