from pathlib import Path

# Obtém o diretório pai do arquivo atual
ROOT_PATH = Path(__file__).parent

try:
    # Tenta abrir o arquivo "1lorem.txt" para leitura
    with open(ROOT_PATH / "1lorem.txt", "r") as arquivo:
        # Lê o conteúdo do arquivo e o imprime
        print(arquivo.read())
except IOError as exc:
    # Se ocorrer um erro de E/S (por exemplo, o arquivo não existe), imprime uma mensagem de erro
    print(f"Erro ao abrir o arquivo {exc}")

# try:
#     with open(ROOT_PATH / "arquivo-utf-8.txt", "w", encoding="utf-8") as arquivo:
#         arquivo.write("Aprendendo a manipular arquivos utilizando Python.")
# except IOError as exc:
#     print(f"Erro ao abrir o arquivo {exc}")

try:
    # Tenta abrir o arquivo "arquivo-utf-8.txt" para leitura, usando a codificação utf-8
    with open(ROOT_PATH / "arquivo-utf-8.txt", "r", encoding="utf-8") as arquivo:
        # Lê o conteúdo do arquivo e o imprime
        print(arquivo.read())
except IOError as exc:
    # Se ocorrer um erro de E/S, imprime uma mensagem de erro
    print(f"Erro ao abrir o arquivo {exc}")
except UnicodeDecodeError as exc:
    # Se ocorrer um erro de decodificação Unicode, imprime a exceção detalhada
    print(exc)
