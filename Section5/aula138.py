#Herança simples - Relaçoes entre classes
#Assisiação - usa,
# Agregação - o objeto tem o outro objeto
#Composição - É dono de

class Pessoa:
    cpf = '122333'

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Cliente(Pessoa): #herdando pessoa
    ...


class Aluno(Pessoa): #herdando pessoa
    ...

c1 = Cliente('Luiz', 'Otávio')
c1.falar_nome_classe()
a1 = Aluno('Maria', 'teste')
a1.falar_nome_classe()
print(a1.cpf)




