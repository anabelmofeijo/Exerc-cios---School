'''
Números Perfeitos:
21) Um número perfeito é aquele que é igual à soma de seus divisores próprios (excluindo ele mesmo).
Peça ao usuário um número e determine se ele é perfeito.
'''

print ("******************************************")
print ("*********Números Perfeitos****************")
print ("******************************************")
print ("")

n = int (input("Digite um número para saber se é perfeito:  "))


números_primos = []

for c in range (1, n - 1):
    if c % 2 == 0:
        números_primos.append(c)

print (f"Todos os números primos de 1 até {n} sâo: {números_primos}")
print (f"A sua soma é igual a: {sum(números_primos)}")

if sum(números_primos) == n:
    print (f"O  número {n} é um número perfeito")
else:
    print (f"O número {n} não é um número perfeito")

# Dr.Stone




