#uso do super em python

class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def falar(self):
        print("Som generico")

class Cachorro(Animal): #heranca
    def __init__(self, nome, raca):
        super().__init__(nome) #estou chamando o construtor da classe pai
        self.raca = raca
    
    def falar(self):
        super().falar() #chamo o método da classe pai, falar
    
cachorro = Cachorro('Aurora', 'Maltes')
cachorro.falar()