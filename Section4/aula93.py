# (Parte1) try e except para tratar exceções

try:
    a = 18
    b = 0
    c = a / b
except ZeroDivisionError as a : #erro de dividir por zero, a vai ser o erro
    print("ERRO: não é possível dividir por zero", end = " ")
    print(a)
except NameError as b : #variável não definida, b vai ser o erro
    print("Não foi possível achar uma de suas variáveis", end = " ")
    print(b)
