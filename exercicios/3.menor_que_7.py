import os
os.system("clear")

primeiro_numero = int(input("Digite o primeiro numero: "))
segundo_numero = int(input("Digite o segundo numero: "))

media = (primeiro_numero + segundo_numero) / 2

produto = (primeiro_numero * segundo_numero)

if primeiro_numero < segundo_numero:
    menor = primeiro_numero
    maior = segundo_numero
else:
    menor = segundo_numero
    maior = primeiro_numero

print(f"media: {media}")
print(f"produto: {produto}")