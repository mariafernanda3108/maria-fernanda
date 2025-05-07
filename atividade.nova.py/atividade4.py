import os
from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class dados():
    nome: str
    data_nascimento: str
    rg: str
    cpf: float

nome = input("digite seu nome:")
data_nascimento = input("digite sua data nascimento:")
rg = input("digite seu rg:")
cpf = input("digite seu cpf")


