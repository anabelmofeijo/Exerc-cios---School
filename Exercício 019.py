'''
Soma dos Dígitos:
19) Solicite um número inteiro ao usuário e calcule a soma dos seus dígitos.
Por exemplo, para o número 123, a soma seria 1 + 2 + 3 = 6.


'''

print("******************************************************")
print("*******************Soma dos Dígitos*******************")
print("")

n = int (input("Digite um número inteiro: "))

num = str (n)

soma = 0

for c in num:
    soma += int(c)

print (f"A soma dos dígitos é: {soma}")


# Dr. Stone





