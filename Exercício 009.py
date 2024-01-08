'''
Verificação de Triângulo:
9) Solicite ao usuário os comprimentos dos lados de um triângulo e
determine se ele é equilátero, isósceles ou escaleno, usando operadores lógicos.

'''

print("************************************")
print("****Verificação de um triângulo*****")
print("************************************")
print("")

l1 = float(input("Digite o L1: "))
l2 = float(input("Digite o l2: "))
l3 = float(input("Digite o L3: "))

# Vendo se é equilatero

if l1 == l2 and l2 == l3 and l1 == l3:
    print ("O triângulo é Equilatero")
elif l1 != l2 and l2 != l3 and l1 != l3:
    print("O triângulo é Escaleno")
else:
    print ("O triângulo é Isosceles")

#Dr. Stone
