#testando enum com exemplo de cores

from enum import Enum


class Cor(Enum):
    VERMELHO = "vermelho"
    AMARELO = "amarelo"
    AZUL = "azul"

cor = Cor.VERMELHO #criando o objeto enum posso escolher qualquer uma das cores para cirar o objeto

if cor == Cor.VERMELHO: #Verificando
    print("Pare 🚨")
elif cor == Cor.AMARELO:
    print("Pode seguir 🟢")
elif cor == Cor.AZUL:
    print("Cor azul 🔵")


class Semaforo(Enum):
    VERMELHO = "vermelho"
    AMARELO = "amarelo"
    VERDE = "verde"

entrada = input("DIGITE A COR: ").lower()
semaforo = Semaforo(entrada)
if semaforo == Semaforo.AMARELO:
    print("ok")
