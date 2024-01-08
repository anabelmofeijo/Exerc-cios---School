'''
Formação de Palavra:
34) Dada uma lista de letras, crie um programa que determine se é possível formar uma palavra específica.
Cada letra na lista só pode ser usada uma vez.
'''


print("***********************************************************")
print("*********************Formação de palavra*******************")
print('***********************************************************')
print("")
# Solicita ao usuário a lista de letras e a palavra a ser formada
lista_letras = input("Digite a lista de letras (sem espaços): ")
palavra_formar = input("Digite a palavra a ser formada: ")

# Converte a lista de letras para um conjunto
letras_disponiveis = set(lista_letras)

# Verifica se é possível formar a palavra
if all(letra in letras_disponiveis for letra in palavra_formar):
    print(f"É possível formar a palavra '{palavra_formar}'.")
else:
    print(f"Não é possível formar a palavra '{palavra_formar}'.")


# Dr.Stone

