"""
try - tento algo
except - caso der erro no try
finally - sempre vai acontecer 

"""
try: # tento
    print("Abrir o arquivo")
    10/0
except ZeroDivisionError as erro:
    print(f"Não é possível dividir um número por zero")
    print(erro)
finally: #sempre será executado
    print("Fechar arquivo")
