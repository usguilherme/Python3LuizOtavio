#escopo da classe e do métodos da classe
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def comendo(self, alimento):
        return(f"{self.nome} está comendo um {alimento}")
    
    def executar(self, *args):
        return self.comendo(*args) #chama outro método, por conta do self, se não tivesse não iria chamar

leao = Animal("leao")
print(leao.executar('maça'))
