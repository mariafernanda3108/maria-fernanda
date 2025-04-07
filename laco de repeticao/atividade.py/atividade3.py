import os
os.system("cls || clear")

def par_ou_impar(numero):
    if numero % 2 == 0:
        print("numero par.")
    else:
        print("numero impar.")

print("= par ou impar =")
numero = int(input("Digite um numero:"))
par_ou_impar(numero)