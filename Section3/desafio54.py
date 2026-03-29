"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
lista = []
while True:
    entrada = input("[i]inserir [a]pagar [l]istar, [s]air ").lower()
    if (entrada == "i"): #inserir
        entrada_ins = input("Valor:")
        lista.append(entrada_ins) #inseir o elemento na lista
        print(f"O elemento {entrada_ins} foi inserido em sua lista")

    elif (entrada == "a"):
        entrada_ins = input("Digite qual índice deseja remover:")
        try:
            entrada_ins_real = int(entrada_ins)
            if (entrada_ins_real < len(lista)): #dentro do intervalo do array
                print(f"O elemento {lista[entrada_ins_real]} foi removido de sua lista")
                lista.pop(entrada_ins_real) #remover o indice correto
            else:
                print("Digite um indice que esteja no array")
        except TypeError:
            print("Digite um número inteiro")

    elif (entrada == "l"):
        for item, valor in enumerate(lista):
            print(item, valor)
            
    elif (entrada == "s"):
        break




