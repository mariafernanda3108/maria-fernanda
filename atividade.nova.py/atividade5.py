import os
os.system("cls ||clear")
from dataclasses import dataclass


@dataclass
class funcionario():
        nome: str
        data_admissao: int  
        matricula: int
        endereco: str
@dataclass
class cliente():
        nome: str
        data_nacimento: int  
        endereco: str
    
    QUANTIDADE_F = 3
    QUANTIDADE = 3
    listagem = []
    listagem_f = [] 
    
for i in range(QUANTIDADE):
   print(f"\t= socilicitando dados do cliente =") 
   cliente = cliente( 
         nome = input("Digite seu nome:"),
         data_nacimento = int(input("Digite sua data de nascimento:")),
         endereco = input("Digite seu endereco:")          
        )             
        
    listagem.append(cliente)                   
                     
for i in range(QUANTIDADE_F)                  
   print(f"\t= socilicitando dados do funcionario =") 
   funcionario = funcionario( 
         nome = input("Digite o nome do funcionario:"),
         data_admissao = input("Digite a data de admissao do funcionario:"),
         matricula = input("Digite a matricula do funcionario:"),
         endereco = input("Digite o endereco do funcionario:")                            
        )            
    listagem_f.append(funcionario)
    
        nome_arquivo = "clientes.txt"
        with open(nome_arquivo, "a", enconding="utf-8") as arquivo_clientes:  
    for cliente in listagem:
        arquivo_clientes.write(f"nome do cliente: {cliente.nome}\ndata de nascimento: {cliente.data_nacimento}\nEndereco: {cliente.endereco")
        print("\t\nSalvando . . .")
try:    
    with open(nome_arquivo, "r", enconding="utf-8") as arquivo::  
    linhas = arquivo.readlines()
    for linha in linhas:
    print(linha)
except FileNotFoundError:
    print("Arquivo não encontrado.")
    
nome_arquivo = "funcionarios.txt"
with open(nome_arquivo, "a", enconding="utf-8") as arquivo_funcionarios: 
    for funcionario in listagem_f:
        arquivo_funcionarios.write(f"nome do funcionario: {funcionario.nome}\ndata de admissao: {funcionario.data_admissao}\nmatricula: {funcionario.matricula}\nEndereco: {funcionario.endereco}")
        print("\t\nSalvando . . .")
try:   
    with open(nome_arquivo, "r", enconding="utf-8") as arquivo: 
    linhas = arquivo.readlines()
    for linha in linhas:
            print(f"{linha.strip()}")
                  
except FileNotFoundError:
    print("Arquivo não encontrado:")    
    
    print(f"\n"Dados salvos com sucesso")