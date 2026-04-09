#classes em py

class Pessoa:
    def __init__(self, nome, sobrenome): #construtor
        self.nome = nome #atributos da classe
        self.sobrenome = sobrenome

p1 = Pessoa('Guilherme', 'macario')
p2 = Pessoa('Valessa', 'Nascimento')

print(p1.nome)
print(p2.nome)


