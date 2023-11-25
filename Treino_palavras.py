def substituir_vogais():
    frase = input("Digite uma palavra ")
    return frase.lower().replace('a', '?!').replace('e', '?!').replace('i', '?!').replace('o', '?!').replace('u', '?!')

print(substituir_vogais())