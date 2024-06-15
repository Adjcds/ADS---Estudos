# Introdução à Infraestrutura Web

Bem-vindo(a) ao guia de introdução à **Infraestrutura Web**. Este repositório contém explicações sobre os principais conceitos e exercícios de fixação para ajudá-lo a entender e aplicar os fundamentos da infraestrutura web.

## Sumário

1. [Introdução à Infraestrutura Web](#introdução-à-infraestrutura-web)
2. [Sistemas Operacionais para Servidores Web](#sistemas-operacionais-para-servidores-web)
3. [Web Servers](#web-servers)
4. [Bancos de Dados para Infraestrutura Web](#bancos-de-dados-para-infraestrutura-web)
5. [Linguagens de Programação para Web - Parte I](#linguagens-de-programação-para-web---parte-i)
6. [Linguagens de Programação para Web - Parte II](#linguagens-de-programação-para-web---parte-ii)
7. [Protocolo HTTP](#protocolo-http)

---

## Introdução à Infraestrutura Web

### O que é Infraestrutura Web?

Infraestrutura web refere-se ao conjunto de componentes tecnológicos necessários para a hospedagem, operação e manutenção de aplicativos e serviços web. Pode incluir servidores físicos ou virtuais, sistemas operacionais, servidores web, bancos de dados, redes, entre outros.

### Exercícios de Fixação I

**Questão 1: O conjunto de elementos que integra a infraestrutura web pode ser físico ou virtual. Qual das seguintes afirmações pode ser considerada como vantagem do uso de infraestrutura física?**  
Resposta: Maior performance, pois não há compartilhamento de recursos.

**Explicação:** Infraestruturas físicas dedicadas oferecem maior desempenho porque os recursos não são compartilhados com outras máquinas ou usuários, o que pode ser crítico para aplicações que demandam alta performance.

**Questão 2: Qual a importância da confiabilidade da infraestrutura web?**  
Resposta: Estar disponível a maior parte do tempo para que os usuários possam acessar seu conteúdo e serviços.

**Explicação:** A confiabilidade da infraestrutura web é crucial para garantir que os serviços estejam disponíveis continuamente, proporcionando uma boa experiência ao usuário e minimizando interrupções.

## Sistemas Operacionais para Servidores Web

### O que são Sistemas Operacionais para Servidores Web?

Sistemas operacionais para servidores web são projetados para gerenciar hardware e software em servidores, otimizando o desempenho e a segurança para hospedar sites, aplicações e serviços web.

### Exercícios de Fixação II

**Questão 1: Qual das seguintes afirmações é verdadeira sobre sistemas operacionais para servidores web?**  
Resposta: Eles são projetados especificamente para rodar em servidores web.

**Explicação:** Sistemas operacionais para servidores web são otimizados para fornecer desempenho, segurança e estabilidade necessários para suportar o tráfego e as operações contínuas de serviços web.

**Questão 2: Qual das seguintes opções abaixo é um sistema operacional gratuito e de código aberto (opensource)?**  
Resposta: Ubuntu Linux.

**Explicação:** Ubuntu Linux é um sistema operacional popular e gratuito, amplamente utilizado para servidores web devido à sua robustez, segurança e comunidade ativa de suporte.

## Web Servers

### O que são Web Servers?

Web servers são softwares responsáveis por aceitar solicitações HTTP de clientes (como navegadores) e servir conteúdo web, como páginas HTML, imagens, vídeos, e outros tipos de dados.

### Exercícios de Fixação III

**Questão 1: Qual é o protocolo responsável pela comunicação entre o Web Server e o cliente (browser, por exemplo)?**  
Resposta: HTTP.

**Explicação:** HTTP (Hypertext Transfer Protocol) é o protocolo padrão para a troca de informações entre web servers e clientes, permitindo a navegação e a transferência de dados na web.

**Questão 2: Qual das características abaixo NÃO se aplica ao Web Server NGINX?**  
Resposta: Funciona apenas no sistema operacional Windows.

**Explicação:** NGINX é um servidor web multiplataforma que funciona em vários sistemas operacionais, incluindo Linux, Windows e BSD, e é conhecido por sua alta performance e eficiência.

## Bancos de Dados para Infraestrutura Web

### O que são Bancos de Dados?

Bancos de dados são sistemas que armazenam e gerenciam dados de forma organizada, permitindo a consulta, inserção, atualização e exclusão de informações de maneira eficiente.

### Exercícios de Fixação IV

**Questão 1: Qual opção a seguir melhor define o que é um banco de dados?**  
Resposta: É um conjunto de dados organizados e estruturados armazenados e gerenciados por um sistema computacional.

**Explicação:** Bancos de dados estruturam dados de maneira que permite fácil acesso, gerenciamento e atualização, essenciais para aplicações web que dependem de informações dinâmicas.

**Questão 2: Qual opção abaixo melhor descreve um banco de dados relacional?**  
Resposta: É composto por tabelas organizadas em linhas e colunas, e é possível estabelecer relações entre elas.

**Explicação:** Bancos de dados relacionais utilizam um modelo de tabelas onde dados podem ser relacionados entre si, facilitando consultas complexas e integridade dos dados.

## Linguagens de Programação para Web - Parte I

### O que é HTML e CSS?

HTML (Hypertext Markup Language) é a linguagem padrão para criar e estruturar conteúdo na web. CSS (Cascading Style Sheets) é a linguagem usada para definir a apresentação visual do conteúdo HTML.

### Exercícios de Fixação V

**Questão 1: Por que o HTML não é considerado uma linguagem de programação?**  
Resposta: Porque ele não é capaz de passar instruções para o computador sobre como manipular os dados, apenas como formatá-los e diagramá-los.

**Explicação:** HTML é uma linguagem de marcação que estrutura conteúdo, mas não possui lógica de programação, como loops ou condicionais, que são características de linguagens de programação.

**Questão 2: Qual a principal função do CSS?**  
Resposta: Definir a aparência visual de páginas web, incluindo cores, fontes, espaçamento, layout e outros aspectos visuais como responsividade.

**Explicação:** CSS estiliza o conteúdo HTML, permitindo separar a estrutura (HTML) da apresentação visual (CSS) para facilitar a manutenção e design consistente.

## Linguagens de Programação para Web - Parte II

### O que são Linguagens de Programação Server-Side?

Linguagens de programação server-side são utilizadas para criar lógica de back-end, processando dados no servidor antes de enviar o resultado para o cliente.

### Exercícios de Fixação VI

**Questão 1: Qual a principal característica de uma linguagem de programação server-side rendering?**  
Resposta: Todo o processamento é feito do lado do servidor e apenas o resultado desse processamento é enviado ao cliente/browser.

**Explicação:** Em server-side rendering, o servidor gera o HTML completo antes de enviá-lo ao cliente, o que pode melhorar a performance percebida e a SEO (Search Engine Optimization).

**Questão 2: Qual das ações abaixo tanto o HTML quanto o CSS não são capazes de executar, porém o JavaScript é?**  
Resposta: Qualquer ação dinâmica sem a necessidade de recarregar a página.

**Explicação:** JavaScript permite criar interações dinâmicas e reativas em páginas web sem recarregar a página, ao contrário de HTML e CSS, que são estáticos.

## Protocolo HTTP

### O que é o Protocolo HTTP?

HTTP (Hypertext Transfer Protocol) é o protocolo de comunicação que permite a transferência de informações na web, estruturando como os pedidos e respostas são formatados e transmitidos.

### Exercícios de Fixação VII

**Questão 1: Quais são as duas unidades de comunicação do protocolo HTTP?**  
Resposta: Requisição e Resposta.

**Explicação:** No HTTP, o cliente faz uma requisição ao servidor, que processa o pedido e envia uma resposta, estabelecendo a comunicação básica para a transferência de dados na web.

**Questão 2: Qual afirmação abaixo NÃO é verdadeira a respeito do protocolo HTTP?**  
Resposta: Todas as requisições são criptografadas por padrão.

**Explicação:** HTTP por si só não criptografa as requisições; para criptografia, é utilizado HTTPS (HTTP Secure), que incorpora SSL/TLS para garantir a segurança na transmissão dos dados.

Este guia é parte do curso de DevOps do Santander Coders 2024 em parceria com a Ada Tech. Para mais informações, consulte a documentação oficial e os recursos de aprendizado disponíveis.

**Autor:** [AdrielleJcds](https://github.com/Adjcds)  
**E-mail:** adrielle.dev@gmail.com  
**Última Atualização:** [14/06/2024]