import os
from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class pessoa():
    nome: str
    idade: int
    peso: float
    altura: float
    
    nome
    

pessoa1 = pessoa(nome=nome, idade=idade, peso=peso, altura=altura)
pessoa2 = pessoa(nome, idade, peso, altura)

print("Exibibindo dados ")
print(f"Nome: {pessoa1.nome}\nidade: {pessoa1.idade}\npeso: {pessoa1.peso}\naltura: {pessoa1.altura}")
print(f"Nome: {pessoa2.nome}\nidade: {pessoa2.idade}\npeso: {pessoa2.peso}\naltura: {pessoa2.altura}")