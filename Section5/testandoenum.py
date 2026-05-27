#quando utilizar ENUM
#utilizo quando tenhos formas limitas e fixas, representando estados, tipo ou categoria
#ou seja, ENUM = só pode ser uma dessas aqui
from enum import Enum


class StatusPedido(Enum): #vai representar o estado PENDENTE de forma segura e padronizada
    PENDENTE = "pendente"
    PAGO = "pago"
    CANCELADO = "cancelado"


statuspedido = StatusPedido.PENDENTE #vai virar minha constante pendente
print(statuspedido.value) #printa o valor da minha constante

