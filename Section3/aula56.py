"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""
frase = '   Olha só que   , coisa interessante          '
lista_frases_cruas = frase.split(',') #separa pela a virgula, colocando no array os elementos 

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip()) #strip remove os espaços do inicio e do fim

# print(lista_frases_cruas)
# print(lista_frases)
frases_unidas = ', '.join(lista_frases) #junta strings
print(frases_unidas)

frase_teste = "-".join(["guilherme", "valessa", "cassia", "isaias", "stephanye"]) #separador = -
print(frase_teste)