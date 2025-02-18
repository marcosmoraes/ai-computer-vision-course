senha = "123"
while True:
    tentativa = input("Digite a senha: ")
    if tentativa == senha:
        print("Senha correta!")
        break
    print("Senha incorreta, tente novamente")