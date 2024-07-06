# Introdução a Banco de Dados NoSQL

Este README oferece uma introdução abrangente aos conceitos básicos, modelagem de dados, operações e recursos complementares relacionados a bancos de dados NoSQL, com foco em MongoDB e Redis.

## Conceitos Básicos dos Bancos de Dados Não Relacionais

Bancos de dados NoSQL são sistemas de gerenciamento de banco de dados que não seguem o modelo relacional tradicional. Eles são projetados para lidar com grandes volumes de dados não estruturados ou semiestruturados, oferecendo flexibilidade e escalabilidade.

### Características dos Bancos de Dados NoSQL:

- **Escalabilidade Horizontal:** Facilidade em distribuir dados e aumentar a capacidade de armazenamento e processamento.
- **Modelagem Flexível:** Suporte a estruturas de dados variadas (documentos, chave-valor, colunas, grafos).
- **Alta Performance:** Otimizado para operações rápidas de leitura e escrita.

## Visão Geral dos Tipos de NoSQL

Existem diferentes tipos de bancos de dados NoSQL, cada um otimizado para casos de uso específicos:

- **Documentos:** Armazenam dados em documentos semiestruturados, como JSON ou BSON. Exemplos: MongoDB, CouchDB.
- **Chave-Valor:** Armazenam pares de chave-valor simples. Exemplos: Redis, Riak.
- **Coluna Família:** Armazenam dados em colunas ao invés de linhas. Ideal para grandes volumes de dados. Exemplos: Cassandra, HBase.
- **Grafos:** Armazenam dados como grafos, com nós e arestas, úteis para redes complexas de relacionamentos. Exemplos: Neo4j, OrientDB.

## Introdução ao MongoDB

MongoDB é um banco de dados NoSQL baseado em documentos. Cada registro é um documento, que pode conter dados complexos e variados.

### Instalação e Configuração do MongoDB Atlas

MongoDB Atlas é um serviço de banco de dados na nuvem oferecido pela MongoDB. Para configurar:

1. **Crie uma conta no MongoDB Atlas.**
2. **Crie um novo cluster.**
3. **Configure o acesso ao cluster, adicionando seu IP e criando um usuário de banco de dados.**
4. **Conecte-se ao cluster usando o MongoDB Compass ou o driver MongoDB em sua aplicação.**

### Modelagem de Dados Usando Documentos

A modelagem no MongoDB é feita usando documentos BSON (JSON-like). Os documentos são estruturados de maneira hierárquica e podem conter arrays e subdocumentos.

**Exemplo:**
```javascript
{
  "nome": "João Silva",
  "idade": 30,
  "endereços": [
    {
      "tipo": "casa",
      "endereço": "Rua A, 123"
    },
    {
      "tipo": "trabalho",
      "endereço": "Av. B, 456"
    }
  ]
}
```

### Estratégias de Modelagem de Dados Eficientes e Escaláveis

- **Embedding:** Incorporar documentos aninhados para relações um-para-um e um-para-muitos.
- **Referencing:** Usar referências entre documentos para relações muitos-para-muitos.
- **Indexação:** Criar índices para melhorar o desempenho de consultas.

**Exemplo de Embedding:**
```javascript
{
  "nome": "Loja A",
  "produtos": [
    {
      "nome": "Produto 1",
      "preco": 100
    },
    {
      "nome": "Produto 2",
      "preco": 200
    }
  ]
}
```

**Exemplo de Referencing:**
```javascript
// Documento Cliente
{
  "nome": "Cliente A",
  "pedido_id": ObjectId("60c72b2f9b1e8b6f0fda3f22")
}

// Documento Pedido
{
  "_id": ObjectId("60c72b2f9b1e8b6f0fda3f22"),
  "data": "2023-07-06",
  "itens": [
    {"produto": "Produto 1", "quantidade": 2}
  ]
}
```

## Operações no MongoDB

### Consultas Simples

**Exemplo de consulta simples no MongoDB:**
```javascript
db.produtos.find({ tipo: "eletrônicos" });
```

### Inserção de Dados

**Exemplo de inserção de dados no MongoDB:**
```javascript
db.clientes.insertOne({
  nome: "Maria",
  idade: 28,
  endereços: [
    { tipo: "casa", endereço: "Rua C, 789" }
  ]
});
```

### Atualização de Dados

**Exemplo de atualização de dados no MongoDB:**
```javascript
db.clientes.updateOne(
  { nome: "Maria" },
  { $set: { idade: 29 } }
);
```

### Exclusão de Dados

**Exemplo de exclusão de dados no MongoDB:**
```javascript
db.clientes.deleteOne({ nome: "Maria" });
```

## Introdução ao Redis

Redis é um banco de dados NoSQL do tipo chave-valor conhecido por sua velocidade e flexibilidade. É usado principalmente para caching, filas de mensagens e gerenciamento de sessões.

### Características do Redis:

- **Alto Desempenho:** Extremamente rápido para operações de leitura e escrita.
- **Estruturas de Dados Avançadas:** Suporta strings, hashes, listas, sets, sorted sets, bitmaps, hyperloglogs e geospacial indexes.
- **Persistência Opcional:** Possibilidade de persistir dados em disco.

**Exemplo de uso do Redis:**
```python
import redis

# Conexão com o Redis
r = redis.Redis(host='localhost', port=6379, db=0)

# Setar um valor
r.set('nome', 'João')

# Obter um valor
nome = r.get('nome')
print(nome)  # Saída: b'João'
```

## Exercícios

### Quais são as principais características do MongoDB?

- **Alta escalabilidade e desempenho**: MongoDB é conhecido por sua capacidade de escalabilidade horizontal e alto desempenho em operações de leitura e escrita.

### Quais são as principais características dos bancos de dados não relacionais?

- **Esquema flexível**: Bancos de dados NoSQL permitem esquemas flexíveis, adaptando-se facilmente a mudanças nos requisitos de dados sem a necessidade de alterações estruturais complexas.
- **Alta capacidade de armazenamento**: São capazes de lidar com grandes volumes de dados distribuídos em diferentes servidores, proporcionando alta escalabilidade e desempenho.

### O que é o MongoDB?

- **Um banco de dados não relacional**: MongoDB é um banco de dados NoSQL, conhecido por sua flexibilidade na modelagem de dados e escalabilidade horizontal.

### Qual é a principal característica do Redis em relação ao armazenamento de dados?

- **Rápido acesso em memória**: Redis é extremamente rápido para operações de leitura e escrita, pois armazena dados principalmente em memória.

### Qual é a finalidade do banco de dados não relacional do tipo chave-valor?

- **Armazenar dados com base em uma chave única**: Bancos de dados chave-valor armazenam dados como pares chave-valor, facilitando o acesso rápido aos dados com base em chaves únicas.

### Como o MongoDB organiza os dados?

- **Em documentos JSON**: MongoDB organiza dados em documentos JSON (ou BSON), permitindo uma estrutura flexível e aninhada para armazenar informações complexas.

### O que é um banco de dados orientado a documentos?

- **Armazena dados em formato de documento JSON**: Bancos de dados orientados a documentos, como o MongoDB, armazenam dados em documentos JSON, permitindo uma estrutura flexível e hierárquica.

### Qual operação é usada no MongoDB para atualizar vários documentos que correspondem a certos critérios?

- **updateMany()**: A operação `updateMany()` é usada no MongoDB para atualizar múltiplos documentos que correspondem a certos critérios de busca.

### Qual é a finalidade da função "findOne()" no MongoDB?

- **Realizar consultas e recuperar o primeiro documento que corresponda aos critérios de busca**: A função `findOne()` no MongoDB é usada para buscar e retornar o primeiro documento que corresponde aos critérios especificados.

### Quais são os benefícios dos bancos de dados não relacionais em relação aos relacionais?

- **Flexibilidade no esquema dos dados**: Bancos de dados NoSQL permitem mudanças no esquema de dados sem a necessidade de uma reestruturação complexa, tornando-os ideais para dados dinâmicos e não estruturados.
- **Alta capacidade de armazenamento**: Bancos de dados NoSQL são projetados para lidar com grandes volumes de dados distribuídos, proporcionando alta escalabilidade e desempenho.

## Materiais Complementares

### Repositório Git

Todo código desenvolvido durante este curso foi versionado e está disponível em:

[Repositório GitHub](https://github.com/pamelaborges/dio-db-nosql)

### Slides

Baixe os slides do curso [aqui](#link).

### Dicas/Links Úteis

- **Artigos/Fórum:** Compartilhe conteúdo técnico e discuta dúvidas nos Fóruns da DIO.
- **Rooms:** Participe de discussões em tempo real com outros alunos.
- **Pesquise na Web:** Use motores de busca para encontrar mais informações e resolver dúvidas.

## Como Usar Este Repositório

1. **Instalação e Configuração:** Configure o ambiente MongoDB e Redis conforme necessário.
2.

 **Modelagem de Dados:** Experimente diferentes estratégias de modelagem usando documentos no MongoDB.
3. **Operações e Consultas:** Pratique operações CRUD e consultas avançadas no MongoDB.
4. **Explorando o Redis:** Experimente cenários de uso do Redis para caching e gerenciamento de sessões.

## Referências

- Documentação oficial do [MongoDB](https://docs.mongodb.com/)
- Documentação oficial do [Redis](https://redis.io/documentation)
- Recursos adicionais na [DIO](https://digitalinnovation.one/)

## Autoria

- **Autor:** Adrielle
- **Contato:** adrielle.dev@gmail.com
- **Data:** 06/07/2024

---

**Autoria:** Esta parte dos materiais complementares foi criada pela professora [Pamela Borges](https://github.com/pamelaborges) da DIO.