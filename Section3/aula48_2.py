"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3   4   5
lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])
lista.append(50) #Append sempre adiciona no final
lista.pop() #sempre removo no final
lista.append(60)
lista.append(70)
print(lista)
lista.insert(0,50) #inserir com o indice de parámetro
lista.insert(len(lista),90) #inserir com o indice de parámetro
ultimo_valor = lista.pop(3) #vai remover o índice 3
print(lista)
lista.clear()
print(lista) #limpando array

#concatenação de listas
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
print(lista_a)
