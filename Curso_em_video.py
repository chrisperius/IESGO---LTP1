# Treino de python com curso em vídeo e aula.
"""
dia = input("Digite o dia que você nasceu!")
mes = input("Digite o mês que você nasceu!")
ano = input("Digite o ano que você nasceu!")
print("Você nasceu no dia ", dia, "de", mes, "de", ano, ".")


resposta = input("Correto?")
if resposta == "sim":
    print("Ok")
else:
    print("Ops, ocorreu um erro!")


"""
# Teste 2

"""
num1 = int(input("Digite um número"))
num2 = int(input("Digite outro número"))
s = num1+num2
print('A soma vale', s)
"""


#Outra tarefa
"""
nome = input("Digite seu nome")
print('É um prazer te conhecer, {}!' .format(nome))

"""

"""
n1 = int(input('Digite um número:'))
n2 = int(input('Digite mais um número'))
s = n1+n2
print('A soma vale{}' .format(s))
"""


#___________________________________________________________________________________________________
#___________________________________________________________________________________________________



# Exercício 1: Faça uma função que recebe um número e retorna True se ele é múltiplo de 5 ou False caso contrário.

# Operador representado pelo símbolo de porcentagem (%), que retorna o resto da divisão entre dois números. Exemplo: 5 % 2 = 1.

# Um número será múltiplo de 5 se o resto da divisão dele por 5 for igual a 0.


"""
def multiplo_de_5(numero):
    if numero % 5 == 0:
        return True
    else:
        return False

print(multiplo_de_5(int(input("Digite um número: "))))
"""


# Exercício 1 apenas com duas linhas

"""
numero = int(input("Digite um número inteiro: "))
print(f"True" if numero % 5 == 0 else f"False")
"""

# Exercício 2: Faça uma função que recebe um número e imprime no console se ele é múltiplo de 5 e de 3 ou False caso contrário.

"""
def multiplo_de_5(numero):
    if numero % 5 == 0:
        return True
    else:
        return False

def multiplo_de_3(numero):
    if numero % 3 == 0:
        return True
    else:
        return False

def multiplo_de_5_e_3(numero):
    if multiplo_de_5(numero) and multiplo_de_3(numero):
        return True
    else:
        return False
    
numero = int(input("Digite um número: "))
print(multiplo_de_5_e_3(numero))
"""

# Exercício 3: Crie um programa em que o usuário insira uma palavra e o programa retorna se a palavra é palíndromo ou não.

"""
def palindromo():
    nome = input("Digite um nome: ")
    if nome == nome[::-1]:
        print(" É um palíndromo ")
    else:
        print("Não é um palíndromo")
palindromo()
"""

# Exercicio 4: Faça um programa que solicita ao usuário escrever o nome das frutas que ele deseja comprar. O usuário deve digitar as frutas até digitar a palavra "sair". O programa deve imprimir na tela a lista de frutas que o usuário deseja comprar.


"""
def lista_de_compras():
    lista = []
    fruta = input("Digite a fruta que você deseja ou digite 'sair' para sair: ").lower()
    while fruta != "sair":
        lista.append(fruta)
        print(lista)
        fruta = input("Digite a fruta que você deseja ou digite 'sair' para sair: ").lower()
    print(f"Lista de compras: \n {lista}")
    return lista         
lista_de_compras()
"""



# Exercício 5: Faça um programa em que o usuário digita o raio de um círculo em m e o programa retorna no console a área do círculo em m² e o perímetro em m.
"""
import math

# Área do cículo = pi * raio²
# Perímetro do círculo = 2 * pi * raio

def area_do_circulo(raio):
    return math.pi * raio ** 2

def perimetro_do_circulo(raio):
    return 2 * math.pi * raio

def dados_do_circulo():
    try:
        raio = float(input("Digite o raio do círculo em m: "))
        print("raio: ", raio)
        print(f"Área do círculo: {area_do_circulo(raio)} m²")
        print(f"Perímetro do círculo: {perimetro_do_circulo(raio)} m")
    except ValueError:
        print("O valor inserido não é um número.")
        dados_do_circulo()
    

dados_do_circulo()
"""
#complemento do Exercício 5

"""
import math

raio = float(input("Digite o raio do círculo em metros: "))

area = math.pi * raio ** 2

perimetro = 2 * math.pi 
5
print(f"A área do círculo é {area:.2f} m²")
print(f"O perímetro do círculo é {perimetro:.2f} m")
"""

# Exercício 6: Faça um programa que solicita o ano de nascimento do usuário e retorna o seu signo no horóscopo chinês.
"""

#### Dica: Para descobrir o seu signo no horóscopo chinês, você precisará conhecer o ano do seu nascimento de acordo com o calendário chinês. O horóscopo chinês é baseado em um ciclo de 12 anos, cada ano representado por um animal do zodíaco chinês. Aqui estão os 12 animais do zodíaco chinês e os anos correspondentes:


def signo_chines(ano):
    signo_chines = ["Rato", "Boi", "Tigre", "Coelho", "Dragão", "Serpente", "Cavalo", "Cabra", "Macaco", "Galo", "Cão", "Porco"]
    calculo = (ano - 1900) % 12
    return signo_chines[calculo]

print(signo_chines(int(input("Digite o ano de nascimento:"))))
"""

# Exercício 7: Faça um programa que solicita ao usuário inserir um número inteiro e retorna se ele é primo.
"""

# Um número é primo quando é divisível apenas por 1 e por ele mesmo. Por exemplo, 2, 3, 5 e 7 são números primos, mas 4, 6, 8 e 9 não são.

def eh_primo(numero):
    if numero <= 1:
        return False
    elif numero <= 3:
        return True
    else:
        for num in range(2, numero):
            if numero % num == 0:
                return False
        return True
    
numero = int(input("Digite um número inteiro: ")) 
print(eh_primo(numero))
"""
# Exercício 8: Faça um programa que solicita ao usuario inserir um email e retorna se ele é válido ou não.
"""
import re 

email_do_usuario = input("Digite seu email: ")

def email_valido(email):
    if "@" in email:    
        return True
    else:
        return False

print(email_valido(email_do_usuario))
# Usando regex:

def checagem_de_email(email):
    padrao = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    resultado = padrao.search(email)
    return resultado != None
"""


# Exercício 9: Usando o método random(), crie um programa que solicita ao usuário que adivinhe um número inteiro entre 1 e 10 (contando o 10). Se o usuário digitar um número menor que 1 ou maior que 10, solicite que ele insira um número válido. Se o usuário digitar um número válido, verifique se o número que o usuário digitou é igual ao número gerado aleatoriamente pelo programa. Se o número for igual, imprima "Você acertou!". Caso contrário, imprima "Você errou!".

# Extra: Conte quantas tentativas o usuário precisou para acertar o número. Permita tentativas até o usuário acertar o número.
"""
import random as rd

def jogo_de_advinhacao(numero):
    numero_de_tentativas = 1
    numero_sorteado = rd.randint(1, 11)
    while numero < 1 or numero > 10:
        print("Número inválido.")
        numero = int(input("Digite um número inteiro entre 1 e 10: "))
    else:
        print("Número válido.")
    while numero != numero_sorteado:
        numero_de_tentativas += 1
        print("Você errou!")
        numero = int(input("Digite um número inteiro entre 1 e 10: "))
    print(f"Você acertou! O número sorteado foi {numero_sorteado}. Você precisou de {numero_de_tentativas} tentativas para acertar o número.")
    
    

numero = int(input("Digite um número inteiro entre 1 e 10: "))
jogo_de_advinhacao(numero)
"""

# Exercício 10: Faça um programa que solicita ao usuário escrever um texto e conta quantas vezes a letra "a" aparece no texto.

"""
frase = input("Digite uma frase ou palavra:")

def contagem_de_a(texto):
    contagem = 0
    for letra in texto: 
        if letra.lower() == "a":
            contagem += 1
    return contagem

print(frase)
print(f"O texto contém a letra 'a' {contagem_de_a(frase)} vezes.")
"""

"""
def palindromo (palavra):
    palavra = palavra.lower(). replace(" ", "")
    return palavra == palavra[::-1]

entrada = input("Digite uma palavra:")

if palindromo(entrada):
    print(f"{entrada} é um palíndromo!")
else:
    print(f"{entrada} não é um palíndrome.")
"""

# Substituir vogal

"""
def substituir_vogais():
    frase = input(" Escreva uma palavra ")
    return frase.lower().replace('a', '?!').replace('e', '?!').replace('i', '?!').replace('o', '?!').replace('u', '?!')

print(substituir_vogais())
"""

# Contar letras
"""
from cgi import print_arguments


def contar_letra(letra):
    texto = input(" Escreva uma frase ").lower()
    return texto.count(letra)

letra_a_contar = 'a'
print("Nome contem ", contar_letra(letra_a_contar), " letras "+ letra_a_contar)
"""

# Colocar letra maiúcula

"""
def letra_maiuscula():
    texto = input(" Escreva o seu nome completo ")
    return texto.upper()

print(letra_maiuscula())
"""

# Colocar letra minúscula

"""
def letra_minúscula():
    texto = input(" Escreva o seu nome completo: ")
    return texto.lower()
print(letra_minúscula())
"""

# Colocar nome maiúculo e sobrenome minúsculo

"""
def Escrever_nome_sobrenome():
    nome = input(" Escreva o seu nome completo: ")
    partes_nome = nome.split( )
    primeiro_nome = partes_nome[0]
    sobrenome = " ".join(partes_nome[1:])

    return primeiro_nome.upper() +" "+ sobrenome.lower()

print(Escrever_nome_sobrenome())
"""

# Contar a quantidade de caracteres de uma palavra

"""
def mostrar_nome_sobrenome(nome):
   
    partes_nome = nome.split( )
    nome_usuário = partes_nome[0]
    sobrenome_usuario = " ".join(partes_nome[1:])
    nome_completo = nome.upper()
    tamanho_nome_completo = len(nome)
    
    print("Nome: "+nome_completo.lower())
    print("tem ",tamanho_nome_completo, " caracteres ")


mostrar_nome_sobrenome(input(" Escreva o seu nome completo "))
"""

# Remover vogal

"""
def remover_vogais():
    frase = input(" Escreva uma palavra ")
    return frase.lower().replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', '')

print(remover_vogais())
"""
