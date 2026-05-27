# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

import json
#Minha classe
class Computador:
    def __init__(self, nome, processador, placa_mae, memoria_ram, fonte):
        self.nome = nome
        self.processador = processador
        self.placa_mae = placa_mae
        self.memoria_ram = memoria_ram
        self.fonte = fonte
    
    def ligar(self):
        return f'O computador {self.nome} está ligando...'
    
    def desligar(self):
        return f'O computador {self.nome} está desligando...'
    
    def toString(self):
        return f'Nome: {self.nome} :Processador: {self.processador} : Placa-Mãe: {self.placa_mae} : Memoria ram: {self.memoria_ram} : Fonte: {self.fonte}'
    
    def get_processador(self):
        return self.processador
    
    def get_nome(self):
        return self.nome
    
    def get_placa_mae(self):
        return self.placa_mae
    
    def get_memoria_ram(self):
        return self.memoria_ram
    
    def get_fonte(self):
        return self.fonte

def converter_variaveis_dicionario(array):
    dados = []
    for i in array:
        dados.append({
            'nome': i.nome,
            'processador': i.processador,
            'placa_mae': i.placa_mae,
            'memoria_ram': i.memoria_ram,
            'fonte': i.fonte,
        })
    return dados

def salvar(CAMINHO_ARQUIVO, lista):
    dados = lista
    with open(CAMINHO_ARQUIVO, 'w', encoding= 'utf8') as arquivo:
        json.dump(lista, arquivo, indent= 2, ensure_ascii= False)
    return dados

def ler(CAMINHO_ARQUIVO, lista):
    try:
        with open(CAMINHO_ARQUIVO, 'r', encoding= 'utf8') as arquivo:
            dados = json.load(arquivo) #apenas lendo o arquivo
            return dados
    except FileNotFoundError: #caso não houver o arquivo
        salvar(CAMINHO_ARQUIVO, lista)
        return lista

def recriar_objetos(lista_dicionario): #apenas recriando os objetos a partir do dicionário
    objetos = []
    for d in lista_dicionario:
        c = Computador(
            d['nome'], d['processador'], d['placa_mae'], d['memoria_ram'], d['fonte']
        )
        objetos.append(c)
    return objetos

computador1 = Computador("PC1", "i5", "Asus", "16GB", "500W")
computador2 = Computador("PC2", "Ryzen 7", "Gigabyte", "32GB", "650W")
lista = [computador1, computador2] #coloquei em uma lista
lista_dicionario = converter_variaveis_dicionario(lista)
salvar('aula127.json', lista_dicionario)



    




