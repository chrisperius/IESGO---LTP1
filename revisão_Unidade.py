# Exemplo 1 - Programa com manipulação de tipos de dados

# Solicitar ao usuário que insira informações
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
casado = input("Você é casado? (sim/não): ").lower() == "sim"
cores_favoritas = input("Digite suas cores favoritas separadas por vírgulas: ").split(',')
comida_favorita = input("Digite sua comida preferida: ")

# Criar um programa que armazene o valor dos produtos e a quantidade, entregando o subtotal

def preco_do_produto():
    valor_unitario_prod1 = float(input("Digite o valor do produto: "))
    qnt_produto_1 = int(input("Digite a quantidade de unidades do produto: "))
    subtotal = valor_unitario_prod1 * qnt_produto_1
    print(f"Subtotal: R${subtotal:.2f}")
preco_do_produto()
