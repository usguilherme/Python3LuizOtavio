#Calculo IMC, e já formatando strings

nome = "Guilherme"
altura = 1.91
peso = 82
imc = 0.0
imc_certo = peso / (altura ** 2)

print(f"{nome} tem {altura} de altura")
print(f"pesa {peso} quilos e seu IMC é") 
print(f"{imc_certo:.2f}")  #Apenas já colocando com duas casas decimais
