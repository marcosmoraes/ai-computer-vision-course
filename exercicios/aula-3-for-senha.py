senha = "123"
for tentativa in range(3): #intervalo de 0 a 2
    senha_digitada = input("Digite a senha: ")
    if senha_digitada == senha:
        print("Senha correta!")
        break
    print("Senha incorreta, tente novamente")
else:
    print("Você excedeu o número de tentativas.")
