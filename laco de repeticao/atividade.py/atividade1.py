import os

os.system("cls || clear")

def saudacao(parametro):
    print(f"Ola, {parametro}: Bem-vindo(a) ao nosso site.")

nome_visitante = input("Digite seu nome: ")
saudacao(nome_visitante)