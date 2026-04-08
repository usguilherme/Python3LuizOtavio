caminho = "C:\\Users\\Guilherme\\Documents\\Nova pasta Atenção\\" #usando duas barras, evitar erros
caminho += "aula116.txt"

#arquivo = open(caminho, 'w') #w para escrever
#arquivo.close() #fecha o arquivo

with open(caminho, 'w+', enconding = 'utf8') as arquivo: #abrindo e fechando arquivos, modo escrita 'w', '+' escrita mais leitura, enconding = linguagem do windows
    arquivo.write("Linha 1\n")
    arquivo.write("linha 2\n")
    arquivo.writelines(('linha 3\n', 'linha 4\n'))

    arquivo.seek(0,0) #apenas voltar para o inicio do arquivo
    print(arquivo.read().strip()) #lendo arquivo
    print(arquivo.readline().strip()) #lendo linha

    for linha in arquivo.readline():
        print(linha.strip())

with open(caminho, 'r') as arquivo: #abrindo e fechando arquivos, modo leitura 'r'
    print(arquivo.read())

with open(caminho, 'a') as arquivo:
    arquivo.write("Olá mundo")