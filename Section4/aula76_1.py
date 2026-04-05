pessoa = {
    'nome': 'Guilherme',
    'sobrenome': 'Macario',
}

tamanho_dicionario = len(pessoa)
chaves = list(pessoa.keys()) #apenas convertendo para list
valores = list(pessoa.values())
chave_valor = list(pessoa.items())
pessoa.setdefault('idade', 30) #adicionando chaves e valores inexistentes

print(pessoa)

pessoa2 = pessoa.copy() #copiando um dicionário
