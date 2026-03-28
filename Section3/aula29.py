"""
Introdução ao try/except
try - tenta executar o código
except - ocrreu algum erro ao tentar executar
tratando erros e excessoes
"""

numero = input("Digite um número que vou dobrar ele: ")

try:
    numero_real = float(numero)
    print(f'o dobro de {numero_real} é {numero_real * 2:.2f}')
except:
    print(f"Erro no seu número digitado")

