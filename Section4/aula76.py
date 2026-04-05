"""
Criando um dicionário em py
chave : valor,
"""

pessoa = {
    "nome" : "Guilherme",
    "sobrenome": "Macario",
    "idade": 20,
    "altura": 1.91,
    "endereco": [
        {"rua" : "rua de Deus", "numero" : 567},
        {"rua" : "rua de jesus", "numero" : 145},
    ],
}

print(pessoa["nome"], pessoa["idade"])

for endereco in pessoa["endereco"]: 
    print(endereco["rua"]) #pegando apenas as ruas

