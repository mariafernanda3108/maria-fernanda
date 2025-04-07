import os
os.system("cls || clear")

def positivo_negativo(numero):
    if numero % 2 == 0:
        print("numero negativo.")
    else:
        print("numero positivo.")

print("= POSITIVO ou NEGATIVO  =")
numero = int(input("Digite um numero:"))
positivo_negativo(numero)