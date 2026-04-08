# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']


import os
import json


def listar_tarefas(tarefas):
    print("TAREFAS:\n")
    if tarefas: #não sendo vázio
        for i, tarefa  in enumerate(tarefas, 1):
            print(f"{i}.{tarefa}")
    else:
        print("Nenhuma tarefa encontrada.")

def desfazer(tarefas, tarefas_desfeitas):
    if not tarefas: #não sendo vázia
        print("Nada a desfazer")
        return
    ultimo_elemento = tarefas.pop() #removendo último elemento
    tarefas_desfeitas.append(ultimo_elemento) #inserindo o último elemento no meu array de desfeitas

def refazer(tarefas, tarefas_desfeitas):
    if tarefas_desfeitas: #não sendo vázio
        tarefas.append(tarefas_desfeitas[-1]) #inserir o último do tarefas_desfeitas
        tarefas_desfeitas.pop() #removo o último do array
    else:
        print("Não foi possível desfazer: ")


def adicionar(tarefa, tarefas):
    print()
    if not tarefa: #existe alguma tarefa
        print("Não foi possível adicionar sua tarefa.")
        return
    
    tarefa = tarefa.strip()
    print(f"A tarefa {tarefa} foi adicionada com sucesso: ")
    tarefas.append(tarefa)
    print()


def ler(caminho_do_arquivo, tarefas):
    dados = []
    try:
        with open(caminho_do_arquivo, 'r', encoding= 'utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não existe')
        salvar(tarefas, caminho_do_arquivo) #se não existir, crio ele
    return dados

def salvar(tarefas, caminho_arquivo):
    dados = tarefas
    with open(caminho_arquivo, 'w', encoding= 'utf8') as arquivo:
            json.dump(tarefas, arquivo, indent = 2, ensure_ascii=False)
    return dados



CAMINHO_ARQUIVO = 'aula119.json'
tarefas = ler(CAMINHO_ARQUIVO, [])
tarefas_desfeitas = []
while True:
    print("Comandos: listar, desfazer, refazer")
    tarefa = input("Digite uma tarefa ou comando: ").lower().strip()

    if tarefa == 'listar':
        listar_tarefas(tarefas)
        continue
    elif tarefa == 'desfazer':
        desfazer(tarefas, tarefas_desfeitas)
        salvar(tarefas, CAMINHO_ARQUIVO)
        continue
    elif tarefa == 'refazer':
        refazer(tarefas, tarefas_desfeitas)
        salvar(tarefas, CAMINHO_ARQUIVO)
    elif tarefa == 'clear':
        os.system('cls' if os.name == 'nt' else 'clear')
        continue
    else:
        adicionar(tarefa, tarefas)
        listar_tarefas(tarefas)
        salvar(tarefas,CAMINHO_ARQUIVO) #adicionando no json
        continue    
