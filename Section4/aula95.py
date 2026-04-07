#raise - lancando exceçoes (erros)

try:
    x = int("abc")
except ValueError:
    print("Erro aconteceu") #primeiro mostro a mensagem
    raise #mostro o erro, não deixo ele passar despercebido

try:
    x = int("cdb")
except ValueError:
    raise ValueError("Erro em: converter Strings para int") #sobreescrevi meu erro, podendo até criar um novo

