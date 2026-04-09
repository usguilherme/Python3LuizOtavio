#public , private, protected

class Animal:
    def __init__(self, nome, raca, idade):
        self.nome = nome #publico, pode ser acessado em qualquer lugar, nenhum _
        self._raca = raca #protected, pode ser acessado, na classe a nas subclasses, _
        self.__idade = idade #privado, só pode ser acessado na propria classe, __