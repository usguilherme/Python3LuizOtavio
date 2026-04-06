#usando funcao lambda comparando com def
#lambda argumentos: expressão

soma = lambda x, y: x + y # funcao lambda, onde tenho x e y, e "retorno" x + y
#print(soma(2,5))

numeros = [1,2,3,4,5,6,7,8]
pares = filter(lambda x: x % 2 == 0, numeros)
print(list(pares))

#ordenar um array usando lambda
numeros2 = [10,3218,1,5,4,31231,323]
ordenado = sorted(numeros2, key = lambda x: x)
print(ordenado)

pessoas = [("João", 25), ("Maria", 20), ("Ana", 30)] #ordenar pela a idade deles

pessoas_ordenadas = sorted(pessoas, key = lambda x: x[1]) #lambda argumentos: regra a ser ordenado
print(pessoas_ordenadas)

pessoas_ordenadas_contrario = sorted(pessoas, key = lambda x: x[1], reverse= True) #lambda argumentos: regra a ser ordenado, reverso
print(pessoas_ordenadas_contrario) #decrescente






