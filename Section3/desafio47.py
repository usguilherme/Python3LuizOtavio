"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

import os


palavra_secreta = "guilherme"
letras_certas = ""
tentativas = 0
palavra_formada = ''
while True:
    tentativas += 1
    entrada = input("Digite sua letra: ").lower()

    if len(entrada) > 1:
        print("Digite alguma letra")
        continue

    if entrada in palavra_secreta:
        print("Voce acertou uma letra")
        cont = palavra_secreta.count(entrada)
        string_ok = entrada * cont #caso tenha duas ou mais letras na frase, já entra com a quantidade de repeticao
        letras_certas += string_ok

    if (len(letras_certas) == len(palavra_secreta)):
        for letra_secreta in palavra_secreta: #Apenas pra ficar atualizando o passo a passo
            if letra_secreta in letras_certas:
                palavra_formada += letra_secreta
    
    if (palavra_formada == palavra_secreta):
        print("Parabéns, voce Ganhou!")
        print(f"A palavra secreta era {palavra_secreta}")
        print(f"A palavra Que voce chegou foi {palavra_formada}")
        print(f"O número de tentativas foi de {tentativas}")
        