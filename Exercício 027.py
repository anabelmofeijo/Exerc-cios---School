'''
Palíndromos:
27) Escreva um programa que verifica se uma palavra é um palíndromo, ou seja,
se ela é igual quando lida da esquerda para a direita e da direita para a esquerda. Exemplo: "radar" é um palíndromo.
'''


print ("*********************************************************")
print ("********************Palindromos**************************")
print ("*********************************************************")


palavra = str (input("Digite uma palavra: ")).upper()


if palavra == palavra[::-1]:
    print ("É palindromo")
else:
    print("Não é um palindromo")


# Dr. Stone
