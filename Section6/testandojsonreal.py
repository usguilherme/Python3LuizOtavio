import json
import os

dados = [

    {
        'Nome': 'Guilherme',
        'idade': 21,
        'ano_nascimento': 2005
    },
    {
        'Nome': 'valessa',
        'idade': 21,
        'ano_nascimento': 2004
    },
    {
        'Nome': 'Cassia',
        'idade': 50,
        'ano_nascimento': 1990
    },
    {
        'Nome': 'Isaias',
        'idade': 51,
        'ano_nascimento': 1990
    }
]

#C:\Users\Guilherme\Documents\Python3LuizOtavio-main\Section6
#armazenar dados em um arquivo.json
link = os.path.join('C:\\', 'Users', 'Guilherme','Documents', 'Python3LuizOtavio-main','Section6', 'dados.json' )

with open(link, 'w', encoding = 'utf-8') as arquivo: #tranformo dicionário para json
    json.dump(dados, arquivo, indent = 2)

with open(link, 'r', encoding= 'utf-8') as arquivo: #tranformo json para dicionário
    resultados = json.load(arquivo)

print(resultados)