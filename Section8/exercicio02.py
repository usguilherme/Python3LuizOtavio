from pathlib import Path
import sqlite3

ROOT_DIR = Path(__file__).parent
FILE_NAME = ROOT_DIR / 'visualizador.db'
TABLE_NAME1 = 'clientes'
TABLE_NAME2 = 'departamento'

connection = sqlite3.connect(FILE_NAME)
cursor = connection.cursor()


# MEUS COMANDOS SQL
def inicializadorTabelas():
    # Criando minha tabela departamento
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {TABLE_NAME2} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT,
            responsavel TEXT
        )
    ''')

    # Criando minha tabela clientes
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

    connection.commit()  # dando commit nas tabelas


# FUNÇÕES DEPARTAMENTO
def inserirDepartamento(nome, descricao, responsavel):
    cursor.execute(f'''
        INSERT INTO {TABLE_NAME2} (nome, descricao, responsavel) VALUES (?,?,?)
    ''', (nome, descricao, responsavel))
    connection.commit()


def buscarDepartamentos():
    cursor.execute(f'''
        SELECT *
        FROM {TABLE_NAME2}
    ''')
    departamentos = cursor.fetchall()  # pega todos os registros e transforma em lista de tuplas
    for dep in departamentos:
        print(dep)
    return departamentos


def buscarDepartamentoId(id_departamento):
    cursor.execute(f'''
        SELECT *
        FROM {TABLE_NAME2}
        WHERE id = ?
    ''', (id_departamento,))
    departamento = cursor.fetchone()  # retorna só um registro
    return departamento


def atualizarDepartamento(id_departamento, nome, descricao, responsavel):
    cursor.execute(f'''
        UPDATE {TABLE_NAME2}
        SET nome = ?, descricao = ?, responsavel = ?
        WHERE id = ?
    ''', (nome, descricao, responsavel, id_departamento))
    connection.commit()
    print(f'Departamento {id_departamento} atualizado com sucesso!')


def deletarDepartamento(id_departamento):
    cursor.execute(f'''
        DELETE FROM {TABLE_NAME2}
        WHERE id = ?
    ''', (id_departamento,))
    connection.commit()
    print(f'Departamento {id_departamento} deletado com sucesso!')


# FUNÇÕES DA TABELA CLIENTE
def inserirCliente(nome, email, telefone, cpf, idade, cidade, endereco, data_cadastro, departamento_id):
    try:
        cursor.execute(f'''
            INSERT INTO {TABLE_NAME1} (nome, email, telefone, cpf, idade, cidade, endereco, data_cadastro, departamento_id)
            VALUES (?,?,?,?,?,?,?,?,?)
        ''', (nome, email, telefone, cpf, idade, cidade, endereco, data_cadastro, departamento_id))
        connection.commit()
        print(f'Cliente {nome} cadastrado com sucesso!')
    except sqlite3.Error as erro:
        connection.rollback()  # desfaz alteração do meu bd
        print(f'Erro ao cadastrar cliente {nome}: {erro}')


def buscarClientes():
    cursor.execute(f'SELECT * FROM {TABLE_NAME1}')
    clientes = cursor.fetchall()
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
        WHERE id = ?
    ''', (nome, email, telefone, cpf, idade, cidade, endereco, data_cadastro, departamento_id, id_cliente))
    connection.commit()
    print(f'Cliente {id_cliente} atualizado com sucesso!')


def removerCliente(id_cliente):
    cursor.execute(f'''
        DELETE FROM {TABLE_NAME1}
        WHERE id = ?
    ''', (id_cliente,))
    connection.commit()
    print(f'Cliente {id_cliente} removido com sucesso!')


# FUNÇÕES COM JOIN
def buscarClientesComDepartamento():
    cursor.execute('''
        SELECT C.nome, D.nome
        FROM clientes C
        INNER JOIN departamento D ON D.id = C.departamento_id
    ''')
    resultados = cursor.fetchall()
    return resultados


def buscarClientesPorDepartamento(id_departamento):
    cursor.execute('''
        SELECT C.nome, D.nome
        FROM clientes C
        INNER JOIN departamento D ON D.id = C.departamento_id
        WHERE D.id = ?
    ''', (id_departamento,))
    resultados = cursor.fetchall()
    return resultados


def contarClientesPorDepartamento():
    cursor.execute('''
        SELECT D.nome, COUNT(C.id) AS total
        FROM departamento D
        LEFT JOIN clientes C ON C.departamento_id = D.id
        GROUP BY D.id, D.nome
    ''')
    resultados = cursor.fetchall()
    return resultados


def buscarDepartamentoMaisClientes():
    cursor.execute('''
        SELECT D.nome, COUNT(C.id) AS total
        FROM departamento D
        LEFT JOIN clientes C ON C.departamento_id = D.id
        GROUP BY D.nome, D.id
        ORDER BY total DESC
        LIMIT 1
    ''')
    resultado = cursor.fetchone()
    return resultado

def fecharConexao():
    return connection.close()
