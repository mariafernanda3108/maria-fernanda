import os
from datetime import date
os.system("cls || clear")

def mediar(soma , quantidade_de_nota):
    return soma / quantidade_de_nota
soma = 0
quantidade_de_notas = 3

for i in range (quantidade_de_notas):
    nota = float(input(f"\nDigite {i+1}ª nota: "))
    soma += nota 

media = mediar(soma, quantidade_de_notas)
print(f"Media: {media: .2f}")