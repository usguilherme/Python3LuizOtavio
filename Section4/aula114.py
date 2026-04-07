#Recursividade em py

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

#entrada = input("Digite seu número: ")
#try:
    #entrada_numero = int(entrada)
    #resultado = fatorial(entrada_numero)
    #print(resultado)
#except ValueError as erro:
    #print(f"Não é possível cadastrar valores sem ser um inteiro, {erro}")

def soma_n_numeros(numero):
    if numero == 0:
        return 0
    return numero + soma_n_numeros(numero - 1)

def potencia(base, exp): 
    if exp == 0:
        return 1
    return base * potencia(base, exp - 1)

"""
2 * primeira chamada
2 * 2   segunda chamada
2 * 2 * 2 terceira chaamda
2 * 2 * 2 * 1 quarta chamada
"""
resultado_quero = potencia(2,3)
print(resultado_quero)

