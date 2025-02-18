#Operadores Aritméticos

# Adição (+)
a = 5 + 3  # 8

# Subtração (-)
b = 10 - 4  # 6

# Multiplicação (*)
c = 3 * 4  # 12

# Divisão (/)
d = 15 / 3  # 5.0 (resultado sempre é float)

# Divisão inteira (//)
e = 17 // 3  # 5 (descarta a parte decimal)

# Módulo (%)
f = 17 % 3  # 2 (resto da divisão)

# Exponenciação (**)
g = 2 ** 3  # 8 (2 elevado a 3)

#Operadores de Comparação:
# Igual a (==)
print(5 == 5)  # True

# Diferente de (!=)
print(5 != 3)  # True

# Maior que (>)
print(7 > 3)   # True

# Menor que (<)
print(2 < 8)   # True

# Maior ou igual a (>=)
print(5 >= 5)  # True

# Menor ou igual a (<=)
print(4 <= 4)  # True

#Operadores Lógicos:
# and (E lógico)
print(True and True)   # True
print(True and False)  # False

# or (OU lógico)
print(True or False)   # True
print(False or False)  # False

# not (NÃO lógico)
print(not True)        # False
print(not False)       # True

# Exemplo prático
idade = 25
tem_carteira = True
pode_dirigir = idade >= 18 and tem_carteira
print(pode_dirigir)    # True

#Operadores de Atribuição:
# Atribuição simples (=)
x = 5

# Atribuição com adição (+=)
x += 3  # equivalente a: x = x + 3

# Atribuição com subtração (-=)
x -= 2  # equivalente a: x = x - 2

# Atribuição com multiplicação (*=)
x *= 4  # equivalente a: x = x * 4

# Atribuição com divisão (/=)
x /= 2  # equivalente a: x = x / 2

#Operadores de Identidade e Pertencimento:
# is (verifica se objetos são o mesmo)
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a is b)  # False (listas diferentes)
print(a is c)  # True (mesma lista)

# in (verifica se elemento está contido)
lista = [1, 2, 3, 4, 5]
print(3 in lista)     # True
print(6 in lista)     # False
print(6 not in lista) # True

#Exemplo usando if/else em uma linha (operador ternário):
# Exemplo de if/else em uma linha
idade = 18
status = "Maior de idade" if idade >= 18 else "Menor de idade"
print(status)

# Outro exemplo
nota = 75
resultado = "Aprovado" if nota >= 60 else "Reprovado"
print(resultado)

#Exemplo usando elif:
# Classificação de notas
nota = 85

if nota >= 90:
    print("Nota A - Excelente")
elif nota >= 80:
    print("Nota B - Muito bom")
elif nota >= 70:
    print("Nota C - Bom")
elif nota >= 60:
    print("Nota D - Regular")
else:
    print("Nota F - Reprovado")

# Outro exemplo: classificação de faixa etária
idade = 25

if idade < 13:
    print("Criança")
elif idade < 20:
    print("Adolescente")
elif idade < 65:
    print("Adulto")
else:
    print("Idoso")

#Exemplos de Listas:
# Lista básica de números
numeros = [1, 2, 3, 4, 5]
print(numeros)

# Lista de strings
frutas = ["maçã", "banana", "laranja"]
print(frutas)

# Lista com diferentes tipos de dados
misturada = [1, "texto", 3.14, True]
print(misturada)

# Lista vazia
vazia = []
print(vazia)

# Acessando elementos da lista (índice começa em 0)
primeira_fruta = frutas[0]  # maçã
ultima_fruta = frutas[-1]  # laranja

# Modificando elementos
frutas[1] = "morango"  # Substitui "banana" por "morango"

# Adicionando elementos
numeros.append(6)  # Adiciona 6 ao final da lista
frutas.insert(1, "pera")  # Insere "pera" na posição 1

# Removendo elementos
numeros.remove(3)  # Remove o número 3
ultima = frutas.pop()  # Remove e retorna o último elemento

# Fatiando listas
primeiros_tres = numeros[0:3]  # Pega os três primeiros elementos
pares = numeros[::2]  # Pega elementos pulando de 2 em 2

# Lista de listas (matriz)
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz[0][1])  # Acessa o elemento 2 (primeira linha, segunda coluna)

# Operações com listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
concatenada = lista1 + lista2  # [1, 2, 3, 4, 5, 6]
multiplicada = lista1 * 2  # [1, 2, 3, 1, 2, 3]

## Comprimento da lista
numeros = [1, 2, 3, 4, 5]
tamanho = len(numeros)  # 5

# Encontrar valor máximo e mínimo
maior = max(numeros)  # 5
menor = min(numeros)  # 1

# Soma dos elementos
soma = sum(numeros)  # 15

# Ordenar lista
desordenada = [3, 1, 4, 1, 5, 9, 2]
desordenada.sort()  # Ordena a lista original
ordenada = sorted(desordenada)  # Cria nova lista ordenada

# Inverter lista
numeros.reverse()  # Inverte a lista original
invertida = numeros[::-1]  # Cria nova lista invertida
# Verificar se elemento existe na lista
tem_tres = 3 in numeros  # True ou False
