"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
Uso do break e uso do continue
"""
contador = 0
while contador <= 100:
    contador += 1
    if contador == 6:
        continue #pular o número 6
    print(contador)

    if (contador == 38):
        break

