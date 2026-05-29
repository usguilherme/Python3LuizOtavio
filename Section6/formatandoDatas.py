#usando o datatime.strftime()

#criar uma data normal, usando o strptime(data, formato)
from datetime import datetime


fmt = '%d-%m-%Y %H:%M:%S'
data = datetime.strptime('29-05-2026 10:35:10', fmt)
print(data) #data normal
print(data.year)

#FORMATANDO ESSA DATA, usando o strftime()
data_mod = data.strftime('%Y/%m/%d') #formando minha string data
data_mod2 = data.strftime('%Y/%m/%d %H--%M--%S') #formando minha string data
print(data_mod) #2026/05/29
print(data_mod2) #2026/05/29  