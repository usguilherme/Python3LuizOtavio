"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

entrada = input("Digite a hora atual em números inteiros: ")
try:
    hora = int(entrada)
    resultado_hora = ""
    if (0 <= hora <= 11):
        resultado_hora = "Bom dia"
    elif (12 <= hora <= 17):
        resultado_hora = "Boa tarde"
    elif (18 <= hora <= 23):
        resultado_hora = "Boa noite"
    else:
        resultado_hora = "Não conheço esse horário"

    print(resultado_hora)
except:
    print("Coloque um horário válido")
