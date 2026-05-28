from abc import ABC, abstractmethod


class Pessoa(ABC): #classe abstrata
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade
    
    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade

class Cliente(Pessoa): #herda da classe pessoa
    def __init__(self, nome, idade, conta):
        super().__init__(nome, idade) #chamando o construtor da classe pai
        self._conta = conta

    @property
    def conta(self):
        return self._conta

class Conta(ABC): #classe abstrata
    def __init__(self, agencia, numero, saldo = 0):
        self._agencia = agencia
        self._numero = numero
        self._saldo = saldo
    
    def depositar(self, valor):
        self._saldo += valor
    
    @abstractmethod
    def sacar(self, valor): #toda classe filha tem que ter esse método
        pass

    @property
    def agencia(self):
        return self._agencia

class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self._saldo >= valor: #se meu saldo for maior ou igual o meu valor, diminui
            self._saldo -= valor

class ContaCorrente(Conta):
    def __init__(self, agencia, numero, saldo = 0, limite = 0):
        super().__init__(agencia, numero, saldo) #chamei o construtor da classe pai
        self._limite = limite
    
    def sacar(self, valor):
        if self._saldo + self._limite >= valor: #pra reduzir, tenho que verificar se o saldo é menor ou igual a o que posso gastar
            self._saldo -= valor

class Banco:
    def __init__(self):
        self._agencias = []
        self._clientes = []
        self._contas = []
    
    def adicionar_cliente(self, cliente):
        self._clientes.append(cliente)
    
    def adicionar_agencia(self, agencia):
        self._agencias.append(agencia)
    
    def adicionar_conta(self, conta):
        self._contas.append(conta)
    
    def autenticar(self, cliente):
        if cliente not in self._clientes:
            return False
        if cliente.conta not in self._contas:
            return False
        if cliente.conta.agencia not in self._agencias:
            return False

        return True



