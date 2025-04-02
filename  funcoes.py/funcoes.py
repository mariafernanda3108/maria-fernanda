import os

# funcao sem retorno
def logo_senai():
    os.system("clear")
    print("== SENAI ==")

logo_senai() # chamando a funcão
nome = input("Digite seu nome:")

logo_senai() # chamando a funcão
idade = int(input("Digite sua idade:"))

logo_senai() # chamando a funcão
print(f"Nome: {nome}")
print(f"Idade: {idade}")
