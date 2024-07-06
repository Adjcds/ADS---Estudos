## Estudos de Introdução a Banco de Dados Relacionais (SQL)

#### 1. Conceitos Básicos e Estrutura do Banco de Dados Relacional

Um Banco de Dados Relacional organiza dados em tabelas, que são compostas por linhas (registros) e colunas (campos). Cada tabela representa uma entidade e as colunas armazenam atributos dessa entidade.

**Exemplo:**
```sql
CREATE TABLE Clientes (
    ID INT PRIMARY KEY,
    Nome VARCHAR(100),
    Email VARCHAR(100)
);
```
Neste exemplo, a tabela "Clientes" possui três colunas: `ID`, `Nome`, e `Email`.

#### 2. Introdução e Conceitos Básicos de SQL

SQL (Structured Query Language) é a linguagem usada para interagir com bancos de dados relacionais. Permite realizar operações como criar tabelas, inserir dados, atualizar, deletar e consultar dados.

**Exemplo:**
```sql
SELECT Nome, Email FROM Clientes;
```
Este comando seleciona os campos `Nome` e `Email` da tabela `Clientes`.

#### 3. MER e DER: Modelagem de Bancos de Dados

MER (Modelo Entidade-Relacionamento) e DER (Diagrama Entidade-Relacionamento) são ferramentas para modelar dados de forma visual, mostrando entidades e seus relacionamentos.

**Exemplo:**
- Entidade: Cliente
- Relacionamento: Compra
- Entidade: Produto

#### 4. Configuração do Ambiente

Para começar a usar SQL, é necessário configurar um ambiente de desenvolvimento. Isso inclui a instalação de um SGBD (Sistema de Gerenciamento de Banco de Dados) como MySQL, PostgreSQL, ou SQLite.

**Exemplo:**
```bash
# Para instalar o MySQL no Ubuntu:
sudo apt-get update
sudo apt-get install mysql-server
```

#### 5. Modelagem de Dados Relacionais: Tabelas, Colunas e Registros

Modelagem de dados envolve a criação de tabelas, definição de colunas e inserção de registros.

**Exemplo:**
```sql
CREATE TABLE Produtos (
    ProdutoID INT PRIMARY KEY,
    Nome VARCHAR(100),
    Preco DECIMAL(10, 2)
);
```
Aqui, a tabela "Produtos" é criada com colunas para `ProdutoID`, `Nome`, e `Preco`.

#### 6. Operações CRUD: Insert e SELECT

CRUD é um acrônimo para Create, Read, Update e Delete, que são as operações básicas em um banco de dados.

**Exemplo:**
```sql
-- Inserir dados
INSERT INTO Clientes (ID, Nome, Email) VALUES (1, 'João Silva', 'joao@email.com');

-- Selecionar dados
SELECT * FROM Clientes;
```

#### 7. Operações CRUD: Update e Delete

Atualizar e deletar registros são operações essenciais para manter os dados corretos e atualizados.

**Exemplo:**
```sql
-- Atualizar dados
UPDATE Clientes SET Email = 'joao.novo@email.com' WHERE ID = 1;

-- Deletar dados
DELETE FROM Clientes WHERE ID = 1;
```

#### 8. Alterando e Excluindo Tabelas

Às vezes, é necessário modificar a estrutura das tabelas ou excluí-las completamente.

**Exemplo:**
```sql
-- Adicionar coluna
ALTER TABLE Clientes ADD DataDeNascimento DATE;

-- Excluir tabela
DROP TABLE Clientes;
```

#### 9. Chaves Primárias e Estrangeiras

Chaves primárias (PK) identificam unicamente cada registro em uma tabela, enquanto chaves estrangeiras (FK) estabelecem relacionamentos entre tabelas.

**Exemplo:**
```sql
CREATE TABLE Pedidos (
    PedidoID INT PRIMARY KEY,
    ClienteID INT,
    Data DATE,
    FOREIGN KEY (ClienteID) REFERENCES Clientes(ID)
);
```

#### 10. Normalização de Dados

Normalização é o processo de organizar dados para minimizar redundâncias. Existem várias formas normais, cada uma com regras específicas.

**Exemplo:**
- 1ª Forma Normal: Eliminar grupos repetitivos.
- 2ª Forma Normal: Garantir que todos os atributos dependam da chave primária.

#### 11. Consultas com Junções e Subconsultas

Junções combinam dados de múltiplas tabelas, enquanto subconsultas são consultas aninhadas dentro de outras consultas.

**Exemplo:**
```sql
-- Junção
SELECT Clientes.Nome, Pedidos.Data
FROM Clientes
JOIN Pedidos ON Clientes.ID = Pedidos.ClienteID;

-- Subconsulta
SELECT Nome FROM Clientes WHERE ID IN (SELECT ClienteID FROM Pedidos WHERE Data > '2024-01-01');
```

#### 12. Funções Agregadas e Agrupamento de Resultados

Funções agregadas realizam cálculos em um conjunto de valores e retornam um único valor. O agrupamento permite agregar resultados por um ou mais campos.

**Exemplo:**
```sql
-- Funções agregadas
SELECT COUNT(*) FROM Clientes;

-- Agrupamento
SELECT ClienteID, COUNT(*) AS NumeroDePedidos
FROM Pedidos
GROUP BY ClienteID;
```

#### 13. Índices

Índices são usados para melhorar a performance das consultas. Eles permitem acesso rápido aos dados.

**Exemplo:**
```sql
-- Criar índice
CREATE INDEX idx_cliente_nome ON Clientes(Nome);
```

### Materiais Complementares

Nossos materiais complementares e de apoio têm como objetivo apresentar informações para facilitar e enriquecer a sua jornada de aprendizado. Para isso, links úteis (como slides, repositórios e páginas oficiais) serão disponibilizados, além de dicas sobre como se destacar na DIO e no mercado de trabalho 😉

#### Repositório Git

O Git é um conceito essencial no mercado de trabalho atualmente, por isso sempre reforçamos sua importância em nossa metodologia educacional. Por isso, todo código-fonte desenvolvido durante este conteúdo foi versionado no seguinte endereço para que você possa consultá-lo a qualquer momento:

[Repositório GitHub](https://github.com/pamelaborges/dio-bd-relacional)

#### Slides
[Baixe aqui](#)

#### Dicas/Links Úteis

Por fim, disponibilizamos alguns links úteis para que você possa se desenvolver ainda mais através de referências oficiais das tecnologias, páginas de documentação e/ou fóruns de discussão relevantes. Nesse contexto, seguem algumas sugestões:

- **Artigos/Fórum**: você pode compartilhar conteúdos técnicos através de Artigos (visíveis globalmente na plataforma da DIO). Por outro lado, você também pode compartilhar suas conquistas e dúvidas usando os Fóruns (que são específicos para cada experiência educacional na DIO, como um Bootcamp por exemplo);
- **Rooms**: caso você esteja inscrito(a) em uma experiência educacional na DIO (como um Bootcamp, por exemplo) você terá acesso ao Rooms. O Rooms é uma ferramenta de bate-papo em tempo real onde todos os inscritos podem interagir, compartilhando dúvidas e dicas (que podem conter imagens e snippets de código-fonte);
- **Pesquise na Web**: pode parecer óbvio, mas é importante frisar a importância das engines de busca no dia-a-dia de um profissional de TI. Caso não encontre o que procura dentro da DIO, pesquise sobre o assunto (conceito, dúvida, erro etc) na Internet (dê um Google), pois na maioria das vezes você será levado à páginas incríveis como o StackOverflow que salvarão o seu dia 😎

### Como Usar Este Repositório

1. **Configuração do Ambiente**: Instale o SGBD de sua preferência e configure-o conforme necessário.
2. **Criação das Tabelas**: Execute os comandos SQL fornecidos para criar as tabelas e inserir dados.
3. **Operações CRUD**: Teste as operações CRUD para praticar a manipulação dos dados.
4. **Consultas e Modelagem**: Experimente as consultas, junções e modelagem de dados conforme descrito.

## Quiz: Introdução a Banco de Dados Relacionais (SQL)

### Pergunta 1:
Qual tipo de join é utilizado para combinar registros de duas tabelas apenas quando houver correspondência entre as chaves?

**a) INNER JOIN**  
b) LEFT JOIN  
c) RIGHT JOIN  
d) FULL JOIN  

**Resposta Correta:** a) INNER JOIN

**Explicação:** Um INNER JOIN retorna apenas os registros das duas tabelas que possuem correspondência entre as chaves especificadas na cláusula ON.

---

### Pergunta 2:
Qual tipo de join é utilizado para retornar todos os registros das duas tabelas, mesmo que não haja correspondência entre as chaves?

a) INNER JOIN  
b) LEFT JOIN  
c) RIGHT JOIN  
**d) FULL JOIN**  

**Resposta Correta:** d) FULL JOIN

**Explicação:** Um FULL JOIN retorna todos os registros das tabelas à esquerda e à direita da cláusula JOIN, combinando os registros onde houver correspondência e incluindo registros nulos onde não houver correspondência.

---

### Pergunta 3:
Qual é o objetivo principal da utilização de chaves primárias em uma tabela?

a) Identificar registros duplicados  
b) Criar um relacionamento entre tabelas  
c) Definir o tamanho máximo dos campos  
**d) Identificar registros exclusivos em uma tabela**  
e) Armazenar dados em cache  

**Resposta Correta:** d) Identificar registros exclusivos em uma tabela

**Explicação:** A chave primária de uma tabela é usada para garantir que cada registro na tabela seja único e possa ser identificado de forma única.

---

### Pergunta 4:
Qual tipo de join é utilizado para retornar todos os registros da tabela da esquerda e os registros correspondentes da tabela da direita, mesmo que não haja correspondência entre as chaves?

**a) LEFT JOIN**  
b) RIGHT JOIN  
c) INNER JOIN  
d) CROSS JOIN  

**Resposta Correta:** a) LEFT JOIN

**Explicação:** Um LEFT JOIN retorna todos os registros da tabela à esquerda da cláusula JOIN, junto com os registros correspondentes da tabela à direita, e registros nulos onde não há correspondência.

---

### Pergunta 5:
Quais são algumas das formas normais utilizadas na normalização de dados?

a) XYZeW  
b) Alpha, Beta, Gamma e Delta  
c) Alta, Média, Baixa e Nenhuma  
**d) 1NF, 2NF, e 3NF**  
e) SUM, AVG e COUNT  

**Resposta Correta:** d) 1NF, 2NF, e 3NF

**Explicação:** As formas normais (1NF, 2NF, 3NF, etc.) são usadas na normalização de dados para eliminar redundâncias e anomalias de atualização em um banco de dados relacional, garantindo a consistência e eficiência dos dados.

---

### Conclusão

Este README abrange os conceitos fundamentais de bancos de dados relacionais e SQL. Siga os exemplos e commits explicativos para aprender e aplicar esses conceitos de forma prática. Boa sorte nos seus estudos!

---

**Autor**: Adrielle

**Contato**: adrielle.dev@gmail.com

**Data**: 06/07/2024

---

**Referências**:

- [Documentação do MySQL](https://dev.mysql.com/doc/)
- [Documentação do PostgreSQL](https://www.postgresql.org/docs/)
- [W3Schools SQL Tutorial](https://www.w3schools.com/sql/)

---

**Autoria:** Esta parte dos materiais complementares foi criada pela professora [Pamela Borges](https://github.com/pamelaborges) da DIO.

Espero que este README seja útil para seus estudos e práticas com bancos de dados relacionais e SQL!