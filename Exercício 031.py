'''
Contagem de Palavras em um Texto:
31) Crie um programa que solicite ao usuário inserir um texto completo e conte o
número de palavras distintas no texto, ignorando maiúsculas e minúsculas.

'''

print ("**********************************************************")
print ("**********************************************************")
print ("")
# Solicita ao usuário inserir um texto completo
texto = input("Digite um texto completo: ")

# Converte o texto para minúsculas e divide em palavras
palavras = texto.lower().split()

# Cria um conjunto para armazenar palavras distintas
palavras_distintas = set(palavras)

# Conta o número de palavras distintas
numero_palavras_distintas = len(palavras_distintas)

# Exibe o resultado
print(f"O número de palavras distintas no texto é: {numero_palavras_distintas}")

# Dr. Stone