#shutil é mais utlizado para mover dados de um arquivo
#C:\Users\Guilherme\Pictures\Saved Pictures
#C:\Users\Guilherme\Documents\Nova pasta
import shutil
import os

origem = os.path.join('C:\\', 'Users','Guilherme', 'Pictures', 'Saved Pictures', 'p3.png')
destino = os.path.join('C:\\','Users','Guilherme','Documents', 'Nova pasta')

shutil.copy(origem, destino) #da origem para o destino
shutil.move('arquivo.txt', 'levandoarquivo.txt')

