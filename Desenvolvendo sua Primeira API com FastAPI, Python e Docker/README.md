# Desenvolvendo sua Primeira API com FastAPI, Python e Docker

Neste projeto, aprenderemos a criar uma API assíncrona robusta para uma competição de crossfit utilizando o framework FastAPI. O objetivo é construir uma aplicação web moderna e eficiente, capaz de lidar com operações simultâneas de maneira escalável.

## Índice

1. [Introdução ao FastAPI](#introdução-ao-fastapi)
2. [Projeto: WorkoutAPI](#projeto-workoutapi)
3. [Configuração do Ambiente](#configuração-do-ambiente)
4. [Estrutura do Projeto](#estrutura-do-projeto)
5. [Endpoints e Query Parameters](#endpoints-e-query-parameters)
6. [Customização de Responses](#customização-de-responses)
7. [Manipulação de Exceções](#manipulação-de-exceções)
8. [Paginação](#paginaçao)
9. [Execução da API](#execução-da-api)
10. [Repositório Git](#repositório-git)
11. [Referências](#referências)

## Introdução ao FastAPI

### Quem é o FastAPI?

O FastAPI é um framework web moderno, rápido (alta performance), fácil de aprender, fácil de codar e pronto para produção. Ele é ideal para a construção de APIs com Python 3.6 ou superior, baseado nos type hints padrões do Python.

### Async

Código assíncrono significa que a linguagem tem um jeito de indicar ao computador/programa que, em certo ponto, ele terá que esperar por algo para finalizar em outro lugar.

## Projeto: WorkoutAPI

### Desafio de Projeto

Vamos construir uma API chamada WorkoutAPI para uma competição de crossfit. Este projeto é hands-on e simplificado, com poucas tabelas, mas suficiente para ensinar como utilizar o FastAPI.

### Modelagem de Entidade e Relacionamento (MER)

Representação das entidades e seus relacionamentos na API.

### Stack da API

A API foi desenvolvida utilizando FastAPI (async), juntamente com as seguintes bibliotecas:
- Alembic
- SQLAlchemy
- Pydantic

Para armazenamento dos dados, estamos utilizando o PostgreSQL, por meio do Docker.

## Configuração do Ambiente

### Requisitos

- Python 3.11.4 (recomendado usar pyenv)
- Docker
- Git

### Passos para Configuração

1. Clone o repositório:
    ```bash
    git clone https://github.com/digitalinnovationone/workout_api
    cd workout_api
    ```

2. Configure o ambiente virtual usando pyenv:
    ```bash
    pyenv virtualenv 3.11.4 workoutapi
    pyenv activate workoutapi
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Suba o banco de dados com Docker:
    ```bash
    make run-docker
    ```

5. Crie uma nova migration:
    ```bash
    make create-migrations d="nome_da_migration"
    ```

6. Crie o banco de dados:
    ```bash
    make run-migrations
    ```

## Estrutura do Projeto

```
workout_api/
├── app/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── database.py
│   └── routers/
│       └── atleta.py
├── tests/
│   └── test_atleta.py
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Endpoints e Query Parameters

### Adicionando Query Parameters nos Endpoints

#### Atleta

Adicione os seguintes parâmetros de consulta:
- **Nome**
- **CPF**

Exemplo de endpoint:
```python
@app.get("/atletas/")
def get_atletas(nome: str = None, cpf: str = None):
    # Lógica para buscar atletas com base nos parâmetros de consulta
    return {"nome": nome, "cpf": cpf}
```

## Customização de Responses

### Customizando Response de Retorno de Endpoints

#### Get All Atletas

No endpoint que obtém todos os atletas, retorne as seguintes informações:
- Nome do atleta
- Centro de treinamento
- Categoria

Exemplo:
```python
@app.get("/atletas/")
def get_all_atletas():
    # Lógica para buscar todos os atletas
    return [{"nome": "Nome do Atleta", "centro_treinamento": "Nome do Centro", "categoria": "Categoria"}]
```

## Manipulação de Exceções

### Manipulando Exceção de Integridade dos Dados

Se ocorrer um erro de integridade, como quando um atleta já está cadastrado com o mesmo CPF, trate a exceção `sqlalchemy.exc.IntegrityError` e retorne a seguinte mensagem:
- "Já existe um atleta cadastrado com o CPF: x"
- Use o código de status HTTP 303.

Exemplo:
```python
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

@app.post("/atletas/")
def create_atleta(atleta: AtletaCreate):
    try:
        db.add(atleta)
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=303, detail=f"Já existe um atleta cadastrado com o CPF: {atleta.cpf}")
```

## Paginação

### Adicionando Paginação com fastapi-pagination

Utilize a biblioteca fastapi-pagination para adicionar paginação aos resultados. Implemente os parâmetros `limit` e `offset` para controlar a quantidade de resultados retornados.

Exemplo:
```python
from fastapi_pagination import Page, paginate
from fastapi_pagination.paginator import Params

@app.get("/atletas/", response_model=Page[Atleta])
def get_atletas(params: Params = Depends()):
    return paginate(db.query(Atleta).all(), params)
```

## Execução da API

Para executar a API, utilize os seguintes comandos:

1. Suba a API:
    ```bash
    make run
    ```

2. Acesse a documentação interativa da API:
    ```
    http://127.0.0.1:8000/docs
    ```

## Repositório Git

O Git é um conceito essencial no mercado de trabalho atualmente, por isso sempre reforçamos sua importância em nossa metodologia educacional. Todo código-fonte desenvolvido durante este conteúdo foi versionado no seguinte endereço para que você possa consultá-lo a qualquer momento:

- [Repositório Oficial](https://github.com/digitalinnovationone/workout_api)

Neste repositório, insira todos os links e arquivos necessários para seu projeto, seja um arquivo de banco de dados ou um link para o template no Figma.

Dica: Se o expert forneceu um repositório Github, você pode dar um "fork" no repositório dele para organizar suas alterações e evoluções mantendo uma referência direta ao código-fonte original.

## Referências

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://docs.pydantic.dev/latest/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/en/20/)
- [Alembic Documentation](https://alembic.sqlalchemy.org/en/latest/)
- [fastapi-pagination Documentation](https://uriyyo-fastapi-pagination.netlify.app/)

---
