#Heranca, Polimofismo

#heranca
class Animal: 
    def falor(self):
        print("Som generico")

class Cachorro(Animal): #cachorro herda de animal
    def falar(self):
        print('au au')

cachorro = Cachorro()
cachorro.falar()

#polimorfismo

class Gato:
    def falar(self):
        print('au')

class Leao:
    def falar(self):
        print("AUUUMMMMM")

#instanciando meus objetos
cat = Gato() 
leao = Leao()
cat.falar()
leao.falar()

#__str__

class Pessoa:
    def __init__(self, nome):
        self.nome = nome
    
    def __str__(self): #toString em java
        return f"Pessoa: {self.nome}"
    
pessoa = Pessoa('GUILHERME')
print(pessoa) #toda vez que eu for printar a pessoa, vai ser o método __str__()
