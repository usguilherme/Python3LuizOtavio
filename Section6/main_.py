#uso do __name__ == "__main__"

def multiplicar(n1, n2):
    return n1 * n2

if __name__ == "__main__":  #Se este arquivo estiver sendo executado diretamente (e não importado como módulo)
    print(multiplicar(10,5))
