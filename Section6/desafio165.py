# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela

from datetime import datetime
from dateutil.relativedelta import relativedelta

valor_emprestimo = 1_000_000
data_emprestino = datetime(2026, 5, 29)
cinco_anos = relativedelta(years = 5) #variavel que armazena cinco anos
data_final = data_emprestino + cinco_anos

parcelas = [] #minha lista de parcelas a se pagar
data_parcela_inicial = data_emprestino
while data_parcela_inicial < data_final:
    parcelas.append(data_parcela_inicial) 
    data_parcela_inicial += relativedelta(months = 1) #aumentnado um mês na parcela

numero_parcelas = len(parcelas)
valor_parcela = valor_emprestimo / numero_parcelas

for data in parcelas:
    print(data.strftime('%d/%m/%Y'), f'RS{valor_parcela:.2f}')

print()
print(
    f'Voce pagou RS {valor_emprestimo:.2f} para pagar '
    f'em {cinco_anos.years} anos'
    f'{numero_parcelas} meses, de parcelas de '
    f'{valor_parcela:.2f}.'
)



