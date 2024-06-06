from pathlib import Path

# Obtém o diretório pai do arquivo atual
ROOT_PATH = Path(__file__).parent

try:
    # Tenta abrir o arquivo "novo.txt" para leitura dentro do diretório "novo-diretorio"
    arquivo = open(ROOT_PATH / "novo-diretorio" / "novo.txt", "r")
except FileNotFoundError as exc:
    # Trata o caso em que o arquivo não é encontrado
    print("Arquivo não encontrado!")
    print(exc)
except IsADirectoryError as exc:
    # Trata o caso em que o caminho fornecido se refere a um diretório, não a um arquivo
    print(f"Não foi possível abrir o arquivo: {exc}")
except IOError as exc:
    # Trata outros erros de E/S que podem ocorrer ao abrir o arquivo
    print(f"Erro ao abrir o arquivo: {exc}")
except Exception as exc:
    # Trata qualquer outro tipo de exceção não especificada acima
    print(f"Algum problema ocorreu ao tentar abrir o arquivo: {exc}")

# try:
#     arquivo = open(ROOT_PATH / "novo-diretorio")
# except IsADirectoryError as exc:
#     print(f"Não foi possível abrir o arquivo: {exc}")
