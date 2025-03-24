import os

os.system("cls || clear")

soma = 0

while True:
    print(""""
=====================MENU=====================
codigo  \tprato    \t\tvalor"
1   \t\tPicanha   \t\tR$ 25,00
2   \t\tLasanha    \t\tR$ 20,00
3   \t\tStrogonoff    \t\tR$ 18,00
4   \t\tBife acebolalado   \t\tR$ 15,00"
5   \t\tPao com ovo      \t\tR$ 5,00
""")
    opcao = int(input("Digite o numero da opcao desejada: "))
    match opcao:
        case 1:
            prato = "picanha"
            preco = 25
        case 2:
            prato = "lasanha"
            preco = 20
        case 3:
            prato = "strogonoff"
            preco = 18
        case 4:
            prato = "bife acebolado"
            preco = 15
        case 5:
            prato = "pao com ovo"
            preco = 5
        case _:
            prato = "opcao invalida"
            preco = 0

    soma += preco
    continuar = input("Deseja escolher outro prato? \nDigite 'S ou 'N: "). lower()
    if continuar == "n":
        break
    os.system("cls || clear")

print(f"\nTotal a pagar: R$ {soma}")


