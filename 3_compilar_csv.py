#Script para compilar todos os arquivos CSV gerados na conversão dos arquivos DBC.

import os
import pandas as pd

# Criar a pasta de saída para os arquivos compilados
os.makedirs("bases_compiladas", exist_ok=True)

# Listar todos os arquivos CSV na pasta "bases_descomprimidas"
csv_files = [f for f in os.listdir("bases_descomprimidas") if f.endswith(".csv")]

# Criar um dataframe vazio para armazenar os dados consolidados
df_compilado = pd.DataFrame()

# Percorrer todos os arquivos CSV e fazer o append no dataframe compilado
for file in csv_files:
    file_path = os.path.join("bases_descomprimidas", file)
    print(f"📄 Lendo {file_path}")
    df = pd.read_csv(file_path, dtype=str)  # Ler os dados como string para evitar problemas de tipo
    df_compilado = pd.concat([df_compilado, df], ignore_index=True)

# Salvar o arquivo consolidado na nova pasta
output_file = "bases_compiladas/dados_compilados.csv"
df_compilado.to_csv(output_file, index=False, encoding="utf-8")

print(f"✅ Arquivo compilado salvo em {output_file}")