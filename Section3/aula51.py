"""
Introdução ao empacotamento e desempacotamento
quero pegar o primeiro elemento e depois o segundo elemento de um array
"""

#pegar o primeiro
nome1, *_ = ["Maria", "Helena", "Luiz"]
print(nome1)

#pegar o segundo elemento
_,nome2, *_ = ["Maria", "Helena", "Luiz"]
print(nome2)

#pegar o terceiro elemento
_,_,nome3, *_ = ["Maria", "Helena", "Luiz"]
print(nome3)