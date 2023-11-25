# String Methods

# Exemplo de Método replace()
"""

def replace_a():
    frase = input("Digite uma frase: ")
    return frase.replace('a', '@').replace('A', '@').replace('á', '@').replace('Á', '@')


print(replace_a())


# Exemplo de Método len() para contar o tamanho da string

def tamanho_do_texto(texto):
    return len(texto)

print(tamanho_do_texto("Pindamonhangaba"))

# Crie um contador de caracteres em que o usuário digite uma frase e o programa exiba quantos caracteres com uma mensagem
def contador():
    frase = input("Digite uma frase: ")
    # f'String....{variavel}
    return len(frase)
print(contador())


#Usar o método count() para contar quantas vezes uma letra aparece na frase.

def contador_de_a():
    texto = input("Digite uma fraseh: ")
    return f"A letra 'a' aparece {texto.count('a') + texto.count('á') + texto.count('A') + texto.count('Á')} vezes na frase."

print(contador_de_a())



# Usando o método Captalise()

def captalize():
    texto = input("Digite uma frase: ")
    return texto.capitalize()

print(captalize())



# Desafio: qual a diferença entre o método upper(), método swapcase() e o método lower()?
# R: O método upper() deixa todas as letras da frase em maiúscula.
# O método lower() deixa todas as letras da frase em minúscula.
# O método swuapcase() deixa todas as letras maiúsculas em minúsculas e vice-versa.

# Escreva um programa que armazena na variável email o endereço de email de um usuário. Solicite via console e exiba na tela o email digitado em letras minúsciulas.

def email_cadastro():
    email = input("Digite o seu endereço de Email: ")
    email = email.lower()
    return email

print(email_cadastro())

"""
"""
# Método split() e método strip():
# O método split() divide uma string em uma lista de strings, separando-as por um delimitador.
# Exemplo:

def seletor_de_nome():
    nome_completo = input("Escreva seu nome e sobrenome: ")
    primeiro_nome = nome_completo.split()[0]
    ultimo_nome = nome_completo.split()[-1]
    return f"Seu primeiro nome é {primeiro_nome} e seu último nome é {ultimo_nome}"

print(seletor_de_nome())

def remover_espaços():
    nome = input("Digite seu nome: ")
    return nome.strip()

print(remover_espaços())

def lista_de_usuarios():
    lista_de_usuarios = ["João", "Maria", "Jose", "Pedro", "Ana"]
    usuario_selecionado = int(input("Digite a posição do usuário: "))
    
    if 1 <= usuario_selecionado <= len(lista_de_usuarios):
        usuario_selecionado = lista_de_usuarios[usuario_selecionado - 1].strip()
        return f"Usuário selecionado: {usuario_selecionado}"
    else:
        return "Posição de usuário inválida."

print(lista_de_usuarios())
"""

#criar um menu de usuário com três funções a saber
### 1 - contar caracteres
### 2 - contar letras "a"
### 3 - substituir letras "a" por "@"
### 4 - sair do programa

def contar_caracteres():
    texto = input("Digite uma frase: ")
    return f"A frase digitada tem {len(texto)} caracteres."

def contar_a():
    texto = input("Digite uma frase: ")
    return f"A letra 'a' aparece {texto.lower().count('a')} vezes na frase."

def substituir_a_por_arroba():
    texto = input("Digite uma frase: ")
    texto_modificado = texto.replace('a', '@')
    return f"Frase com 'a' substituído por '@': {texto_modificado}"

def menu_usuario():
    while True:
        print("\nMENU DE USUÁRIO:")
        print("1 - Contar caracteres")
        print("2 - Contar letras 'a'")
        print("3 - Substituir letras 'a' por '@'")
        print("4 - Sair do programa")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            print(contar_caracteres())
        elif opcao == '2':
            print(contar_a())
        elif opcao == '3':
            print(substituir_a_por_arroba())
        elif opcao == '4':
            print("Programa encerrado. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

# Chamar a função do menu para iniciar o programa
menu_usuario()







