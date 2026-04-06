#usando funcao lambda comparando com def
#lambda argumentos: expressão

soma = lambda x, y: x + y # funcao lambda, onde tenho x e y, e "retorno" x + y
print(soma(2,5))

numeros = [1,2,3,4,5,6,7,8]
pares = filter(lambda x: x % 2 == 0, numeros)
print(list(pares))

