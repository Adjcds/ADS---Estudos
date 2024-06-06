import os
import shutil
from pathlib import Path

# Obtém o diretório pai do arquivo atual
ROOT_PATH = Path(__file__).parent

# Cria um novo diretório chamado "novo-diretorio" no diretório pai do arquivo atual
os.mkdir(ROOT_PATH / "novo-diretorio")

# Abre um novo arquivo chamado "novo.txt" em modo de escrita ("w") no diretório pai do arquivo atual
arquivo = open(ROOT_PATH / "novo.txt", "w")
# Fecha o arquivo
arquivo.close()

# Renomeia o arquivo "novo.txt" para "alterado.txt"
os.rename(ROOT_PATH / "novo.txt", ROOT_PATH / "alterado.txt")

# Remove o arquivo "alterado.txt"
os.remove(ROOT_PATH / "alterado.txt")

# Move o arquivo "novo.txt" para o diretório "novo-diretorio"
shutil.move(ROOT_PATH / "novo.txt", ROOT_PATH / "novo-diretorio" / "novo.txt")
