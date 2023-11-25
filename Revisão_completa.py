#Palíndrome
"""
def palindromo():
    nome = input("Digite seu nome:")
    if nome == nome[::-1]:
        print("É palíndromo")
    else:
        print("Não é palíndromo")

palindromo()
"""


"""
# Solicite ao usuário nome e sobrenome e retorne um usuário para login com as três primeiras letras do nome e as três primeiras letras do sobrenome.

def login():
    nome = input("Digite seu nome:")
    sobrenome = input("Digite seu sobrenome:")
    login = nome[0:3] + sobrenome [0:3]
    print("O seu nome de login é:", login)
login()

"""

#
"""
def lista_de_compras():
    lista = []
    fruta = input("Digite o nome da fruta  que deseja comprar ou 'sair' para sair:").lower()
    while fruta != "sair":
        lista.append(fruta)
        print(lista)
        fruta = input("Digite o nome da fruta que deseja comprar ou 'sair' para sair: ").lower()
    print(f"Lista de compras: \n {lista}")
lista_de_compras()

"""
# Faça um programa em que o usuário digita o raio de um círculo em m e o programa retorna no console a área do círculo em m2 e o perímetro em m

# Área do círculo = pi * raio
# Perímetro do círculo = 2 * pi * raio

import math

def area_do_circulo(raio):
    return math.pi * raio ** 2

def perimetro_do_circulo(raio):
    return 2 * math.pi * raio

def dados_do_circulo():
    raio = float(input("Digite o raio do círculo em metros: "))
    
    area = area_do_circulo(raio)
    perimetro = perimetro_do_circulo(raio)

    print(f"Raio: {raio} m")
    print(f"Área do círculo: {area:.2f} m²")
    print(f"Perímetro do círculo: {perimetro:.2f} m")

# Chamar a função para obter os dados do círculo
dados_do_circulo()


