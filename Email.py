import re
def valida_email(email):
    # validação de email usando expressão regular
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(padrao, email):
        return True
    else:
        return False
# Solicitar para inserir um email
email = input("Insira um email: ")

# Chamar a função de validação e mostrar o resultado
if valida_email(email):
    print("O email é válido.")
else:
    print("O email não é válido.")