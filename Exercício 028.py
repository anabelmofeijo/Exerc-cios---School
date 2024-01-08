'''
Contagem de Palavras:
28) Peça ao usuário para digitar uma frase e conte o número de palavras na frase.
Considere que as palavras são separadas por espaços em branco.

'''

palavra = str(input("Digite uma frase: ")).upper().strip().split()
print (palavra)
print (f"Número de palavras: {len(palavra)}")

# Dr. Stone
