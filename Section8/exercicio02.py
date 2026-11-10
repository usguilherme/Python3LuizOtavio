from pathlib import Path
import sqlite3

ROOT_DIR = Path(__file__).parent
FILE_NAME = ROOT_DIR /'visualizador.db'
TABLE_NAME1 = 'clientes'
TABLE_NAME2 = 'departamento'

connection = sqlite3.connect(FILE_NAME) 
cursor = connection.cursor()


#MEUS COMANDOS SQL
def inicializadorTabelas():
    
    #Criando minha tebala departamento
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {TABLE_NAME2} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT,
            responsavel TEXT
        )
    ''')
    
    #criando minha tabela clientes
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {TABLE_NAME1} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            email TEXT,
            telefone TEXT,
            cpf TEXT,
            idade INTEGER,
            cidade TEXT,
            endereco TEXT,
            data_cadastro DATE,
            departamento_id INTEGER, 
            FOREIGN KEY (departamento_id) 
            REFERENCES {TABLE_NAME2}(id)
        ) 
    ''')

inicializadorTabelas()



