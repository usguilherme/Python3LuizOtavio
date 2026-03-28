"""
Fatiamente de Strings
    012345678
    Olá Mundo
-   987654321
Fatiamente [inicio: fim: passo]
Função len
"""

variavel = "Olá Mundo"
print(variavel[2: 8]) #vai dá letra á até o D
print(variavel[2: 9]) #vai dá letra á até o O
print(variavel[0: 5]) #vai dá letra O até o M
print(variavel[2:len(variavel)]) #vai do á até o final
print(variavel[0:len(variavel)]) #toda a palavra
print(variavel[0:len(variavel): 2]) #pulando de dois em dois passos
print(variavel[-1: -10: -1]) #vai inverter
print(variavel[::-1]) #vai inverter também