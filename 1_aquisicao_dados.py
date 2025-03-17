import os
import json
import pandas as pd

# Definição do caminho base dos arquivos no FTP
FTP_BASE_URL = "ftp://ftp.datasus.gov.br/dissemin/publicos/CNES/200508_/Dados/PF/PFMG"
LINK_SUFFIX = ".dbc"

# Período dos arquivos desejados (anos e meses)
anos = range(2019, 2021)
meses = range(1, 2)

# Lista para armazenar os links de download
links = [
    f"{FTP_BASE_URL}{str(ano)[2:]}{str(mes).zfill(2)}{LINK_SUFFIX}"
    for ano in anos
    for mes in meses
]

# Salvar os links em um arquivo JSON para referência futura
with open("links.json", "w", encoding="utf-8") as f:
    json.dump(links, f, indent=4)

print("✅ Links de download gerados e salvos em 'links.json'.")

# Criar a pasta de armazenamento dos arquivos brutos
os.makedirs("bases_raw", exist_ok=True)

# Baixar os arquivos do FTP para a pasta "bases_raw"
for link in links:
    os.system(f"wget -P bases_raw --inet4-only {link}")

print("✅ Download dos arquivos concluído e salvos em 'bases_raw/'.")

# Criar a pasta de saída dos arquivos convertidos
os.makedirs("bases_descomprimidas", exist_ok=True)