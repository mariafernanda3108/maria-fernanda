import os
os.system("cls || clear")

def aplicar_inflacao(preco):
    if preco < 100:
          resultado = preco *1.1
    else:
          resultado = preco*1.2
    return resultado
 
def descontar(preco):
    if preco < 100:
            resultado = preco * 0.1
    else:
        resultado = preco*0.2
    return resultado

preco_descontado = descontar(preco_produto)

preco_final =  preco_produto - preco_descontado

print(f"Valor descontado: {preco_final: .2f}")

preco_produto = float(input("Digite o preco do produto:"))

preco_inflacionado = inflacionar(preco_inflacionado)

print(f"Valor com aumento: {preco_inflacionado: 2f}")


