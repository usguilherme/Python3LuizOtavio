#Recursividade em py

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

entrada = input("Digite seu número: ")
try:
    entrada_numero = int(entrada)
    resultado = fatorial(entrada_numero)
    print(resultado)
except ValueError as erro:
    print(f"Não é possível cadastrar valores sem ser um inteiro, {erro}")