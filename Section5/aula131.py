#property

class Caneta:
    def __init__(self, cor):
        self._cor = cor #cor com _, deixando privado minha variável
    
    @property #fazendo um get com property, forma de acessar um método como se fosse um atributo
    def cor(self):
        return self._cor
    
    @cor.setter #usando como se fosse um atributo, meu método
    def cor(self, valor):
        self._cor = valor
    
can = Caneta('vermelho')
print(can.cor)
can.cor = 'laranja'
print(can.cor)
    