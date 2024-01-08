'''
Classificação de Triângulos II:
11) Peça ao usuário os ângulos internos de um triângulo e determine
se ele é um triângulo válido. Se válido, classifique-o como agudo, obtuso ou retângulo com base nos ângulos.
'''

print('**********************************************')
print("*********Classificação de triângulo II********")
print("**********************************************")
print("")

# interação com o usuário
l1 = float(input("Digite o l1: "))
l2 = float(input("Digite o l2: "))
l3 = float(input("Digite o l3: "))

# Condição
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:

    print ("O triângulo é válido!")
    print (" ")
    a1 = int(input("Digite o 1º ângulo: "))
    a2 = int(input("Digite o 2º ângulo: "))
    a3 = int(input("Digite o 3º ângulo: "))
    # Condição
    if a1 == 90 and a2 == 90 and a3 == 90:
        print ("O triângulo é Agudo!")
    elif a1 == 90 or a2 == 90 or a3 == 90:
        print ("O triângulo é Rectângulo")
    elif a1 > 90 or a2 > 90 or a3 > 90:
        print ("O triângulo é obtuso!")
    else:
        print ("O triângulo é escaleno pois tds os seus ângulos internos são diferentes")

else:
    print ("O triângulo não é válido!")
