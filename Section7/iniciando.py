import sqlite3
from pathlib import Path
ROOT_DIR = Path(__file__).parent #o caminho da pasta que estou agora
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME  
TABLE_NAME = 'customers'

#iniciando conexao e cursor
connection = sqlite3.connect(DB_FILE) #conectando o meu arquivo
cursor = connection.cursor() #inciando o cursor


#Criando tabela
cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        weight REAL
    )
''')

#DELETANDO MINHA TABELA, APENAS PRA EVITAR REPETICAO
cursor.execute(f'''
    DELETE FROM {TABLE_NAME}
''')

connection.commit() #apenas salvando

#registrar valores nas colunas da minha tabela
cursor.execute(f'''
    INSERT INTO {TABLE_NAME} (id, name, weight)
    VALUES (NULL, "Guilherme Nunes", 82)
''')

cursor.execute(f'''
    INSERT INTO {TABLE_NAME} (id, name, weight)
    VALUES (NULL, "VALESSA NASCIMENTO", 52)
''')
connection.commit()

#fechando
cursor.close() #fechando o cursor
connection.close() #fechando a conexão

