# 1. Lista de frutas
frutas = ["maçã", "banana", "laranja", "uva", "pera"]
print(frutas[2])  # Imprime o terceiro elemento

# 2. Lista vazia com números
numeros = []
numeros.append(5)
numeros.append(10)
numeros.append(15)
print(numeros)

# 3. Lista de cores
cores = ["vermelho", "azul", "amarelo", "roxo"]
cores[1] = "verde"
print(cores)

# 4. Concatenação de listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = lista1 + lista2
print(lista3)

# 5. Removendo último elemento
elementos = [1, 2, 3, 4, 5, 6]
elementos.pop()
print(elementos)

# 6. Ordenando países
paises = ["Brasil", "Argentina", "Chile", "Portugal"]
paises.sort()
print(paises)

# 7. Maior e menor valor
numeros = [10, 5, 8, 2, 15]
print(f"Maior valor: {max(numeros)}")
print(f"Menor valor: {min(numeros)}")

# 8. Loop com animais
animais = ["gato", "cachorro", "coelho", "peixe"]
for animal in animais:
    print(animal)

# 9. Multiplicando números por 2
numeros = [1, 2, 3, 4, 5]
for i in range(len(numeros)):
    numeros[i] *= 2
print(numeros)

# 10. Adicionando elementos com while
lista = []
contador = 0
while len(lista) < 5:
    lista.append(contador)
    contador += 1
print(lista)

# 11. Removendo elementos com while
lista = [1, 2, 3, 4]
while lista:
    elemento_removido = lista.pop()
    print(f"Removendo {elemento_removido}")
    print(f"Lista atual: {lista}")
print("Lista vazia!")