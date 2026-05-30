#C:\Riot Games\League of Legends\Saved\webcache
#C:\Users\Guilherme\Documents\Valessa

import os
caminho = os.path.join('C:\\','Riot Games','League of Legends','Saved', 'webcache' ) #deixando o caminho correto
caminho2 = os.path.join('C:\\', 'Users', 'Guilherme', 'Documents', 'Valessa')
print(caminho2)

#listar os diretorios do caminho
for item in os.listdir(caminho):
    print(item)

for raiz, pastas, arquivos in os.walk(caminho2):
    print(raiz,pastas,arquivos)

#criando uma pasta
os.mkdir('NovaPasta')
os.makedirs('Projetos/Python/Teste') #crio várias pastas

#remover uma pasta
os.rmdir('NovaPasta') #removo uma pasta
os.remove('arquivo.txt') #removo um arquivo
os.rename('arquivo.txt', 'novo_arquivo.txt') #primeiro o nome que é, depois o que vai ficar

#percorres subpastas
for raiz, pasta, arquivo in os.walk(caminho2):
    print(raiz)
    print(pasta)
    print(arquivo)
