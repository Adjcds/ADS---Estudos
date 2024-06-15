# Conteinerização com Docker

Bem-vindo(a) ao guia de introdução à **Conteinerização com Docker**. Este repositório contém explicações sobre os principais conceitos e exercícios de fixação para ajudá-lo a entender e aplicar os fundamentos da conteinerização usando Docker.

## Sumário

1. [Apresentação de containers e instalação do Docker](#apresentação-de-containers-e-instalação-do-docker)
2. [Comandos do Docker](#comandos-do-docker)
3. [Imagens no Docker, Criando containers através de imagens, Volumes](#imagens-no-docker-criando-containers-através-de-imagens-volumes)
4. [Redes](#redes)
5. [Ecossistema de containers](#ecossistema-de-containers)
6. [Docker Compose: o que é?](#docker-compose-o-que-é)
7. [Docker Compose na prática, Conclusão, benefícios e orquestradores](#docker-compose-na-prática-conclusão-benefícios-e-orquestradores)

---

## Apresentação de containers e instalação do Docker

### Descrição

Os containers são unidades padronizadas de software que empacotam código e suas dependências, permitindo que aplicações rodem de forma rápida e confiável em diferentes ambientes de computação. Docker é uma plataforma que facilita a criação, a implementação e a execução de containers.

### Links para Estudo

- [Solomon Hykes | Creator of Docker | In 2013 Explained - Why we built Docker](https://www.youtube.com/watch?v=3Kn6_b-1mK4)
- [Install Docker Engine](https://docs.docker.com/engine/install/)

### Exercícios de Fixação I

**Questão 1: O que é um container?**  
Resposta: Um container é uma unidade padronizada de software que empacota código e todas as suas dependências para que uma aplicação rode de forma consistente em diferentes ambientes.

**Explicação:** Containers isolam a aplicação e suas dependências do ambiente subjacente, garantindo que o software funcione da mesma maneira, independentemente de onde ele é executado.

**Questão 2: Como instalar o Docker em seu sistema operacional?**  
Resposta: A instalação do Docker pode ser realizada seguindo as instruções específicas para cada sistema operacional disponíveis na documentação oficial do Docker.

**Explicação:** A documentação do Docker fornece guias detalhados e comandos necessários para instalar o Docker no Windows, macOS e várias distribuições Linux.

## Comandos do Docker

### Descrição

Docker possui uma série de comandos para gerenciar containers, imagens, volumes e redes. Esses comandos permitem a criação, execução, parada, remoção e inspeção de containers e imagens.

### Links para Estudo

- [What can we help you find?](https://docs.docker.com)

### Exercícios de Fixação II

**Questão 1: Qual é o comando para listar todos os containers em execução?**  
Resposta: `docker ps`

**Explicação:** O comando `docker ps` exibe todos os containers atualmente em execução no sistema.

**Questão 2: Como remover uma imagem Docker?**  
Resposta: `docker rmi <imagem_id>`

**Explicação:** O comando `docker rmi` remove uma imagem específica identificada pelo seu ID ou nome.

## Imagens no Docker, Criando containers através de imagens, Volumes

### Descrição

As imagens Docker são templates imutáveis usados para criar containers. Volumes são utilizados para persistir dados gerados e utilizados pelos containers.

### Links para Estudo

- [Volumes](https://docs.docker.com/storage/volumes/)

### Exercícios de Fixação III

**Questão 1: O que é uma imagem Docker?**  
Resposta: Uma imagem Docker é um template imutável que contém todos os elementos necessários para rodar um container, incluindo código, runtime, bibliotecas e configurações.

**Explicação:** Imagens são usadas para criar containers, que são instâncias em execução dessas imagens.

**Questão 2: Para que servem os volumes no Docker?**  
Resposta: Volumes são usados para persistir dados gerados e utilizados por containers, permitindo que esses dados sejam preservados mesmo se o container for removido.

**Explicação:** Volumes facilitam o gerenciamento de dados persistentes, separando o ciclo de vida dos dados do ciclo de vida dos containers.

## Redes

### Descrição

Docker oferece várias opções de networking para conectar containers entre si e com o mundo exterior, incluindo redes bridge, host e overlay.

### Links para Estudo

- [Networking overview](https://docs.docker.com/network/)
- [Bridge network driver](https://docs.docker.com/network/drivers/bridge/)

### Exercícios de Fixação IV

**Questão 1: O que é uma rede bridge no Docker?**  
Resposta: Uma rede bridge é a rede padrão criada pelo Docker, onde os containers são conectados e podem se comunicar entre si.

**Explicação:** A rede bridge permite a comunicação interna entre containers na mesma máquina host.

**Questão 2: Como criar uma nova rede bridge no Docker?**  
Resposta: `docker network create --driver bridge minha_rede`

**Explicação:** O comando `docker network create` com o parâmetro `--driver bridge` cria uma nova rede bridge com o nome especificado.

## Ecossistema de containers

### Descrição

O ecossistema de containers inclui diversas ferramentas e serviços que facilitam a implementação e o gerenciamento de aplicações containerizadas, como Docker Compose, Kubernetes e outras.

### Links para Estudo

- [How to install WordPress with Docker](https://upcloud.com/resources/tutorials/wordpress-with-docker)

### Exercícios de Fixação V

**Questão 1: Quais são alguns componentes do ecossistema de containers?**  
Resposta: Docker Compose, Kubernetes, Docker Swarm, Helm.

**Explicação:** Esses componentes e ferramentas ajudam a gerenciar, orquestrar e escalar aplicações containerizadas.

**Questão 2: Como o Docker Compose ajuda no gerenciamento de containers?**  
Resposta: Docker Compose permite definir e gerenciar multi-containers applications com arquivos YAML, facilitando a configuração e a orquestração.

**Explicação:** O Docker Compose simplifica o gerenciamento de aplicações compostas por múltiplos containers, fornecendo uma maneira fácil de definir, configurar e executar essas aplicações.

## Docker Compose: o que é?

### Descrição

Docker Compose é uma ferramenta para definir e executar aplicações multi-containers. Com Docker Compose, você pode usar um arquivo YAML para configurar os serviços da aplicação.

### Links para Estudo

- [Overview of installing Docker Compose](https://docs.docker.com/compose/install/)
- [Try Docker Compose](https://docs.docker.com/compose/gettingstarted/)

### Exercícios de Fixação VI

**Questão 1: O que é Docker Compose?**  
Resposta: Docker Compose é uma ferramenta para definir e executar aplicações multi-containers com arquivos YAML.

**Explicação:** Docker Compose permite que desenvolvedores configurem serviços, redes e volumes em um único arquivo e depois iniciem e gerenciem a aplicação inteira com comandos simples.

**Questão 2: Como instalar o Docker Compose?**  
Resposta: Seguindo as instruções de instalação disponíveis na documentação oficial do Docker Compose.

**Explicação:** A documentação do Docker Compose fornece passos detalhados para instalar a ferramenta em diferentes sistemas operacionais.

## Docker Compose na prática, Conclusão, benefícios e orquestradores

### Descrição

Docker Compose facilita a criação e o gerenciamento de aplicações containerizadas complexas. Benefícios incluem a simplificação do desenvolvimento e da produção, além de facilitar a orquestração de containers com ferramentas como Kubernetes.

### Links para Estudo

- [Introdução ao Docker — Criando um servidor web com Node.js e subindo para o container](https://blog.rocketseat.com.br/introducao-ao-docker-criando-um-servidor-web-com-node-js-e-subindo-para-o-container/)
- [Kubernetes Blog](https://kubernetes.io/blog/)

### Exercícios de Fixação VII

**Questão 1: Quais são os benefícios do uso de Docker Compose?**  
Resposta: Simplificação do gerenciamento de aplicações multi-containers, configuração reutilizável, facilidade de teste e desenvolvimento.

**Explicação:** Docker Compose permite definir todos os serviços, redes e volumes necessários em um único arquivo YAML, simplificando o processo de configuração e implantação.

**Questão 2: O que é Kubernetes?**  
Resposta: Kubernetes é uma plataforma de orquestração de containers que automatiza a implantação, o dimensionamento e a operação de aplicações containerizadas.

**Explicação:** Kubernetes oferece uma infraestrutura robusta para gerenciar containers em grande escala, garantindo alta disponibilidade, escalabilidade e recuperação de falhas.

---

Este guia é parte do curso de DevOps do Santander Coders 2024 em parceria com a Ada Tech. Para mais informações, consulte a documentação oficial e os recursos de aprendizado disponíveis.

**Autor:** [AdrielleJcds](https://github.com/Adjcds)  
**E-mail:** adrielle.dev@gmail.com  
**Última Atualização:** [14/06/2024]