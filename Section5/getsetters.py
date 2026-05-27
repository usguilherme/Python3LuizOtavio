#atributo protegido
#getters e setters

class Conta:
    def __init__(self, saldo):
        self._saldo = saldo #protegido, pois usei o _
    
    def ver_saldo(self):
        return f"o seu saldo é {self.saldo}"

    def get_saldo(self): #getter
        return self._saldo
    
    def set_saldo(self, valor): #setter
        if valor >= 0:
            self._saldo = valor
    

    