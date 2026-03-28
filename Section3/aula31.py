"""
Atribuiçoes dos valor de None, is, is not, flags em geral
"""

controlador = None
condicao = True
if condicao:
    controlador = True
    print("Faça algo: ")
else:
    print("Não faça algo: ")

print(controlador, controlador is None) #verificando sé é none
print(controlador, controlador is not None) #verificando sé não é none