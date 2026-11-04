import sqlite3
from pathlib import Path #da minha biblioteca pathlib, eu importo a classe Path


ROOT_DIR = Path(__file__).parent  #caminho até meu arquivo atual, sem o proprio arquivo
DB_FILE = ROOT_DIR / 'db.bancoDados3'
TABLE_NAME = 'usuarios'

connection = sqlite3.connect(DB_FILE) #caso não exista, crio o arquivo, e conecto ele ao BD
cursor = connection.cursor() #variavel que puxa os comandos do proprio sql

#CRIANDO A TABELA usuarios
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'nome TEXT,'
    'idade INTEGER,'
    'peso REAL' #ponto flutuante em sqlite
    ')'
)

connection.commit() #salvando minhas modificaçoes


#INSERINDO DADOS NO SQLITE

#cursor.execute(f'INSERT INTO {TABLE_NAME} (nome, idade, peso) VALUES (?,?,?)', ('Valessa Nascimento', 22, 51)) #inserindo valores
#cursor.executemany( #inserindo varios valores
    #f'INSERT INTO {TABLE_NAME} (nome, idade, peso) VALUES (?,?,?)', 
    #[('Guilherme', 21, 82), ('Cassia', 50, 62)]
#)

#DELETAR MINHA TABELA

connection.commit() #Salvo minha tabela



