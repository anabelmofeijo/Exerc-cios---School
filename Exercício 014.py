'''
Soma dos Números Pares até N:
14) Solicite um número inteiro positivo N ao usuário. Em seguida, calcule a soma dos números pares de 1 até N.

'''

print ("****************************************")
print ("****Soma dos números pares até N********")
print ("****************************************")
print ("")

n = int (input("Digite um número inteiro positivo: "))


soma_pares = 0

for c in range (1, n + 1):
    if c % 2 == 0:
        soma_pares += c

print (f'Soma dos números pares de {1} até {n} é: {soma_pares}')


