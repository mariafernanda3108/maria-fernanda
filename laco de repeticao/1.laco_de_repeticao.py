import os

os.system("cls || clear")

numero = int(input("Digite um numero para tabuada :"))

for i in range(1,11):
    print(f"{numero} * {i} = {numero * i}")

    print("Fim da programa")