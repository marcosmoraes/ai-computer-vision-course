# Programa para calcular IMC
# Recebe dados do usuário
peso = input("Digite seu peso em kg: ")
altura = input("Digite sua altura em metros: ")

# Converte strings para float
peso = float(peso)
altura = float(altura)

# Calcula o IMC
imc = peso / (altura * altura)

# Mostra o resultado formatado
print(f"\nSeu IMC é: {imc:.2f}")

# Classifica o IMC
if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif imc < 25:
    print("Classificação: Peso normal")
elif imc < 30:
    print("Classificação: Sobrepeso")
else:
    print("Classificação: Obesidade")