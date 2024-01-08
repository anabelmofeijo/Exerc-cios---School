'''
Comparação de Números:
6) Peça dois números ao usuário e informe qual é o maior, o menor ou se são iguais.
'''

print ("***********************************")
print ("******Comparação de Números********")
print ("***********************************")
print("")

n1 = float (input("Digite um número: "))
n2 = float (input("Digite outro número: "))

if n1 > n2:
    print (f"O maior número é: {n1}")
if n2 > n1:
    print (f"O maior número é: {n2}")

if n1 < n2:
    print (f"O menor número é: {n1}")
if n2 < n1:
    print (f"O menor número é: {n2}")
if n1 == n2:
    print ("Os números são iguais!")

# Dr. Stone
