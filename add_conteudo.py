# Nome do arquivo
nome_arquivo = "dados.txt"

# Dados a serem acrescentados
novos_dados = ["Segunda linha\n", "Terceira linha\n", "Quarta linha\n"]

# Leitura do arquivo para obter a lista de linhas existentes
with open(nome_arquivo, "r") as arquivo:
    linhas_existentes = arquivo.readlines()

# Abre o arquivo em modo de escrita ('a' para "append") e acrescenta os novos dados ao final do arquivo,
# verificando antes se cada linha já existe no arquivo.
with open(nome_arquivo, "a") as arquivo:
    for dado in novos_dados:
        if dado not in linhas_existentes:
            arquivo.write(dado)

# Leitura do arquivo para verificar o resultado.
with open(nome_arquivo, "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
