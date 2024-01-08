'''
Série de Fibonacci com Restrições:
22) Peça ao usuário um número N e exiba os primeiros N termos da sequência de Fibonacci.
No entanto, para cada termo, exclua aqueles que são múltiplos de 3.

'''
# Solicita ao usuário o número de termos desejados
N = int(input("Digite o número de termos desejados na sequência de Fibonacci: "))

# Inicializa os dois primeiros termos
a, b = 0, 1

# Lista para armazenar os termos da sequência
fibonacci_sequence = [a, b]

# Gera os termos da Sequência de Fibonacci excluindo múltiplos de 3
while len(fibonacci_sequence) < N:
    next_term = a + b
    # Exclui termos múltiplos de 3
    if next_term % 3 != 0:
        fibonacci_sequence.append(next_term)
    a, b = b, next_term

# Exibe os termos
print(f"Os primeiros {N} termos da Sequência de Fibonacci (excluindo múltiplos de 3) são: {fibonacci_sequence}")
