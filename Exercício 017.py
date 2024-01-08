'''
Verificação de Números Primos até N:
17) Peça ao usuário um número inteiro N e exiba todos os números primos de 1 até N.

'''

print("***************************************************")
print("*****Verificação de números primios ate N**********")
print("***************************************************")
print("")

n = int(input('Digite um número inteiro: '))

números_primos = []

for c in range (1, n + 1):
    if c % 2 == 0:
        números_primos.append(c)

print (f"Todos os números primos de 1 até {n} sâo: {números_primos}")

