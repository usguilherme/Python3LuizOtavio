# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.
# def duplicar(numero):
#     return numero * 2

# def triplicar(numero):
#     return numero * 3

# def quadruplicar(numero):
#     return numero * 4

def multiplicador(multiplicador): #por quanto?
    def multiplicar(numero): #numero a ser multiplicado
        return numero * multiplicador
    return multiplicar 

duplicar = multiplicador(2)
triplicar = multiplicador(3)
quadruplicar = multiplicador(4)

resultado = duplicar(2)
print(resultado)

#tipo um empacotamento de funçoes


