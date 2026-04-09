class Carro:
    def __init__(self, nome, modelo):
        self.nome = nome
        self.modelo = modelo
    
    def acelerar(self): #método
        print(f"O carro {self.nome} está acelerando...")
    
fusca = Carro('Fusca', 'volkswagem') #instanciando objeto
onix = Carro('onix', 'chevrolet')

fusca.acelerar() #chamando método
onix.acelerar()
