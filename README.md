# 📥 Extract Datasus - Aquisição e Processamento de Dados CNES

Este repositório contém um conjunto de scripts para **baixar, converter e compilar dados do CNES (Cadastro Nacional de Estabelecimentos de Saúde) a partir do FTP do DATASUS**.

## 🚀 Visão Geral
Os dados do CNES são disponibilizados em arquivos no formato `.dbc`, que precisam ser processados antes de serem utilizados para análise. Este projeto automatiza esse processo em três etapas:

1. **Baixa os arquivos `.dbc` do FTP do DATASUS.**
2. **Converte os arquivos `.dbc` para `.csv` utilizando R.**
3. **Compila os arquivos `.csv` em um único dataset consolidado.**

---

## 📌 Estrutura do Projeto
```plaintext
extract_datasus/
│── 1_aquisicao_dados.py      # Script para baixar arquivos do FTP do DATASUS
│── 2_conversao_dbc.R         # Script em R para converter .dbc para .csv
│── 3_compilar_csv.py         # Script para compilar os arquivos CSV em um único dataset
│── .gitignore                # Arquivos ignorados pelo Git
│── README.md                 # Documentação do projeto
│── requirements.txt          # Dependências do Python
│── bases_raw/                # Diretório onde os arquivos .dbc são armazenados
│── bases_descomprimidas/     # Diretório onde os arquivos convertidos para .csv são armazenados
│── bases_compiladas/         # Diretório onde o dataset consolidado é salvo
