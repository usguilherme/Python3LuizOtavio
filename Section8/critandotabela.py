import sqlite3

connect = sqlite3.connect('meubanco.db')
cursor = connect.cursor()

#CRIANDO TABELA
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        nome TEXT NOT NULL,
        idade INTEGER,
        altura REAL
)
''')

#SALVANDO TABELA
connect.commit()

#INSERINDO USUARIO
cursor.execute('''
    INSERT INTO usuarios(nome, idade, altura) VALUES (?,?,?)''',
    ('Guilherme', 21, 1.91))

#SALVANDO TABELA
connect.commit()

#FECHANDO TABELA
connect.close()


