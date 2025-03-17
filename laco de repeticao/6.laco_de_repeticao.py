import os

os.system("cls || clear")

print("somando numeros:")
soma = 0
for i in range(3):
    nota = float(input(f"Digite a {i+1}nota: "))
    soma =  soma + nota

print(f"soma: {soma}")

print("FIM DO PROGRAMA")