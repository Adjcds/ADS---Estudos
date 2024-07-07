# Introdução ao Desenvolvimento Web

Este repositório contém uma introdução ao desenvolvimento web, abordando conceitos fundamentais e exemplos práticos para ajudar a compreender como a web funciona e as tecnologias envolvidas no processo de desenvolvimento.

## Índice

1. [Introdução ao Desenvolvimento Web](#introdução-ao-desenvolvimento-web)
2. [Como a Web Funciona](#como-a-web-funciona)
3. [Tecnologias Front-end e Back-end](#tecnologias-front-end-e-back-end)
4. [APIs e Conceitos Fundamentais](#apis-e-conceitos-fundamentais)
5. [Tipos de APIs](#tipos-de-apis)
    - [RESTful](#restful)
    - [SOAP](#soap)
    - [GraphQL](#graphql)
6. [Verbos HTTP](#verbos-http)
    - [GET](#get)
    - [POST](#post)
    - [PATCH](#patch)
    - [PUT](#put)
    - [DELETE](#delete)

## Introdução ao Desenvolvimento Web

O desenvolvimento web é o processo de criação de sites e aplicações web. Envolve o uso de várias tecnologias e frameworks para construir e manter sites e aplicações que funcionam na internet.

## Como a Web Funciona

A web funciona através de uma arquitetura cliente-servidor. Quando você digita um endereço web no navegador, uma solicitação (request) é enviada para o servidor, que responde com os dados necessários para exibir a página (response). Esses dados geralmente incluem HTML, CSS e JavaScript.

![Web Architecture](https://example.com/web-architecture.png)

## Tecnologias Front-end e Back-end

### Front-end

O front-end refere-se à parte do desenvolvimento web que lida com a interface do usuário e a experiência do usuário. As principais tecnologias front-end incluem:

- **HTML (HyperText Markup Language)**: Estrutura a página web.
- **CSS (Cascading Style Sheets)**: Estiliza a página web.
- **JavaScript**: Adiciona interatividade à página web.

### Back-end

O back-end refere-se à parte do desenvolvimento web que lida com a lógica do servidor, banco de dados e autenticação. As principais tecnologias back-end incluem:

- **Linguagens de Programação**: Python, Java, PHP, Node.js, etc.
- **Servidores Web**: Apache, Nginx.
- **Bancos de Dados**: MySQL, PostgreSQL, MongoDB.

## APIs e Conceitos Fundamentais

APIs (Application Programming Interfaces) permitem a comunicação entre diferentes partes de um software ou entre diferentes softwares. Elas são fundamentais para a construção de aplicações modernas e escaláveis.

### Tipos de APIs

#### RESTful

REST (Representational State Transfer) é uma arquitetura de API que utiliza verbos HTTP e URLs para gerenciar recursos.

#### SOAP

SOAP (Simple Object Access Protocol) é um protocolo de comunicação baseado em XML para troca de informações estruturadas.

#### GraphQL

GraphQL é uma linguagem de consulta para APIs que permite solicitar exatamente os dados necessários, economizando largura de banda e melhorando o desempenho.

## Verbos HTTP

### GET

O verbo GET é usado para solicitar dados de um servidor. Não altera o estado do recurso no servidor.

```http
GET /api/resource
```

### POST

O verbo POST é usado para enviar dados ao servidor, geralmente para criar um novo recurso.

```http
POST /api/resource
Content-Type: application/json

{
    "name": "Novo Recurso",
    "description": "Descrição do novo recurso"
}
```

### PATCH

O verbo PATCH é usado para atualizar parcialmente um recurso no servidor.

```http
PATCH /api/resource/1
Content-Type: application/json

{
    "description": "Descrição atualizada"
}
```

### PUT

O verbo PUT é usado para atualizar completamente um recurso no servidor.

```http
PUT /api/resource/1
Content-Type: application/json

{
    "name": "Recurso Atualizado",
    "description": "Descrição atualizada"
}
```

### DELETE

O verbo DELETE é usado para excluir um recurso no servidor.

```http
DELETE /api/resource/1
```

---
