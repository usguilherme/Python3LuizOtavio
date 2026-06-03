import sqlite3
from pathlib import Path
ROOT_DIR = Path(__file__).parent #o caminho da pasta que estou agora
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME  
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE) #conectando o meu arquivo
cursor = connection.cursor() #inciando o cursor

cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        weight REAL
    )
''')

connection.commit()


cursor.close() #fechando o cursor
connection.close() #fechando a conexão
