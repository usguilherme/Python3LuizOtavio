import sqlite3
from pathlib import Path
ROOT_DIR = Path(__file__).parent #o caminho da pasta que estou agora
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME  

con = sqlite3.connect(DB_FILE) #conectando o meu arquivo
cursor = con.cursor() #inciando o cursor
cursor.close() #fechando o cursor
con.close() #fechando a conexão
