import os

os.system("cls || clear")

print("numeros pares e impares:")
for i in range(5):
    numero = int(input("Digite um numero: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print()
print(f"pares: {pares}")
print(f"impares: {impares}")

print("\nFIM DO PROGRAMA")