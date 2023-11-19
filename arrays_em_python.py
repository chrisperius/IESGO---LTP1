# Dicionário
# Lista
# Tupla
# String


import array as arr

# Criar um array de inteiros vazios
meu_array = arr.array('i')

# Adicionar cinco no ao array
for i in range(5):
    num = int(input("Insira um número inteiro"))
    meu_array.append(num)

print("array resultante", meu_array)

# Somar os números do array
print(sum (meu_array))


# Encontrar o min e max
min_valor = min(meu_array)
max_valor = max(meu_array)
print(f"O menor valor é: {min_valor}\nO maior valor é: {max_valor}")

# Remover o último elemento
print(meu_array)
meu_array.pop()
print("Removido o último elemento", meu_array)

# Inverter a ordem
meu_array.reverse()
print("Lista invertida", meu_array)