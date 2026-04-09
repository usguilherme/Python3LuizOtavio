#method vs @classmethod vs @taticmethod

class Pessoa:
    #construtor
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
    
    #método, uso do objeto em si
    def mostrar_pessoa(self):
        return f'Pessoa: {self.nome}, Idade: {self.idade}, Endereco: {self.endereco}'

    @classmethod #uso da propria classe
    def contruir_sem_nome(cls, idade, endereco):
        return cls('Desconhecido', idade, endereco) #retorno a classe
    
    @staticmethod #não uso nem cls (classe), e nem self (objeto)
    def somar(x,y):
        return x + y
    
