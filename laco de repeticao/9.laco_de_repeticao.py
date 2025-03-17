import os

os.system("cls || clear")

soma = 0

print("Notas")
for i in range(4):
    nota = float(input("Digite uma nota: "))
    soma + nota

media =  soma / 4

print()
print(f"media: {media}")

print("FIM DA PROGRAMACAO")