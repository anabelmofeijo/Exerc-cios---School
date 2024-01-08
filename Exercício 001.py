'''
1) Solicite ao usuário três notas, calcule a média aritmética e informe se o
 aluno foi aprovado (média maior ou igual a 9.5) ou reprovado.
'''
print ("************************************")
print ("**********Sistema Escolar***********")
print ("************************************")
print("")
mac = float(input("Digite a sua MAC: "))
p1 = float(input("Digite a sua nota da P1: "))
p2 = float(input("Digite a sua nota da P2: "))

media_final = (mac + p1 + p2)/3

print (f"A sua média final é de : {media_final:.2f} valores")

if media_final < 9.5:
    print ("Estás reprovado!")
else:
    print ("Estás apto cientista!")

# Dr. Stone
