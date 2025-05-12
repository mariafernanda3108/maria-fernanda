import os
from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class Funcionario:
    def __init__(self, nome, data_nascimento, cpf, funcao):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.funcao = funcao

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Data de Nascimento: {self.data_nascimento}")
        print(f"CPF: {self.cpf}")
        print(f"Função: {self.funcao}")
        print("-" * 20)

def cadastrar_funcionario():
    nome = input("Digite o nome do funcionário: ")
    data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")
    cpf = input("Digite o CPF: ")
    funcao = input("Digite a função: ")
    return Funcionario(nome, data_nascimento, cpf, funcao)

def exibir_todos_funcionarios(funcionarios):
    if not funcionarios:
        print("Nenhum funcionário cadastrado.")
        return
    print("\n--- Lista de Funcionários ---")
    for funcionario in funcionarios:
        funcionario.exibir_informacoes()

def main():
    funcionarios = []

    while True:
        print("\n--- Menu ---")
        print("1. Cadastrar Funcionário")
        print("2. Listar Funcionários")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            novo_funcionario = cadastrar_funcionario()
            funcionarios.append(novo_funcionario)
            print("Funcionário cadastrado com sucesso!")
        elif opcao == "2":
            exibir_todos_funcionarios(funcionarios)
        elif opcao == "3":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()