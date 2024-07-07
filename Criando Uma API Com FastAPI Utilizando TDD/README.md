## Criando uma API com FastAPI utilizando TDD

### Desafio de Projeto: Implementação de uma API com FastAPI e Testes

Neste projeto, você aprenderá a implementar uma API com FastAPI usando a abordagem de Test-Driven Development (TDD) e o Pytest para realizar testes unitários e de integração. A API utilizará o banco de dados MongoDB e seguirá boas práticas de documentação.

### Passos do Projeto:

1. **Instalação das Dependências**:
   - Certifique-se de ter o Python instalado em sua máquina.
   - Instale FastAPI, Pytest e outras bibliotecas necessárias:
     ```sh
     pip install fastapi uvicorn pytest httpx motor
     ```

2. **Criação da Estrutura do Projeto**:
   - Crie uma pasta para o projeto e dentro dela os seguintes arquivos:
     - `main.py`: Arquivo principal da aplicação.
     - `test_main.py`: Arquivo de testes.
     - `requirements.txt`: Lista das dependências do projeto.

3. **Definição das Rotas da API**:
   - No `main.py`, crie as rotas (endpoints) da API utilizando FastAPI.
     ```python
     from fastapi import FastAPI

     app = FastAPI()

     @app.get("/")
     def read_root():
         return {"message": "Bem-vindo à API de crossfit!"}
     ```

4. **Configuração do MongoDB**:
   - Instale a biblioteca `motor` para trabalhar com MongoDB.
   - Crie a conexão com o banco de dados no `main.py`.

5. **Implementação dos Testes**:
   - No `test_main.py`, crie testes unitários e de integração para as funcionalidades da API.
   - Utilize o Pytest para executar os testes automaticamente.

6. **Documentação do Projeto**:
   - Utilize o Swagger UI gerado automaticamente pelo FastAPI para documentar as rotas da API.
   - Adicione comentários e docstrings explicativas no código.

7. **Execução da Aplicação**:
   - Inicie o servidor com o comando:
     ```sh
     uvicorn main:app --reload
     ```
   - Acesse a documentação da API em `http://localhost:8000/docs`.

### Dicas para Escrever Testes Eficazes com Pytest:

1. **Organize seus Testes**:
   - Separe os testes em arquivos ou pastas específicas, como um diretório chamado `tests`.
   - Nomeie os arquivos de teste com o prefixo `test_` para que o Pytest os reconheça automaticamente.

2. **Escreva Testes Claros e Descritivos**:
   - Dê nomes significativos aos testes.
   - Use docstrings para explicar o propósito de cada teste.

3. **Use Fixtures**:
   - As fixtures no Pytest permitem criar dados de teste reutilizáveis.
   - Defina fixtures para inicializar objetos, configurar o ambiente ou preparar dados para os testes.

4. **Teste Diferentes Cenários**:
   - Escreva testes para casos de sucesso e também para cenários de erro.
   - Considere testar limites, valores nulos, entradas inválidas, etc.

5. **Use Asserts**:
   - Use afirmações (assertions) para verificar se o resultado esperado é igual ao resultado real.
     ```python
     def test_soma():
         resultado = soma(2, 3)
         assert resultado == 5
     ```

6. **Use Marcadores (Markers)**:
   - Os marcadores permitem agrupar e executar testes específicos.
   - Marque testes como "lentos" ou "de integração" e execute-os separadamente.

7. **Execute os Testes**:
   - Execute os testes com o comando:
     ```sh
     pytest
     ```

8. **Verifique a Cobertura de Código**:
   - Use ferramentas como o `pytest-cov` para verificar a cobertura de código pelos testes.
   - Isso ajuda a identificar áreas não testadas.

### Repositório Git

O Git é um conceito essencial no mercado de trabalho atualmente, por isso sempre reforçamos sua importância em nossa metodologia educacional. Todo código-fonte desenvolvido durante este conteúdo foi versionado no seguinte endereço para que você possa consultá-lo a qualquer momento:

- [Repositório Oficial](https://github.com/digitalinnovationone/store_api)

Neste repositório, insira todos os links e arquivos necessários para o projeto, como arquivos de banco de dados ou links para templates no Figma. Se o expert forneceu um repositório no GitHub, você pode fazer um fork para organizar suas alterações e evoluções, mantendo uma referência direta ao código-fonte original.

### Referências
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pytest Documentation](https://docs.pytest.org/en/stable/)
- [MongoDB Documentation](https://docs.mongodb.com/)
- [Motor Documentation](https://motor.readthedocs.io/en/stable/)
- [Pydantic Documentation](https://docs.pydantic.dev/latest/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/en/20/)
- [Alembic Documentation](https://alembic.sqlalchemy.org/en/latest/)
- [Fastapi-pagination Documentation](https://uriyyo-fastapi-pagination.netlify.app/)