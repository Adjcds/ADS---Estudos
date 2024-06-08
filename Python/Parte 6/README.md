# 01 - Ambiente Virtual

Este é um projeto básico configurado com o Poetry para demonstrar o uso de ambientes virtuais e gerenciamento de dependências em projetos Python.

## Principais Funcionalidades

- Configuração de um ambiente virtual isolado para o projeto.
- Gerenciamento de dependências utilizando o Poetry.
- Facilidade na instalação e atualização de pacotes Python.
- Consistência no ambiente de desenvolvimento entre diferentes máquinas.

## Como Usar

### Pré-requisitos

Certifique-se de ter o Python e o Poetry instalados na sua máquina.

### Instalação

1. Clone ou faça o download deste repositório.
2. Navegue até o diretório do projeto.
3. Execute o comando `poetry install` para instalar as dependências.

### Para o Que Usar

Este projeto serve como um template básico para iniciar novos projetos Python. Ele já está configurado com um ambiente virtual isolado e o gerenciador de dependências Poetry, permitindo um desenvolvimento mais organizado e consistente.

## Como Executar na Sua Máquina

### No Terminal

1. Após a instalação das dependências, você pode executar o projeto diretamente no terminal com o comando `poetry run python <arquivo.py>`.

 #### Vamos detalhar essa parte:

1. **Poetry**: Poetry é uma ferramenta para gerenciamento de dependências e ambientes virtuais em projetos Python. Ele simplifica o processo de instalação e atualização de pacotes, garantindo consistência no ambiente de desenvolvimento.

2. **run**: O comando `run` é usado para executar comandos dentro do ambiente virtual configurado pelo Poetry. Isso garante que as dependências necessárias para o projeto estejam disponíveis durante a execução.

3. **python**: É o interpretador Python que será usado para executar o código. O `python` indica que estamos executando um script Python.

4. **<arquivo.py>**: Aqui você deve substituir `<arquivo.py>` pelo nome do arquivo Python que deseja executar. Por exemplo, se o seu arquivo se chama `main.py`, o comando completo seria `poetry run python main.py`.

Em resumo, `poetry run python <arquivo.py>` é um comando que executa um arquivo Python dentro do ambiente virtual gerenciado pelo Poetry, garantindo que todas as dependências necessárias estejam disponíveis durante a execução do código.

### No VSCode

1. Abra o projeto no VSCode.
2. Certifique-se de ter a extensão Poetry instalada.
3. O VSCode deve reconhecer automaticamente o ambiente virtual configurado pelo Poetry.
4. Você pode executar o código pressionando `Ctrl + Alt + N` ou clicando no botão de play na parte superior direita do arquivo Python.

Com esses passos simples, você estará pronto para começar a desenvolver seu projeto Python de forma organizada e eficiente!