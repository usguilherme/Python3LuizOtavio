
import json

dados_pessoais = {
    'nome': 'Guilherme',
    'idade': 21
}

tranformar_json = json.dumps(dados_pessoais) #converto um objeto python para uma string json
print(tranformar_json)
print(type(tranformar_json))

dados = '{"nome": "Guilherme", "idade": 20}'
dados = json.loads(dados) #tranformando uma sting json em objeto python
print(dados)