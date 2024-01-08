'''
Triângulo de Pascal:
23) Crie um programa que solicite um número N e imprima as primeiras N linhas do Triângulo de Pascal.
Cada número no triângulo é a soma dos dois números diretamente acima dele na linha anterior.

'''
print("***********************************************************")
print("*******************Triângulo PASCAL************************")
print("***********************************************************")
print("")
# Solicita ao usuário o número de linhas desejadas no Triângulo de Pascal
num_linhas = int(input("Digite o número de linhas desejadas no Triângulo de Pascal: "))

triangulo_pascal = []

# Constrói o Triângulo de Pascal
for linha in range(num_linhas):
    linha_atual = [1] * (linha + 1)
    for coluna in range(1, linha):
        linha_atual[coluna] = triangulo_pascal[linha - 1][coluna - 1] + triangulo_pascal[linha - 1][coluna]
    triangulo_pascal.append(linha_atual)

# Exibe o Triângulo de Pascal
for linha in triangulo_pascal:
    print(linha)

# Dr. Stone
