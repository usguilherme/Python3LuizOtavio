#Acessando, removendo no dicionário

pessoa = {} #criando meu dicionário

#inserindo no dicionário
pessoa["nome"] = "Guilherme"
pessoa["sobrenome"] = "Macario"
print(pessoa)

#busca no dicionário
if pessoa.get("sobrenome"):
    print(f"Existe sim: {pessoa['sobrenome']}")
else:
    print("Não existe")

#remover no dicionário
del pessoa["sobrenome"] #apagando todos os valores de sobrenome
print(pessoa)