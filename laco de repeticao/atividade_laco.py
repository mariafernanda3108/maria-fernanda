import os

os.system("cls || clear")

contador = 0
soma = 0

while True:
    nota = int(input(f"digite o {contador + 1 } numero: "))

    if nota <0:
        break
    else:
        contador += 1
        soma += nota

media = soma / contador

print(f"media: {media}:")
    