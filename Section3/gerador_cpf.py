"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""


#retirando os . e -
cpf_inicial = "746.824.890-70"
cpf_numeros = ""
for letra in cpf_inicial:
    if letra.isdigit():
        cpf_numeros += letra

#resolvendo o somatório de todas as multiplicaçoes
soma = 0
for i, num in enumerate(range(10,1,-1)): #quero pegar o indice e o valor, i = indice, num é o valor
    soma += int(cpf_numeros[i]) * num

soma *= 10
soma %= 11
soma = 0 if soma > 9 else soma #se soma > 9 é = 0, caso contrario soma é soma


