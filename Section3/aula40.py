""" Calculadora com while """
operacoes_permitados = "+-x.//" #não coloquei tres barras pra não dar erro no in da operacao
while True:
    numero1 = input("Digite seu primeiro número: ")
    numero2 = input("Digite seu segundo número: ")
    operacao = input("Digite sua operação: ")
    try:
        numero1_real = int(numero1)
        numero2_real = int(numero2)
        operacao in operacoes_permitados #verificar se tá entre os permidos
        if (operacao == "+"):
            resultado = numero1_real + numero2_real
        elif (operacao == "-"):
            resultado = numero1_real - numero2_real
        elif (operacao == "x" or operacao == "."):
            resultado = numero1_real * numero2_real
        elif (operacao == "%" or operacao == "/"):
            resultado = numero1_real / numero2_real
        elif (operacao == "//"):
            resultado = numero1_real // numero2_real
        print(f"O resultado de {numero1_real} {operacao} {numero2_real} = {resultado}")    
    except:
        print("Digite números válidos de entrada")


    sair = input("Deseja sair? [s]im ").lower().startswith('s') #colocando para minusculo e verificando se começa com s
    if sair is True:
        print("Programa encerrando... ")
        break