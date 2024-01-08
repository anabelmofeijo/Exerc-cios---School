'''
Validação de Senha Forte:
33) Solicite ao usuário criar uma senha e verifique se ela atende aos seguintes critérios:
pelo menos 8 caracteres, contendo letras maiúsculas, letras minúsculas, números e caracteres especiais.

'''

print ("*************************************************************")
print ("**************Validação de Senha Forte***********************")
print ("*************************************************************")
print ("")
# Solicita ao usuário criar uma senha
senha = input("Digite uma senha: ")

# Verifica se a senha atende aos critérios
tem_maiuscula = any(c.isupper() for c in senha)
tem_minuscula = any(c.islower() for c in senha)
tem_numero = any(c.isdigit() for c in senha)
tem_caractere_especial = any(c in '!@#$%^&*(),.?":{}|<>' for c in senha)

if len(senha) >= 8 and tem_maiuscula and tem_minuscula and tem_numero and tem_caractere_especial:
    print("Senha forte! 😊")
else:
    print("A senha não atende aos critérios. Tente novamente.")

# Dr. Stone
