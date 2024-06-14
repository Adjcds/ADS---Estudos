# Guia sobre Git e Versionamento

## Sumário
1. [O que é Git?](#o-que-é-git)
2. [Instalando e configurando o Git](#instalando-e-configurando-o-git)
3. [Repositórios do Git](#repositórios-do-git)
4. [Gravando mudanças no repositório](#gravando-mudanças-no-repositório)
5. [Git diff e commit](#git-diff-e-commit)
6. [Git log e restore](#git-log-e-restore)
7. [Repositórios remotos](#repositórios-remotos)
8. [GitHub](#github)
9. [Git branch e Merging branches](#git-branch-e-merging-branches)

## O que é Git?

Git é um sistema de controle de versão distribuído amplamente utilizado para rastrear mudanças no código-fonte durante o desenvolvimento de software. Ele permite que vários desenvolvedores trabalhem simultaneamente em um projeto, mantendo um histórico completo das alterações e facilitando a colaboração.

## Instalando e configurando o Git

### Instalando o Git

Para instalar o Git, siga as instruções de acordo com seu sistema operacional:

#### Windows
1. Baixe o instalador do Git em [git-scm.com](https://git-scm.com/download/win).
2. Execute o instalador e siga as instruções na tela.

#### macOS
```sh
brew install git
```

#### Linux (Debian/Ubuntu)
```sh
sudo apt-get update
sudo apt-get install git
```

### Configurando o Git

Após a instalação, configure seu nome de usuário e email:

```sh
git config --global user.name "Seu Nome"
git config --global user.email "seu.email@exemplo.com"
```

Verifique suas configurações:

```sh
git config --list
```

## Repositórios do Git

Um repositório Git é um diretório que contém todo o histórico de mudanças de um projeto. Para criar um novo repositório, use o comando `git init`:

```sh
mkdir meu-projeto
cd meu-projeto
git init
```

## Gravando mudanças no repositório

Para começar a rastrear arquivos no repositório, primeiro adicione-os ao índice (staging area) e depois grave as mudanças com um commit.

### Adicionando arquivos
```sh
git add arquivo.txt
```

Para adicionar todos os arquivos:
```sh
git add .
```

### Gravando um commit
```sh
git commit -m "Mensagem descrevendo a mudança"
```

## Git diff e commit

### Git diff
O comando `git diff` mostra as diferenças entre arquivos no índice e no repositório:

```sh
git diff
```

Para ver diferenças entre o índice e a última versão commitada:
```sh
git diff --staged
```

### Git commit
O comando `git commit` é usado para gravar mudanças no repositório. Cada commit deve ter uma mensagem que descreva a mudança:

```sh
git commit -m "Descrição das mudanças"
```

## Git log e restore

### Git log
O comando `git log` exibe o histórico de commits:

```sh
git log
```

Para um log mais compacto:
```sh
git log --oneline
```

### Git restore
O comando `git restore` é usado para restaurar arquivos:

Para descartar mudanças em um arquivo:
```sh
git restore arquivo.txt
```

Para restaurar um arquivo do índice:
```sh
git restore --staged arquivo.txt
```

## Repositórios remotos

Repositórios remotos são versões do seu projeto hospedadas na internet ou em outra rede. Para adicionar um repositório remoto, use o comando `git remote add`:

```sh
git remote add origin https://github.com/seu-usuario/seu-repositorio.git
```

Para enviar mudanças ao repositório remoto:
```sh
git push origin main
```

Para obter mudanças do repositório remoto:
```sh
git pull origin main
```

## GitHub

GitHub é uma plataforma de hospedagem de código-fonte com controle de versão usando Git. Ele oferece recursos como gerenciamento de repositórios, colaboração, issues e pull requests.

### Criando um repositório no GitHub

1. Acesse [github.com](https://github.com) e faça login.
2. Clique em "New repository".
3. Preencha o nome do repositório e outras configurações.
4. Clique em "Create repository".

### Clonando um repositório GitHub

Para clonar um repositório, use o comando `git clone`:

```sh
git clone https://github.com/seu-usuario/seu-repositorio.git
```

## Git branch e Merging branches

### Git branch
Ramos (branches) permitem que você trabalhe em diferentes funcionalidades de forma isolada. Para criar e mudar para um novo branch:

```sh
git checkout -b nova-funcionalidade
```

Para listar todos os branches:
```sh
git branch
```

Para mudar para um branch existente:
```sh
git checkout nome-do-branch
```

### Merging branches
Para mesclar (merge) um branch no branch atual, use o comando `git merge`:

```sh
git checkout main
git merge nova-funcionalidade
```

Para resolver conflitos de merge, edite os arquivos conflitantes e depois finalize o merge:

```sh
git add arquivos-resolvidos
git commit -m "Resolvidos conflitos de merge"
```

---

Este guia é parte do curso de DevOps do Santander Coders 2024 em parceria com a Ada Tech. Para mais informações, consulte a documentação oficial do Git em [git-scm.com/doc](https://git-scm.com/doc) e a documentação do GitHub em [docs.github.com](https://docs.github.com).


**Autor:** [AdrielleJcds](https://github.com/Adjcds)  
**E-mail:** adrielle.dev@gmail.com  
**Última Atualização:** [14/06/2024]
