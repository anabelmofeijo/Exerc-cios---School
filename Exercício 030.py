'''
Compressão de Strings:
30) Crie um programa que comprima uma string, substituindo repetições
consecutivas de um caractere por esse caractere seguido pelo número de repetições.
Por exemplo, a string "aaabbbcc" seria comprimida para "a3b3c2".

'''


print ("********************************************")
print ("********************************************")
print ("")

# Solicita ao usuário a string a ser comprimida
string_original = input("Digite a string a ser comprimida: ")

# Inicializa variáveis
string_comprimida = ""
contador = 1

# Loop para percorrer a string
for i in range(1, len(string_original)):
    if string_original[i] == string_original[i - 1]:
        contador += 1
    else:
        string_comprimida += string_original[i - 1] + str(contador)
        contador = 1

# Adiciona o último caractere e seu contador à string comprimida
string_comprimida += string_original[-1] + str(contador)

# Exibe a string comprimida
print(f"A string comprimida é: {string_comprimida}")


# Dr. Stone
