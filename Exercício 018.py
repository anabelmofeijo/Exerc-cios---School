'''
Calculadora de Factorial com Estrutura de Repetição:
18) Solicite um número inteiro ao usuário e calcule o factorial desse número usando uma estrutura de repetição.

'''
print('**********************************************')
print("**********************************************")
print("")

# Solicita um número inteiro positivo ao usuário
n = int(input("Digite um número inteiro positivo: "))

# Inicializa o resultado da fatorial
fatorial = 1

# Loop for para calcular a fatorial
for i in range(1, n + 1):
    fatorial *= i

# Exibe o resultado
print(f"A fatorial de {n} é: {fatorial}")


# Dr. Stone

