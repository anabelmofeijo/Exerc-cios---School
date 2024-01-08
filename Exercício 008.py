'''
Validação de Senha:
8) Peça ao usuário que crie uma senha. Verifique se a senha tem pelo menos 8 caracteres
e contém pelo menos um número e um caractere especial.

'''
print ("*********************************")
print ("*******Validação de Senha********")
print ("*********************************")
print ('')

# Solicita ao usuário criar uma senha
senha = input("Digite uma senha: ")

# Verifica se a senha atende aos critérios
if len(senha) >= 8 and any(c.isdigit() for c in senha) and any(c in '!@#$%^&*(),.?":{}|<>' for c in senha):
    print("Senha válida! 😊")
else:
    print("A senha não atende aos critérios. Tente novamente.")


# Dr. Stone


