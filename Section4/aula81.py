# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.

lista = [
     {'nome': 'Luiz', 'sobrenome': 'miranda'},
     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
     {'nome': 'Daniel', 'sobrenome': 'Silva'},
     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
     {'nome': 'Aline', 'sobrenome': 'Souza'},
]
lista1 = [4, 32, 1, 34, 5, 6, 6, 21, ]
lista1.sort() #ordenar normal
lista1.sort(reverse=True) #ordenar inverso


def exibir(list):
    for item in list:
        print(item)
    print()


#ordenar um dicionário usando lambda
list3 = sorted(lista, key = lambda item: item['sobrenome']) #ordenei por sobrenome, usando lambda
list4= sorted(lista, key = lambda item: item['nome']) #ordenei por nome, usando lambda

exibir(list3)
exibir(list4)

