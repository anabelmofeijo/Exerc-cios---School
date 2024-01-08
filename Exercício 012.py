'''
Calculadora de Factorial:
12) Solicite um número inteiro ao usuário e calcule o factorial desse número.
O factorial de um número n é o produto de todos os inteiros de 1 a n.

'''

numero = int(input("Digite um número inteiro: "))
resultado = 1
count = 1
while count <= numero:
    resultado *= count
    count += 1
print(f"O fatorial de {numero} é {resultado}.")


# Dr. Stone

