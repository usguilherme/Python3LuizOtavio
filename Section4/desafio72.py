# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplica(*args): #pode receber quantos argumento necessários
    total = 1
    for i in args:
        total *= i
    return total


# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def paridade(numero):
    try:
        mult_dois = numero % 2 == 0
        if (mult_dois):
            return f"O número {numero} é par"
        else:
            return f"O número {numero} é ímpar"
    except:
        return "Coloca um número real"

