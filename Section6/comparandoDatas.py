from datetime import datetime, timedelta

fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('30/05/2005 09:15:10', fmt) #data inicial
data_fim = datetime.strptime('28/05/2026 11:20:05', fmt) #data final
delta = timedelta(days=10) #uma variavel com dez dias armazanados

data_soma = data_fim + delta #pego o data_fim e aumento dez dias
data_sub = data_fim - delta #pego o data_fim e diminuo dez dias
diferenca = data_fim - data_inicio #vai mostrar o total de dias e o restante de horas, minutos e etc

#print(diferenca)
#print(data_fim > data_inicio)
#print(data_fim == data_inicio)
#print(data_fim <= data_inicio)