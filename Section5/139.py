#utilizaçõa do super em py

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def info(self):
        return f"Nome: {self.nome}, Idade: {self.idade} "

class Estudante(Pessoa): #herdando pessoa em estudante
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade) #chamando o construstor da minha classe Pessoa, classe Pai
        self.matricula = matricula
    
    def info(self):
        mensagem_pai = super().info() #chamar meu método info da classe Pai, ou seja, da classe Pessoa
        return mensagem_pai + f", Matrícula: {self.matricula}"


aluno = Estudante("Guilherme", 20, '122232131')
print(aluno.info())
