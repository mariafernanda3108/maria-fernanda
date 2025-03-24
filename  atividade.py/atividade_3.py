import os

os.system("cls || clear")

soma = 0
contador = 1
while True:
    nota = float(input("Digite uma nota: "))
    resposta = input("Deseja inserir mais uma nota? \nDigite 'S' ou 'n'"). upper()
    if resposta == "N":
        break
    else:
        contador += 1
        soma = nota

media = soma / contador 

print(f"\nMedia: {media}")