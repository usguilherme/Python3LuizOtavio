class Pessoa:
    ano = 2023
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    @classmethod
    def metodo_de_classe(cls):
        print('hey')
    
    @classmethod
    def criar_com_50_anos(cls, nome): #cls é a classe
        return cls(nome, 50) #sempre iniciando com 50 anos
    
    @classmethod #criando objeto sem nome
    def criar_sem_nome(cls, idade):
        return cls('Anonima', 23)

p1 = Pessoa("Guilherme", 20)
p2 = Pessoa.criar_com_50_anos("Valessa")
p3 = Pessoa.criar_sem_nome(30)

print(p2.nome, p2.idade) 
print(p3.idade)
