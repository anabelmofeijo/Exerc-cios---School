'''
Troca de Palavras:
32) Peça ao usuário para digitar uma frase e duas palavras.
Substitua todas as ocorrências da primeira palavra pela segunda na frase.

'''


print("**********************************************************")
print("*******************Troca de strings***********************")
print("**********************************************************")
print ("")
# Solicita ao usuário inserir uma frase, a primeira palavra e a segunda palavra
frase = input("Digite uma frase: ")
palavra_original = input("Digite a primeira palavra: ")
palavra_nova = input("Digite a segunda palavra: ")

# Realiza a substituição na frase
frase_modificada = frase.replace(palavra_original, palavra_nova)

# Exibe o resultado
print(f"A frase modificada é: {frase_modificada}")

# Dr. Stone
