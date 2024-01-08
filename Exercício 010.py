'''
Verificação de Ano Bissexto:
10) Solicite ao usuário um ano e determine se é bissexto ou não.

'''

print ("**************************************")
print ("******Verificação de ano bissexto*****")
print ("**************************************")
print ("")

ano = int (input("Digite o ano: "))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print (f"O ano  {ano} é bissexto!")
else:
    print (f"O ano {ano} não é bissexto!")
