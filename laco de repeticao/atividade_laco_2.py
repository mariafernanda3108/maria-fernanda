import os

os.system("cls || clear")

contador = 0
soma_pares = 0
soma_geral = 0
quantidade = 0

while True:
    numero = int(input(f"Digite o {contador + 1}º numero: "))
    
    if numero == 0:
        break
    
    if numero % 2 == 0:
       quantidade_pares += 1 
       soma_pares += numero
    else:
        quantidade_impares += 1
        
    contador += 1    
    soma_geral += numero

media_pares = soma_pares / quantidade_pares
media_geral = soma_geral / contador

print(f"\nQuantidade de pares: {quantidade_pares}")
print(f"Quantidade de impares: {quantidade_impares}")
print(f"\nMedia de pares: {media_pares}")
print(f"Media geral: {media_geral}")