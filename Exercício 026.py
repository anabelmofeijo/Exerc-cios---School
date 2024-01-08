'''
Anagramas:
26) Crie um programa que verifica se duas palavras são anagramas, ou seja,
se podem ser formadas pelas mesmas letras, independentemente da ordem.
Por exemplo, "listen" e "silent" são anagramas.

'''

print("*****************************************************")
print("**********************Anagramas**********************")
print("*****************************************************")
print("")

palavra1 = input("Digite a primeira palavra: ").lower()
palavra2 = input("Digite a segunda palavra: ").lower()

# Remove espaços em branco (opcional)
palavra1 = palavra1.replace(" ", "")
palavra2 = palavra2.replace(" ", "")

# Verifica se as palavras são anagramas
if sorted(palavra1) == sorted(palavra2):
    print(f"{palavra1} e {palavra2} são anagramas.")
else:
    print(f"{palavra1} e {palavra2} não são anagramas.")

# Dr. Stone
