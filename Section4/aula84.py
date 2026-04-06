# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
# print(list(range(10)))

lista = []

for numero in range(10):
    lista.append(numero)

lista2 = [numero for numero in range(10)]
lista_par = [numero for numero in range(20) if numero % 2 == 0] 
lista_impar = [numero for numero in range(20) if numero % 2 != 0]

numeros = [1,2,3,4,5,6,7,8,9,10]
pares_maiores_que_5 = [numero for numero in numeros if numero % 2 == 0 if numero > 5]

numeros2 = [1,2,3,4,5]
resultado = ["PAR" if x % 2 == 0 else "ÍMPAR" for x in numeros2] #inserir com condição e depois for normal
print(resultado)

