# Script: conversao_dbc.R
# Converte arquivos .dbc para .csv usando a biblioteca read.dbc

# Instalar o pacote read.dbc diretamente do GitHub (caso necessário)
if (!requireNamespace("read.dbc", quietly = TRUE)) {
    devtools::install_github("danicat/read.dbc")
}

# Carregar a biblioteca necessária
library("read.dbc")

# Função para converter todos os arquivos .dbc para .csv
convert_all_dbc <- function(rawDir, convertedDir) {
    files <- list.files(path = rawDir, pattern = "\\.dbc$", full.names = TRUE)  # Lista arquivos .dbc
    for (file in files) {
        tryCatch({
            print(paste("Convertendo:", file))  # Exibir arquivo atual

            # Ler arquivo .dbc
            x <- read.dbc(file)

            # Criar nome do arquivo CSV
            csv_file <- paste0(convertedDir, "/", tools::file_path_sans_ext(basename(file)), ".csv")

            # Salvar CSV garantindo delimitadores corretos
            write.table(x, file = csv_file, fileEncoding = "UTF-8", row.names = FALSE, sep = ",", dec = ".", na = "", quote = TRUE)

            print(paste("✅ Convertido com sucesso:", csv_file))
        }, error = function(e) {
            print(paste("❌ Erro ao converter:", file, "->", e$message))
        })
    }
}

# Criar a pasta de saída se não existir
dir.create("bases_descomprimidas", showWarnings = FALSE)

# Executar a conversão
convert_all_dbc("bases_raw", "bases_descomprimidas")