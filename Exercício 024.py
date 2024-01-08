'''
Sequência de Collatz:
24) Crie um programa que solicite um número ao usuário e imprima a sequência de Collatz para esse número.
A sequência é gerada da seguinte forma: se o número for par, divida por 2; se for ímpar, multiplique por 3 e adicione 1.
 Repita até atingir 1.

'''

print ("********************************************************")
print ("*****************Sequência de Collatz*******************")
print ("********************************************************")
print("")

# Solicita ao usuário o número inicial
numero_inicial = int(input("Digite um número inteiro positivo para a Sequência de Collatz: "))

# Gera e exibe a sequência de Collatz para o número inicial fornecido
print("Sequência de Collatz:")
while numero_inicial != 1:
    print(numero_inicial, end=' ')
    if numero_inicial % 2 == 0:
        numero_inicial = numero_inicial // 2
    else:
        numero_inicial = 3 * numero_inicial + 1

print(1)  # Adiciona 1 para indicar o final da sequência
