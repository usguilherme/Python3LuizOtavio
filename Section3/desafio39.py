"""
Iterando strings com while, apenas modificando o nome
"""
        #
nome = "Luiz Otávio"
tamanho_nome = len(nome)
cont = 0
nova_string = ""
while cont <= tamanho_nome - 1:
    nova_string += f"*{nome[cont]}"
    cont += 1

print(nova_string)


