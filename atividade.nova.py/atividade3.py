import os
from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class pessoa():
    nome: str
    email: str
    telefone: int
    endereco: str

nome = input("Digite seu nome: ")
email = input("Digite se email: ")
telefone = input("Digite seu telefone: ")
endereco = input("Digite seu endereco: ")

pessoal1 = pessoa(nome=nome, email=email, telefone=telefone, endereco=endereco)

print("\nExibindo dados: ")
print(f"\nNome: {pessoal1.nome}\nemail: {pessoal1.email}\ntelefone : {pessoal1.telefone}\nendereco: {pessoal1.endereco}")
