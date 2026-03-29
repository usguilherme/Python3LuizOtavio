"""
Descobrir qual letra da frase foi mais usada
"""

frase = 'aaaooookkkkkk'
letra_mais_repetida = ""
vezes_maior = 0
i = 0
while i < len(frase):
    letra_atual = frase[i]
    qnt_vezes_apareceu_atual = frase.count(letra_atual) #contar quantas vezes apareceu
    if (letra_atual == " "):
        i+=1
        continue
    
    if (qnt_vezes_apareceu_atual > vezes_maior):
        vezes_maior = qnt_vezes_apareceu_atual
        letra_mais_repetida = letra_atual
    
    i+=1

print(f"A letra mais usada na frase foi {letra_mais_repetida}")