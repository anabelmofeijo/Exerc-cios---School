'''
Calculadora de Desconto:
3) Crie um programa que solicita o valor original de um produto e um percentual de desconto.
Calcule o valor final com o desconto aplicado.
'''

print ("*************************************")
print ("******Calculadora de desconto********")
print ("*************************************")
print ("")

# OBS: irá se aplicar um desconto de 5%

preço = int (input("Digite o preço do produto: "))

desconto = preço - (5 /100)*preço
print (f"O desconto de 5% do produto é de : {desconto:.0f}.00Kz")

# Dr. Stone

