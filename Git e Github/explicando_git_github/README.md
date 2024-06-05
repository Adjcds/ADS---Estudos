# Comandos Básicos do Git

## git init
- Inicializa um novo repositório Git.
- Uso:
  ```bash
  git init
  ```
  - Cria um novo repositório Git no diretório atual.


# git pull
- Atualiza o repositório local com as mudanças do repositório remoto.
- Uso:
  ```bash
  git pull origin main
  ```
  - Busca e incorpora as mudanças do branch `main` do repositório remoto `origin` para o branch atual no repositório local.

## git push
- Envia as mudanças do repositório local para o repositório remoto.
- Uso:
  ```bash
  git push origin main
  ```
  - Envia as mudanças do branch `main` do repositório local para o branch `main` do repositório remoto `origin`.

## git log
- Exibe o histórico de commits do repositório.
- Uso:
  ```bash
  git log
  ```
  - Mostra uma lista de commits, com detalhes como autor, data e mensagem de commit.

## git restore
- Restaura arquivos no repositório local para um estado anterior.
- Remove o arquivo da área de staging:
  - Uso:
    ```bash
    git restore --staged <arquivo>
    ```
    - Remove o arquivo especificado da área de staging.

- Restaura o arquivo para o estado do último commit:
  - Uso:
    ```bash
    git restore <arquivo>
    ```
    - Restaura o arquivo especificado para o estado do último commit.

## git diff
- Mostra as diferenças entre commits, branches, arquivos, etc.
- Diferenças entre a área de trabalho e a área de staging:
  - Uso:
    ```bash
    git diff
    ```
    - Mostra as diferenças entre as mudanças na área de trabalho e as mudanças na área de staging.

- Diferenças entre dois commits:
  - Uso:
    ```bash
    git diff <commit antigo> <commit novo>
    ```
    - Mostra as diferenças entre dois commits específicos.

## git commit
- Grava as mudanças na área de staging para o repositório.
- Uso:
  ```bash
  git commit -m "Mensagem de commit"
  ```
  - Faz o commit das mudanças na área de staging com uma mensagem descritiva.

## git add
- Adiciona arquivos ou mudanças à área de staging.
- Adiciona o arquivo especificado à área de staging. Ao pressionar Tab, o VSCode ou terminal autocompleta o nome do arquivo.:
  - Uso:
    ```bash
    git add <arquivo>
    ```
    - Adiciona o arquivo especificado à área de staging.

- Adiciona todas as mudanças no diretório atual:
  - Uso:
    ```bash
    git add .
    ```
    - Adiciona todas as mudanças no diretório atual à área de staging.

## git status
- Exibe o estado atual do repositório.
- Uso:
  ```bash
  git status
  ```
  - Mostra quais arquivos foram modificados, quais estão na área de staging e quais não estão sendo rastreados.

## git branch
- Gerencia branches no repositório.
- Lista todos os branches:
  - Uso:
    ```bash
    git branch
    ```
    - Lista todos os branches no repositório.

- Cria um novo branch:
  - Uso:
    ```bash
    git branch <nome-do-branch>
    ```
    - Cria um novo branch com o nome especificado.

## git checkout
- Muda de branch ou restaura arquivos no repositório.
- Muda para o branch especificado:
  - Uso:
    ```bash
    git checkout <nome-do-branch>
    ```
    - Muda para o branch especificado.

- Restaura o arquivo para o estado do último commit:
  - Uso:
    ```bash
    git checkout -- <arquivo>
    ```
    - Restaura o arquivo especificado para o estado do último commit.

## git merge
- Mescla branches no repositório.
- Uso:
  ```bash
  git merge <branch>
  ```
  - Mescla o branch especificado com o branch atual.

## git clone
- Faz uma cópia de um repositório remoto.
- Uso:
  ```bash
  git clone <url-do-repositório>
  ```
  - Clona o repositório remoto especificado pela URL para o diretório local.