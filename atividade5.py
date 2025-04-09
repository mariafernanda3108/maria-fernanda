import os
os.system("cls || clear")

def juntar(nome, sobrenome):
    return nome + sobrenome

nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")

nome_completo = juntar(nome, sobrenome)

print(f"Nome completo: {nome_completo}")