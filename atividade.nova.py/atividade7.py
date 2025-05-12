import os
from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class Endereco:
    def __init__(self, logradouro, numero, cidade, estado):
        self.logradouro = logradouro
        self.numero = numero
        self.cidade = cidade
        self.estado = estado

    def __str__(self):
        return f"{self.logradouro}, {self.numero}, {self.cidade} - {self.estado}"

class Aluno:
    def __init__(self, nome, data_nascimento, ra, curso, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.ra = ra
        self.curso = curso
        self.endereco = endereco

    def __str__(self):
        return f"Nome: {self.nome}\nData de Nascimento: {self.data_nascimento}\nRA: {self.ra}\nCurso: {self.curso}\nEndereço: {self.endereco}"

class SistemaAlunos:
    def __init__(self):
        self.alunos = []

    def cadastrar_aluno(self):
        print("\n--- Cadastrar Novo Aluno ---")
        nome = input("Nome do aluno: ")
        data_nascimento = input("Data de nascimento (DD/MM/AAAA): ")
        ra = input("Registro Acadêmico (RA): ")
        curso = input("Curso: ")

        print("\n--- Endereço ---")
        logradouro = input("Logradouro: ")
        numero = input("Número: ")
        cidade = input("Cidade: ")
        estado = input("Estado (UF): ")
        endereco = Endereco(logradouro, numero, cidade, estado)

        aluno = Aluno(nome, data_nascimento, ra, curso, endereco)
        self.alunos.append(aluno)
        print("\nAluno cadastrado com sucesso!")

    def listar_alunos(self):
        if not self.alunos:
            print("\nNenhum aluno cadastrado.")
            return
        print("\n--- Lista de Alunos ---")
        for aluno in self.alunos:
            print(aluno)
            print("-" * 20)

    def buscar_aluno(self, ra):
        for aluno in self.alunos:
            if aluno.ra == ra:
                return aluno
        return None

    def atualizar_aluno(self):
        ra_busca = input("Digite o RA do aluno que deseja atualizar: ")
        aluno_encontrado = self.buscar_aluno(ra_busca)

        if aluno_encontrado:
            print("\n--- Atualizar Dados do Aluno ---")
            aluno_encontrado.nome = input(f"Novo nome ({aluno_encontrado.nome}): ") or aluno_encontrado.nome
            aluno_encontrado.data_nascimento = input(f"Nova data de nascimento ({aluno_encontrado.data_nascimento}): ") or aluno_encontrado.data_nascimento
            aluno_encontrado.curso = input(f"Novo curso ({aluno_encontrado.curso}): ") or aluno_encontrado.curso

            print("\n--- Atualizar Endereço ---")
            aluno_encontrado.endereco.logradouro = input(f"Novo logradouro ({aluno_encontrado.endereco.logradouro}): ") or aluno_encontrado.endereco.logradouro
            aluno_encontrado.endereco.numero = input(f"Novo número ({aluno_encontrado.endereco.numero}): ") or aluno_encontrado.endereco.numero
            aluno_encontrado.endereco.cidade = input(f"Nova cidade ({aluno_encontrado.endereco.cidade}): ") or aluno_encontrado.endereco.cidade
            aluno_encontrado.endereco.estado = input(f"Novo estado ({aluno_encontrado.endereco.estado}): ") or aluno_encontrado.endereco.estado

            print("\nAluno atualizado com sucesso!")
        else:
            print("\nAluno não encontrado.")

    def deletar_aluno(self):
        ra_deletar = input("Digite o RA do aluno que deseja deletar: ")
        aluno_encontrado = self.buscar_aluno(ra_deletar)

        if aluno_encontrado:
            self.alunos.remove(aluno_encontrado)
            print("\nAluno deletado com sucesso!")
        else:
            print("\nAluno não encontrado.")

def exibir_menu():
    print("\n--- Menu do Sistema de Alunos ---")
    print("1. Cadastrar Aluno")
    print("2. Listar Alunos")
    print("3. Atualizar Aluno")
    print("4. Deletar Aluno")
    print("5. Sair")
    opcao = input("Escolha uma opção: ")
    return opcao

if __name__ == "__main__":
    sistema = SistemaAlunos()

    while True:
        opcao = exibir_menu()

        if opcao == '1':
            sistema.cadastrar_aluno()
        elif opcao == '2':
            sistema.listar_alunos()
        elif opcao == '3':
            sistema.atualizar_aluno()
        elif opcao == '4':
            sistema.deletar_aluno()
        elif opcao == '5':
            print("\nSaindo do sistema...")
            break
        else:
            print("\nOpção inválida. Tente novamente.")