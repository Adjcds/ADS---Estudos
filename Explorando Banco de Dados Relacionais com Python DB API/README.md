# Explorando Banco de Dados Relacionais com Python DB API

Este README oferece uma introdução abrangente ao uso de bancos de dados relacionais com Python, utilizando a DB API. Vamos explorar conceitos fundamentais dos bancos de dados relacionais e como interagir com eles de maneira eficaz usando Python.

## Introdução aos Bancos de Dados Relacionais - Parte 1

### O que são Bancos de Dados Relacionais?

Bancos de dados relacionais (RDBMS - Relational Database Management Systems) são sistemas de gerenciamento de banco de dados baseados no modelo relacional, onde os dados são armazenados em tabelas compostas por linhas e colunas. Cada linha representa um registro único e cada coluna um atributo dos dados.

### Principais Características:

- **Modelagem de Dados com Tabelas:** Dados organizados em tabelas com linhas e colunas.
- **Chaves Primárias e Estrangeiras:** Chaves primárias identificam unicamente cada registro, enquanto chaves estrangeiras estabelecem relacionamentos entre tabelas.
- **Integridade Referencial:** Garantia de que as relações entre tabelas são mantidas corretamente.
- **SQL (Structured Query Language):** Linguagem padrão para gerenciamento e manipulação de dados.

### Vantagens dos Bancos de Dados Relacionais:

- **Consistência e Integridade dos Dados:** Regras rígidas garantem a consistência dos dados.
- **Suporte a Transações ACID:** Atomicidade, Consistência, Isolamento e Durabilidade para operações seguras e confiáveis.
- **Consultas Complexas com SQL:** Capacidade de realizar consultas complexas e obter insights valiosos dos dados.

### Exemplos de Bancos de Dados Relacionais:

- MySQL
- PostgreSQL
- SQLite
- Oracle Database
- Microsoft SQL Server

## Introdução aos Bancos de Dados Relacionais - Parte 2

### Conectando-se a um Banco de Dados Relacional com Python DB API

A Python DB API (PEP 249) é um padrão para interfaces de bancos de dados em Python, que fornece uma maneira consistente de interagir com diferentes bancos de dados.

#### Passos Básicos para Conectar-se a um Banco de Dados:

1. **Instalar a Biblioteca do Banco de Dados:**
   - Para MySQL: `pip install mysql-connector-python`
   - Para PostgreSQL: `pip install psycopg2`
   - Para SQLite: `pip install sqlite3` (SQLite já está incluído na biblioteca padrão do Python)

2. **Importar a Biblioteca e Estabelecer Conexão:**

```python
import sqlite3  # ou mysql.connector, psycopg2, etc.

# Conectar-se ao banco de dados
conn = sqlite3.connect('example.db')  # ou outras bibliotecas de banco de dados
```

3. **Criar um Cursor para Executar Comandos SQL:**

```python
cursor = conn.cursor()
```

4. **Executar Comandos SQL:**

```python
# Criar uma tabela
cursor.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

# Inserir dados
cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 30)")

# Consultar dados
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())
```

5. **Fechar a Conexão:**

```python
conn.close()
```

## Introdução aos Bancos de Dados Relacionais - Parte 3

### Manipulação de Dados com Python DB API

#### Inserção de Dados:

```python
def insert_user(name, age):
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
```

#### Consulta de Dados:

```python
def fetch_users():
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()
```

#### Atualização de Dados:

```python
def update_user_age(user_id, new_age):
    cursor.execute("UPDATE users SET age = ? WHERE id = ?", (new_age, user_id))
    conn.commit()
```

#### Exclusão de Dados:

```python
def delete_user(user_id):
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id))
    conn.commit()
```

### Tratamento de Erros e Exceções

É importante tratar erros e exceções ao trabalhar com bancos de dados para garantir que sua aplicação possa lidar com problemas de maneira graciosa.

```python
try:
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    # Executar comandos SQL
except sqlite3.Error as e:
    print(f"Erro ao conectar ao banco de dados: {e}")
finally:
    if conn:
        conn.close()
```

### Exemplo Completo:

```python
import sqlite3

def connect_db():
    return sqlite3.connect('example.db')

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
    conn.commit()

def insert_user(conn, name, age):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()

def fetch_users(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

def update_user_age(conn, user_id, new_age):
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET age = ? WHERE id = ?", (new_age, user_id))
    conn.commit()

def delete_user(conn, user_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id))
    conn.commit()

# Exemplo de uso
conn = connect_db()
create_table(conn)
insert_user(conn, 'Alice', 30)
insert_user(conn, 'Bob', 25)
print(fetch_users(conn))
update_user_age(conn, 1, 31)
delete_user(conn, 2)
print(fetch_users(conn))
conn.close()
```

## Conectando com o Banco de Dados

Para conectar-se a um banco de dados, utilize a biblioteca apropriada para o seu RDBMS. A conexão é estabelecida usando um método específico da biblioteca.

### Exemplo com SQLite:

```python
import sqlite3

# Conectar-se ao banco de dados
conn = sqlite3.connect('example.db')
```

### Exemplo com MySQL:

```python
import mysql.connector

# Conectar-se ao banco de dados
conn = mysql.connector.connect(
    host="localhost",
    user="seu_usuario",
    password="sua_senha",
    database="nome_do_banco"
)
```

## Criando uma Tabela

Para criar uma tabela no banco de dados, utilize o comando `CREATE TABLE`.

### Exemplo:

```python
cursor = conn.cursor()
cursor.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
conn.commit()
```

## Inserindo Registros

Para inserir registros em uma tabela, utilize o comando `INSERT INTO`.

### Exemplo:

```python
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Alice', 30))
conn.commit()
```

## Atualizando Registros

Para atualizar registros existentes, utilize o comando `UPDATE`.

### Exemplo:

```python
cursor.execute("UPDATE users SET age = ? WHERE name = ?", (31, 'Alice'))
conn.commit()
```

## Removendo Registros

Para remover registros, utilize o comando `DELETE`.

### Exemplo:

```python
cursor.execute("DELETE FROM users WHERE name = ?", ('Alice',))
conn.commit()
```

## Inserindo Registros em Lote

Para inserir múltiplos registros de uma vez, utilize o método `executemany`.

### Exemplo:

```python
users = [('Bob', 25), ('Carol', 27), ('Dave', 22)]
cursor.executemany("INSERT INTO users (name, age) VALUES (?, ?)", users)
conn.commit()
```

## Consultando os Registros

Para consultar registros, utilize o comando `SELECT`.

### Exemplo:

```python
cursor.execute("SELECT * FROM users")
result = cursor.fetchall()
print(result)
```

## Alterando o `row_factory`

A propriedade `row_factory` do cursor permite personalizar a forma como os resultados das consultas são retornados.

### Exemplo para Retornar Dicionários:

```python
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(dict(row))
```

## Boas Práticas

### Fechar Conexões

Sempre feche a conexão ao finalizar as operações para evitar vazamentos de memória e travamentos de recursos.

```python
conn.close()
```

### Uso de Placeholders

Use placeholders ao passar parâmetros para consultas para evitar injeção de SQL.

```python
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Bob', 25))
```

### Tratamento de Erros

Utilize blocos `try-except-finally` para tratar erros e garantir que a conexão seja fechada corretamente.

```python
try:
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    # Executar comandos SQL
except sqlite3.Error as e:
    print(f"Erro ao conectar ao banco de dados: {e}")
finally:
    if conn:
        conn.close()
```

## Gerenciando Transações

Utilize transações para garantir a integridade dos dados durante operações que envolvem múltiplos comandos SQL. Transações permitem que você confirme (`commit`) ou desfaça (`rollback`) mudanças no banco de dados.

Aqui está a continuação do README sobre Explorando Banco de Dados Relacionais com Python DB API:

## Gerenciando Transações

Utilize transações para garantir a integridade dos dados durante operações que envolvem múltiplos comandos SQL. Transações permitem que você confirme (`commit`) ou desfaça (`rollback`) mudanças no banco de dados.

### Exemplo de Transação Completa:

```python
import sqlite3

# Função para conectar ao banco de dados
def connect_db():
    conn = sqlite3.connect('example.db')
    return conn

# Função para criar uma tabela
def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
    conn.commit()

# Função para inserir um usuário
def insert_user(conn, name, age):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()

# Função para consultar usuários
def fetch_users(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

# Função para atualizar a idade de um usuário
def update_user_age(conn, user_id, new_age):
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET age = ? WHERE id = ?", (new_age, user_id))
    conn.commit()

# Função para excluir um usuário
def delete_user(conn, user_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()

# Exemplo de uso de transação
def example_transaction():
    conn = connect_db()
    try:
        create_table(conn)

        # Iniciar transação
        conn.execute("BEGIN")

        # Inserir usuários
        insert_user(conn, 'Alice', 30)
        insert_user(conn, 'Bob', 25)

        # Consultar usuários antes da atualização
        users_before = fetch_users(conn)
        print("Usuários antes da atualização:", users_before)

        # Atualizar idade do usuário com id=1
        update_user_age(conn, 1, 31)

        # Consultar usuários depois da atualização
        users_after = fetch_users(conn)
        print("Usuários depois da atualização:", users_after)

        # Commit da transação
        conn.commit()
    except sqlite3.Error as e:
        print(f"Erro durante a transação: {e}")
        # Rollback em caso de erro
        conn.rollback()
    finally:
        conn.close()

# Executar exemplo de transação
example_transaction()
```

Este exemplo demonstra como usar transações para garantir que todas as operações (inserção, atualização e consulta) sejam tratadas de forma atômica e segura, mantendo a integridade dos dados mesmo em casos de erros durante o processo.

### Exercícios

### Exercício 1: Conectando-se ao Banco de Dados

1. **Qual é o primeiro passo para conectar-se a um banco de dados usando Python DB API?**

   a) Importar a biblioteca do banco de dados  
   b) Criar uma tabela  
   c) Executar uma consulta SQL  
   d) Fechar a conexão

   **Resposta correta:** a) Importar a biblioteca do banco de dados

   **Explicação:** O primeiro passo para conectar-se a um banco de dados usando Python DB API é importar a biblioteca adequada, como `sqlite3`, `mysql.connector`, ou `psycopg2`.

---

### Exercício 2: Criando uma Tabela

2. **Como você cria uma tabela em um banco de dados usando Python DB API?**

   a) Utilizando o método `create_table()`  
   b) Chamando `execute("CREATE TABLE ...")`  
   c) Inserindo dados diretamente  
   d) Usando o método `insert_table()`

   **Resposta correta:** b) Chamando `execute("CREATE TABLE ...")`

   **Explicação:** Para criar uma tabela, você utiliza o método `execute()` com o comando SQL `CREATE TABLE ...`.

---

### Exercício 3: Inserindo Registros

3. **Qual método é usado para inserir registros em uma tabela usando Python DB API?**

   a) `execute("INSERT ...")`  
   b) `add_record()`  
   c) `insert_row()`  
   d) `execute("UPDATE ...")`

   **Resposta correta:** a) `execute("INSERT ...")`

   **Explicação:** Para inserir registros em uma tabela, utiliza-se o método `execute()` com o comando SQL `INSERT INTO ...`.

---

### Exercício 4: Consultando Registros

4. **Como você executa uma consulta para recuperar todos os registros de uma tabela usando Python DB API?**

   a) `fetch_all()`  
   b) `query("SELECT ...")`  
   c) `execute("SELECT ...")`  
   d) `fetch_rows()`

   **Resposta correta:** a) `fetch_all()`

   **Explicação:** O método `fetch_all()` é utilizado para recuperar todos os registros de uma consulta executada com `execute("SELECT ...")`.

---

### Exercício 5: Atualizando Registros

5. **Qual método é usado para atualizar dados em uma tabela usando Python DB API?**

   a) `update_record()`  
   b) `execute("UPDATE ...")`  
   c) `change_data()`  
   d) `modify_table()`

   **Resposta correta:** b) `execute("UPDATE ...")`

   **Explicação:** Para atualizar registros em uma tabela, utiliza-se o método `execute()` com o comando SQL `UPDATE ...`.

### Conclusão

Este README abrange os conceitos fundamentais de bancos de dados relacionais e SQL, proporcionando uma base sólida para você iniciar e aprofundar seus conhecimentos. Ao seguir os exemplos e commits explicativos fornecidos, você poderá aprender e aplicar esses conceitos de forma prática em seus projetos.

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

