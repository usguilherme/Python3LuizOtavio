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

    connection.commit() #dando commit nas tabelas


    #Funcoes departamento
    def inserirDepartamento(nome, descricao, responsavel):
        cursor.execute('''
            INSERT INTO {TABLE_NAME2} (nome, descricao, responsavel) VALUES (?,?,?)''', (nome, descricao, responsavel)
        )

        connection.commit() 
    
    def buscarDepartamentos():
        cursor.execute('''
        SELECT * 
        FROM {TABLE_NAME2}''')

        departamentos = cursor.fetchall #pega todos meus registros e tranforma em tupla
        for dep in departamentos:
            print(dep) #cada tupla ira ser mostrada
        
        return departamentos 
    
    def buscarDepartamentoId(id_departamento):
        cursor.execute('''
        SELECT * 
        FROM {TABLE_NAME2} 
        WHERE id = ?''', (id_departamento))

        departamento = cursor.fetchone #retorna só um registro
        return departamento

    def atualizarDepartamento(id_departamento, nome, descricao, responsavel):
        cursor.execute(f'''
        UPDATE {TABLE_NAME2} 
        SET nome = ?, descricao = ?, responsavel = ? 
        WHERE id = ?''',(nome, descricao, responsavel, id_departamento))
    
        connection.commit()
        print(f'Departamento {id_departamento} atualizado com sucesso!')
    
    def deletarDepartamento(id_departamento):
        cursor.execute(f'''
        DELETE FROM {TABLE_NAME2} 
        WHERE ID = ?''', (id_departamento))
    
        connection.commit()
        print(f'Departamento {id_departamento} deletado com sucesso!')


    #FUNCOES DA TABELA CLIENTE
    def inserirCliente(nome, email, telefone, cpf, idade, cidade, endereco, data_cadastro, departamento_id):
        try:
            cursor.execute(f'''
            INSERT INTO {TABLE_NAME1} (nome, email, telefone, cpf, idade, cidade, endereco, data_cadastro, departamento_id)
            VALUES (?,?,?,?,?,?,?,?,?)''', (nome, email, telefone, cpf, idade, cidade, endereco, data_cadastro, departamento_id))
            connection.commit()
            print(f'Cliente {nome} cadastradi com sucesso!')
        except sqlite3.Error as erro:
            connection.rollback() #desfaz alteração do meu bd
            print(f'Cliente {nome} cadastrado com sucesso!')
    
    def buscarClientes():
        cursor.execute('SELECT * FROM {TABLE_NAME1}')
        clientes = cursor.fetchall
        for cli in clientes:
            print(cli)

        print('---')
        return clientes

    def buscarClienteId(id_cliente):
        cursor.execute(f''' 
            SELECT *
            FROM {TABLE_NAME1}
            WHERE id = ?
        ''', (id_cliente,))
        cliente = cursor.fetchone()
        return cliente

    def atualizarCliente(id_cliente, nome, email, telefone, cpf, idade, cidade, endereco, data_cadastro, departamento_id):
        cursor.execute(f'''
            UPDATE {TABLE_NAME1}
            SET nome = ?, email = ?, telefone = ?, cpf = ?, idade = ?,
                cidade = ?, endereco = ?, data_cadastro = ?, departamento_id = ?
            WHERE id = ?''', (nome, email, telefone, cpf, idade, cidade, endereco, data_cadastro, departamento_id, id_cliente))
        connection.commit()
        print(f'Cliente {id_cliente} atualizado com sucesso!')

    def removerCliente(id_cliente):
        cursor.execute(f'''
            DELETE FROM {TABLE_NAME1}
            WHERE id = ?''', (id_cliente,)
        )
        connection.commit()
        print(f'Cliente {id_cliente} removido com sucesso!')




