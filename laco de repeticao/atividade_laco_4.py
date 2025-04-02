import os
import time

contador = 0
soma_salario = 0
maio_idade = 0
menor_idade = 9999
mulheres5k = 0

while True:
    print("""
codigo | descricao
   1   | Adicionar pessoa
   2   | exibir resultados
   3   | sair
""")

    opcao = int(input("Digite a opcao desejada: "))

    match opcao:
        case 1:
            idade = int(input("Digite sua idade: "))
            sexo = int(input("informe seu sexo - use 'M' OU 'F': "))
            salario = int(input("Digite seu salario: "))
            contador += 1 
            soma_salario += salario
            maior_idade = max(maior_idade, idade)
            menor_idade = min(menor_idade, idade)
            if sexo == "F" and salario >= 5000:
                mulheres5k += 1
        case 2:
            if contador > 0:
                media_salarial = soma_salario / contador
                print("\n= Exibindo resultados =")
                print(f"Media salarial do grupo: {media_salarial}")
                print(f"Maior de idade do grupo: {maior_idade}")
                print(f"Menor de idade do grupo: {menor_idade}")
                print(f"Quantidade de mulheres com salario a partir de 5k:{mulheres5k}: ")
            else:
                print("\entao foram informados os dados necessarios.")
            time.sleep(3)
            os.system("cls || clear")
        case 3:
                print("\n= fim =")
                break
        case _:  
                print("\nOpcao invalida.")
                time.sleep(3)
                os.system("cls || clear")




