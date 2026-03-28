"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

numero = input("Digite seu número: ")

try:
    numero_inteiro = int(numero)
    paridade = numero_inteiro % 2 == 0
    resultado = "impar"
    if (paridade): #par
        resultado = "par"
    print(f"O número {numero_inteiro} é {resultado}")
except:
    print("Você não digitou um número inteiro")

