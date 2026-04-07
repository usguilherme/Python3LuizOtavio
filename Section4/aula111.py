from functools import reduce


array = [1,2,3,4,5,6,7]
array_novos_valores = [x ** 2 for x in array]


#Usando função map, até com lambda, mapeando
resultado = map(lambda x: x ** 2, array)
#print(list(resultado))

#usando a funcao filter, estou filtrando meu interável
resultado1 = filter(lambda x: x % 2 == 0, array) #mostra apenas o números pares
print(list(resultado1))

#usando o reduce, reduzindo uma lista em um único valor
resultado2 = reduce(lambda x,y: x + y, array)
print(resultado2) #somatório de todos

resultado3 = reduce(lambda x,y: x * y, array)
print(resultado3) #multiplicação de todos

