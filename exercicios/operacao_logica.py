import os
os.system("clear")

primeiro_numero = int(input("Digite um numero: "))                     
segundo_numero = int(input("Digite um numero: "))

if primeiro_numero > segundo_numero:
    maior = primeiro_numero
    menor = segundo_numero
else:
    maior = segundo_numero
    menor = primeiro_numero

