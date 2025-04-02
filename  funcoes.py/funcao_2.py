import os

os.system("cls || clear") 

def calcular_media (primeira_nota, segundo_nota):
    soma = primeira_nota + segundo_nota
    media = soma / 2
    return media

primeiro_numero = int(input("Digite  o 1° numero:")) 
segundo_numero = int(input("Digite  o 2° numero:"))

media = calcular_media(primeiro_numero, segundo_numero)
print(f"Media: {media}")