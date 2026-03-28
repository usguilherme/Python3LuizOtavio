#Exercicio utilizando operadores de comparação, usando if/elif/else também, vê qual é maior ou menor

primeiro_valor = input("Digite seu valor: ")
segundo_valor = input("Digite seu valor: ")

if (primeiro_valor > segundo_valor):
    maior = primeiro_valor
    menor = segundo_valor
elif (primeiro_valor < segundo_valor):
    maior = segundo_valor
    menor = primeiro_valor

print(f"{maior} é o maior do que {menor}")
