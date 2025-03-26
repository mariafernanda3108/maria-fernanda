import os

os.system("cls || clear")

while True
    print("""
codigo | descricao
   1   |
   2   |
   3   |
""")

    opcao = int(input())
    
    match opcao:
        case 1:
            # solicite que a informe a idade.
            # solicite que a informe o sexo.
            # solicite que a informe o salario.
         case 2:   
            # mostre os resultados.
         case 3:   
            # pare.
         case _:  
            # opcao invalida.