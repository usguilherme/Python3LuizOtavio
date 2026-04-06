# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
# print(list(range(10)))

lista = []
for numero in range(10):
    lista.append(numero)
# print(lista)

            #expressao  #for normal 
lista2 = [numero for numero in range(10)]
print(lista2)
          #expressao  #for                   #condicao
lista_par = [numero for numero in range(20) if numero % 2 == 0] #lista com números pares
print(lista_par)

lista_impar = [numero for numero in range(20) if numero % 2 != 0]
print(lista_impar)
