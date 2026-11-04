import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
ARQUIVO = ROOT_DIR / 'db.testandobd'
TABLE_NAME = 'clientes'
#FIZ MINHA CONEXAO, E CRIEI O MEU CURSOR
connection = sqlite3.connect(ARQUIVO)
cursor = connection.cursor()

#Criar minha tabela
def criarTabela():
    cursor.execute(
        f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INTEGER PRIMARY KEY AUTOINCREMENT,'
            'nome TEXT,'
            'email TEXT,'
            'telefone TEXT,'
            'idade INTEGER,'
            'cidade TEXT,'
            'data DATE'
        ')'
    )
    connection.commit() #salvando minha tabela


#INSERIR NA MINHA TABELA
def inserirNaTabela(nome, email, telefone, idade, cidade, data):
    cursor.execute(
        f'INSERT INTO {TABLE_NAME} (nome, email, telefone, idade, cidade, data) VALUES (?,?,?,?,?,?)',
        (nome, email, telefone, idade, cidade, data)
    )
    connection.commit()


#Buscando todos os meus clientes de uma vez
def buscarClientes():
    cursor.execute('SELECT * FROM clientes')
    return cursor.fetchall()

#Buscando um cliente especifico
def buscarClientesId(id):
    cursor.execute('SELECT * FROM clientes WHERE id = ?', (id,))
    return cursor.fetchone() #retorna um só registro

#Remover na tabela
def removerNaTabela(id):
    cursor.execute('DELETE FROM clientes WHERE id = ?', (id,))
    connection.commit()
    return cursor.rowcount #quantidade de linhas excluidas

#Excluir tabela
def excluirTabela():
    cursor.execute('DROP TABLE clientes')
    connection.commit()

def apagarRegistroTabela():
    cursor.execute('DELETE FROM clientes')
    connection.commit()

#Atualizar dados de um cliente
def atualizarDados(id, novo_email):
    cursor.execute('UPDATE clientes SET email = ? WHERE id = ?', (novo_email,id))
    connection.commit()
    return cursor.rowcount


    

connection.close() #fechando minha conexão