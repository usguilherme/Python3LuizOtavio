# uso do property

#sem property

class Animal:
    def __init__(self, nome):
        self._nome = nome
    
    def get_nome(self): #getter normal
        return self._nome

#usando o property

class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade
    
    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade

#sem o property
animal = Animal('Leão')
print(animal.get_nome())

#usando o property, eu consigo chamar o atributo privado, usando a funcao
pessoa = Pessoa('Guilherme', 20)
print(pessoa.nome)
print(pessoa.idade)