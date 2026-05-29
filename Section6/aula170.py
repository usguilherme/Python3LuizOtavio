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