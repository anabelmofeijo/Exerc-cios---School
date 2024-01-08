'''
Soma dos Quadrados:
25) Solicite um número ao usuário e determine se pode ser representado como a soma de dois quadrados.
Por exemplo, 5 pode ser representado como 1^2 + 2^2.
'''

print ("***************************************************")
print ("**************Soma dos Quadrados*******************")
print ("***************************************************")
print (" ")

def pode_ser_soma_quadrados(numero):
    limite = int(numero**0.5) + 1  # limite para a busca, evita cálculos desnecessários
    for i in range(limite):
        for j in range(limite):
            if i**2 + j**2 == numero:
                return True
    return False

# Solicita ao usuário o número a ser verificado
numero_verificar = int(input("Digite um número para verificar se pode ser representado pela soma de quadrados: "))

# Verifica se o número pode ser representado pela soma de quadrados
if pode_ser_soma_quadrados(numero_verificar):
    print(f"{numero_verificar} pode ser representado pela soma de quadrados.")
else:
    print(f"{numero_verificar} não pode ser representado pela soma de quadrados.")


# Dr. Stone
