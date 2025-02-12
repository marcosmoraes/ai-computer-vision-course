#Exemplos de laços for:
# Exemplo 1: Loop básico com range
for i in range(5):
    print(i)  # Imprime 0, 1, 2, 3, 4

# Exemplo 2: Loop com lista
frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(f"Eu gosto de {fruta}")

# Exemplo 3: Loop com range personalizado
for num in range(2, 11, 2):  # início, fim, passo
    print(num)  # Imprime números pares de 2 a 10

#Exemplos de laços while:
# Exemplo 1: Loop while básico
contador = 0
while contador < 5:
    print(contador)
    contador += 1

# Exemplo 2: Loop com break
senha = "123"
while True:
    tentativa = input("Digite a senha: ")
    if tentativa == senha:
        print("Senha correta!")
        break
    print("Senha incorreta, tente novamente")

# Exemplo 3: Loop com continue
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue  # Pula a iteração quando i é 3
    print(i)

#Mais exemplos de laços de repetição:
# Loop for com enumerate (quando precisamos do índice)
frutas = ["maçã", "banana", "uva"]
for indice, fruta in enumerate(frutas):
    print(f"Índice {indice}: {fruta}")

# Loop for com zip (para iterar sobre múltiplas listas simultaneamente)
nomes = ["Ana", "João", "Maria"]
idades = [25, 30, 35]
for nome, idade in zip(nomes, idades):
    print(f"{nome} tem {idade} anos")

# List comprehension (forma concisa de criar listas)
quadrados = [x**2 for x in range(5)]  # Cria lista: [0, 1, 4, 9, 16]

# While com else (executado quando while termina normalmente)
contador = 0
while contador < 3:
    print(contador)
    contador += 1
else:
    print("Loop concluído!")

# For com else (executado quando for termina normalmente)
for i in range(3):
    print(i)
else:
    print("Loop for concluído!")

# Loop while com multiple condições
x = 0
y = 5
while x < 3 and y > 0:
    print(f"x={x}, y={y}")
    x += 1
    y -= 1

