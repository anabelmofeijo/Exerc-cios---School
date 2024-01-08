'''
Validação de Número Primo:
13) Peça ao usuário um número e verifique se é um número primo.
Um número primo é aquele que é divisível apenas por 1 e por ele mesmo.

'''

print ("*********************************")
print ("****Validação de número primo****")
print ("*********************************")
print("")

n = int (input("Digite um número: "))


# Condição para saber os divisores de um número

d = 0
divisão = []
for c in range (1, n+1):
    if n % c == 0:
        divisão.append(c)

#Condição se é ou não um  número primo
if len(divisão) == 2:
    print ("É um número primo!")
else:
    print ("Não é um número primo!")



# Dr. Stone