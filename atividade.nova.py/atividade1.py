import os
os.system("cls || clear") 
from attr import dataclass
nome: str
idade: int

@dataclass
class pessoa():
    nome: str
    idade: int
    
@dataclass
class pet():
    nome: str
    idade: int
    raca: str

pessoa1 = pessoa("Marta", 30)
pessoa2 = pessoa("josé", 40)

pet1 = pet("Toto", 4, "pastor-alemão")
pet2 = pet("Hulk", 6, "pitbull")

print("Dados da pessoa")
print(f"Nome da 1ª pessoa: {pessoa1.nome}\nidade: {pessoa1.idade}")
print(f"Nome da 2ª pessoa: {pessoa2.nome}\nidade: {pessoa2.idade}")

print("Dados do pet")
print(f"Nome do 1º pet: {pet1.nome}\nidade: {pet1.idade} \nraça: {pet1.raca}")
print(f"Nome do 2º pet: {pet2.nome}\nidade: {pet2.idade}\nraça: {pet2.raca}")

