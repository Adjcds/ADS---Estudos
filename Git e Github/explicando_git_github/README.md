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

## uso do comando `git branch`:

1. **Listar Branches**:
   ```bash
   git branch
   ```
   Isso lista todos os branches presentes no repositório local. O branch atual é marcado com um asterisco (`*`).

2. **Criar Branches**:
   ```bash
   git branch feature/nova-feature
   ```
   Isso cria um novo branch chamado `feature/nova-feature` com base no commit atual. Porém, você não muda para esse novo branch automaticamente.

3. **Deletar Branches**:
   ```bash
   git branch -d feature/nova-feature
   ```
   Isso exclui o branch `feature/nova-feature`. O argumento `-d` é usado para indicar que você está excluindo um branch já mesclado. Se você quiser excluir um branch não mesclado, deve usar `-D`.

4. **Mudar de Branch**:
   ```bash
   git checkout feature/nova-feature
   ```
   Isso muda para o branch `feature/nova-feature`. Agora você está trabalhando nesse branch e pode fazer commits nele.

5. **Visualizar Branches Remotos**:
   ```bash
   git branch -r
   ```
   Isso lista todos os branches remotos. Você pode ver os branches remotos que foram baixados do servidor remoto.

6. **Renomear Branches**:
   Não há um comando direto para renomear um branch, mas você pode fazer isso criando um novo branch com o nome desejado e excluindo o antigo:
   ```bash
   git branch -m nome-antigo nome-novo
   ```
   Este comando renomeia o branch `nome-antigo` para `nome-novo`.

Lembre-se de que o comando `git branch` é usado principalmente para manipular a estrutura de branches localmente. As operações relacionadas a branches remotos geralmente envolvem o uso de outros comandos, como `git fetch`, `git push`, entre outros.

# O merging (mesclagem) de branches 

- é um processo no Git pelo qual você combina as alterações feitas em diferentes branches em um único branch. Isso é  - comumente usado para incorporar o trabalho de um branch de feature de volta ao branch principal, como o `main` ou `master`.

Aqui está um passo a passo básico de como o merging funciona:

1. **Escolher o Branch de Destino**: Primeiro, você precisa decidir qual branch será o destino da mesclagem. Isso geralmente é o branch para o qual você deseja adicionar as alterações. Por exemplo, você pode querer mesclar um branch de feature de volta para o branch `main`.

2. **Mudar para o Branch de Destino**: Antes de fazer a mesclagem, você precisa mudar para o branch de destino usando o comando `git checkout`.

3. **Executar o Comando de Merge**: Depois de mudar para o branch de destino, você pode mesclar outro branch usando o comando `git merge`. Por exemplo, se você estiver no branch `main` e quiser mesclar um branch de feature chamado `feature/nova-feature`, você executaria:
   ```bash
   git merge feature/nova-feature
   ```

4. **Resolução de Conflitos**: Em alguns casos, pode haver conflitos durante o processo de mesclagem, especialmente se as mesmas partes do código forem alteradas em ambos os branches. Nesse caso, você precisará resolver os conflitos manualmente, editando os arquivos afetados para escolher as alterações corretas.

5. **Concluir o Merge**: Depois de resolver quaisquer conflitos, você pode concluir o merge e confirmar as alterações usando `git commit`.

6. **Push das Alterações (Opcional)**: Se você mesclou um branch e está satisfeito com o resultado, pode enviar as alterações para o repositório remoto usando `git push`, se necessário.

O merging de branches é uma parte essencial do fluxo de trabalho do Git, pois permite a colaboração eficaz em projetos com múltiplos colaboradores e várias linhas de desenvolvimento simultâneas. Ele ajuda a garantir que as alterações sejam integradas de forma suave e organizada no código principal do projeto.