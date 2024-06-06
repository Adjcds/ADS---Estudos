import csv
from pathlib import Path

# Obtém o diretório pai do arquivo atual
ROOT_PATH = Path(__file__).parent

# Índices das colunas no arquivo CSV
COLUNA_ID = 0
COLUNA_NOME = 1

try:
    # Escrevendo dados no arquivo CSV usando csv.writer
    with open(ROOT_PATH / "usuarios.csv", "w", newline="", encoding="utf-8") as arquivo:
        # Cria um objeto escritor de CSV
        escritor = csv.writer(arquivo)
        # Escreve o cabeçalho
        escritor.writerow(["id", "nome"])
        # Escreve linhas de dados
        escritor.writerow(["1", "Maria"])
        escritor.writerow(["2", "João"])
except IOError as exc:
    # Trata erros de E/S
    print(f"Erro ao criar o arquivo. {exc}")

try:
    # Lendo dados do arquivo CSV usando csv.reader
    with open(ROOT_PATH / "usuarios.csv", "r", newline="", encoding="utf-8") as arquivo:
        # Cria um objeto leitor de CSV
        leitor = csv.reader(arquivo)
        # Itera sobre as linhas do arquivo
        for idx, row in enumerate(leitor):
            if idx == 0:
                continue  # Ignora o cabeçalho
            # Imprime dados das colunas selecionadas
            print(f"ID: {row[COLUNA_ID]}")
            print(f"Nome: {row[COLUNA_NOME]}")
except IOError as exc:
    # Trata erros de E/S
    print(f"Erro ao criar o arquivo. {exc}")

try:
    # Lendo dados do arquivo CSV como dicionários usando csv.DictReader
    with open(ROOT_PATH / "usuarios.csv", newline="") as csvfile:
        # Cria um objeto leitor de CSV que retorna dicionários
        reader = csv.DictReader(csvfile)
        # Itera sobre os dicionários representando cada linha
        for row in reader:
            # Acessa os valores pelo nome da coluna
            print(f"ID: {row['id']}")
            print(f"Nome: {row['nome']}")
except IOError as exc:
    # Trata erros de E/S
    print(f"Erro ao criar o arquivo. {exc}")
